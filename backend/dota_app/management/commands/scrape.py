import os
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from myapp.management.commands.process import result as meta_data  
import json


# Directory where your HTML files are stored

main_page_directory = r'..\\tmp\\html'
profile_directory = r'..\\tmp\\html\\profiles'

def parse_mainpage(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        
        metatable = soup.find('table')

        s_tier = []
        a_tier = []
        b_tier = []
        c_tier = []
        d_tier = []
            

        for row in metatable.find_all('tr'):
            s_class = row.find( class_="tw-rounded tw-w-6 tw-text-center tw-cursor-default tw-text-white tw-text-sm tw-font-bold tw-bg-violet-600")
            a_class = row.find( class_="tw-rounded tw-w-6 tw-text-center tw-cursor-default tw-text-white tw-text-sm tw-font-bold tw-bg-sky-600")
            b_class = row.find( class_="tw-rounded tw-w-6 tw-text-center tw-cursor-default tw-text-white tw-text-sm tw-font-bold tw-bg-emerald-600")
            c_class = row.find( class_="tw-rounded tw-w-6 tw-text-center tw-cursor-default tw-text-white tw-text-sm tw-font-bold tw-bg-amber-600")
            d_class = row.find( class_="tw-rounded tw-w-6 tw-text-center tw-cursor-default tw-text-white tw-text-sm tw-font-bold tw-bg-rose-600")

            if s_class:
                s_text = row.get_text(separator=' ', strip=True)
                s_tier.append(s_text)
         

            if a_class:
                a_text = row.get_text(separator=' ', strip=True)
                a_tier.append(a_text)


            if b_class:
                b_text = row.get_text(separator=' ', strip=True)
                b_tier.append(b_text)

            if c_class:
                c_text = row.get_text(separator=' ', strip=True)
                c_tier.append(c_text)

            if d_class:
                d_text = row.get_text(separator=' ', strip=True)
                d_tier.append(d_text)



        mainpagedata = [
            s_tier,
            a_tier,
            b_tier,
            c_tier,
            d_tier
        ]

        print( mainpagedata)

        return mainpagedata


#  parse the HTML profiles
def parse_profiles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        

        herodata = {
        'title': [],
        'type':'',
        'Facets': [],
        'Lane Presence':[],
        'Items': [],
        'Best Match Ups':[],
        'Worst Match Ups':[]

        }

        title = soup.find('title')

    
        herodata['title'].append(title.get_text(separator=' ', strip=True))

        pagesections = soup.find_all('section')
        pagedivs = soup.find_all('div')
        pagearticles = soup.find_all('article')

        #attributes
        if soup.find('tbody', class_='primary-all'):
            herodata['type'] = 'Universal'
        if soup.find('tbody', class_='primary-intelligence'):
            herodata['type'] = 'Intelligence'
        if soup.find('tbody', class_='primary-strength'):
            herodata['type'] = 'Strength'
        if soup.find('tbody', class_='primary-agility'):
            herodata['type'] = 'Agility'


        #FACETS
        for div in pagedivs:

            tables = div.find_all('table')

            for table in tables:
                if 'Facet' in table.get_text(): 

                    for row in table.find_all('tr'):
                        facet_text = []

                        for cell in row.find_all('td'):
                            facet_text.append(cell.get_text(separator=' ', strip=True))

                        facet_text_str = ' '.join(facet_text)
                        herodata['Facets'].append(facet_text_str)

        #Matchups, Laning Presence, Item
        for section in pagesections:

            header = section.find('header')

            if header:
                header_text = header.get_text(separator=' ', strip=True)

                if header and header_text == 'Lane Presence':
                    lp_text = section.get_text(separator=' ', strip=True)
                    herodata['Lane Presence'].append(lp_text)
                
                if 'Most Used Items' in header_text:
                    items_text = section.get_text(separator=' ', strip=True)
                    herodata['Items'].append(items_text) 

                if 'Best Versus' in header_text:
                    bestmatchups_text = section.get_text(separator=' ', strip=True)
                    herodata['Best Match Ups'].append(bestmatchups_text)

                if 'Worst Versus' in header_text:
                    worstmatchups_text = section.get_text(separator=' ', strip=True)
                    herodata['Worst Match Ups'].append(worstmatchups_text)

        #Win Rate
        winrates = soup.find('span', ['won', 'lost'])

        winrate_text = winrates.get_text(separator=' ', strip=True)
        herodata['Win Rate'] = winrate_text

        # Return extracted data as a dictionary
        return {
            'herodata': herodata
        }




def scrape_profiles(directory):
    all_profile_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            parsed_data = parse_profiles(file_path)
            all_profile_data.append(parsed_data)
    return all_profile_data


def scrape_mainpage(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            mainpage_data = parse_mainpage(file_path)
            return mainpage_data 

def save_data_to_json(data, filename):
    full_path = os.path.join('../tmp/scraped', f'{filename}.json')
    print(full_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Scraping completed and data saved to ../tmp/scraped")


# Run the scraping functions
mainpage_data = scrape_mainpage(main_page_directory)
profile_data = scrape_profiles(profile_directory)

# Save data to JSON
save_data_to_json(mainpage_data, 'mainpage_scrape')
save_data_to_json(profile_data, 'profile_scrape')




class Command(BaseCommand):
    help = 'Scrape and save main page and profile data to JSON files' 

    def handle(self, *args, **kwargs):
        # Run the scraping functions within the command's handle method
        mainpage_data = scrape_mainpage(main_page_directory)
        profile_data = scrape_profiles(profile_directory)

        # Save data to JSON
        save_data_to_json(mainpage_data, 'mainpage_scrape')
        save_data_to_json(profile_data, 'profile_scrape')
        
        # Print success message when done
        self.stdout.write(self.style.SUCCESS("Scraping completed successfully and data saved to JSON files."))