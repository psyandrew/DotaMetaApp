'''

def processdata(data, i):

    hero = {
        'name': '',
        'winrate': '',
        'facets': [],
        'lane presence': '',
        'items': [],
        'good match ups': [],
        'bad match ups': [],
    }

    #heroname
    name =  rawdataprofile[i]['herodata']['title'][0].split(' -')[0]
    hero['name'] = name

    #winrate
    #hero['winrate'] = float(rawdataprofile[i]['herodata']["Win Rate"][0][0:4])

    #facetsmeta
    facet_regex =r'^([A-Za-z\s]+)'
    facet_numbers = r'\d+\.\d+\s%'

    facetsAll = list(filter(lambda x: x != '', rawdataprofile[i]['herodata']["Facets"]))  
    
    facetlist = []
    
    facets = []

    for facet in facetsAll:

        facetname = re.findall(facet_regex, facet)
        facetnumbers = re.findall(facet_numbers, facet)


        if facetname[0] not in facetlist:
            result = {'name':facetname[0], 'pickrate':float(facetnumbers[0][0:4]), 'winrate':float(facetnumbers[1][0:4])}        
            facets.append(result)
            facetlist.append(facetname[0])
            continue

        if facetname[0] in facetlist:
            break
    
    hero['facets'] = facets


    #lanemeta
    laning_regex = [r'(Mid Lane)',r'(Safe Lane)',r'(Soft Support)',r'(Hard Support)',r'(Off Lane)',r'(Jungle)']
    lane_regex_numbers  =  r'(\d+\.\d+%)'

    lane_presence = rawdataprofile[i]['herodata']['Lane Presence'][0][55:len(rawdataprofile[i]['herodata']['Lane Presence'][0])]

    laning = [re.findall(el, lane_presence) for el in laning_regex if re.search(el, lane_presence)]

    lane_numbers =  re.findall(lane_regex_numbers, lane_presence)

    lane_presence =[{'lane':laning[x][0], 'rate': float(lane_numbers[2*x][:-1]),'winrate': float(lane_numbers[2*x + 1][:-1]),  }  for x in range(len(laning))]


    hero['lane presence'] = lane_presence


    #items
    items = rawdataprofile[i]['herodata']['Items'][0][58:len(rawdataprofile[i]['herodata']['Items'][0])]

    items = items.split(r'%')

    items = [' '.join(re.split(r'  ', el)) for el in items]

    itemwinrates = [float(el[-5:len (el)]) for el in items if el != '']

    itemnames = [ re.findall(r"^([A-Za-z\s(5)']+)",el) for el in items if el != '']

    for x in range(11):
        hero['items'].append({'item':itemnames[x][0], 'winrate':itemwinrates[x]})


    #goodmatchups
    matchups_regex_pattern = r'(?:^|\s)([A-Za-z\s\-]+?)\s(\d+\.\d+%)\s(\d+\.\d+%)'

    goodmatchups = rawdataprofile[i]['herodata']['Best Match Ups'][0][59:len(rawdataprofile[i]['herodata']['Best Match Ups'][0])]

    goodmatchups = re.findall(matchups_regex_pattern, goodmatchups)

    for goodmatchup in range(5):
        hero['good match ups'].append({'counters':goodmatchup[0], 'win rate':float(goodmatchup[2][0:4])})


    #badmatchups
    badmatchups = rawdataprofile[i]['herodata']['Worst Match Ups'][0][63:len(rawdataprofile[i]['herodata']['Worst Match Ups'][0])]

    badmatchups = re.findall(matchups_regex_pattern, badmatchups)
    

    for badmatchup in range(5):
        hero['bad match ups'].append({'countered by': badmatchup[0], 'win rate':float(badmatchup[2][0:4])})


    webdata.append(hero)

    return webdata



for x in range(len(rawdataprofile)):
    processdata(rawdataprofile, x)

processmainpage(rawdatamain)

with open('processed.json', 'w', encoding='utf-8') as json_file:
    json.dump(webdata, json_file, indent=4)

'''|




# Directory where your HTML files are stored
'''
main_page_directory = '..tmp/html'
profile_directory = '..tmp/html/profiles'

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
        '''           
        #Items
       
        '''
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
    with open('../tmp/processed/processed.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Scraping completed and data saved to ../tmp/processed/processed.json")


# Run the scraping functions
mainpage_data = scrape_mainpage(main_page_directory)
profile_data = scrape_profiles(profile_directory)

# Save data to JSON
save_data_to_json(mainpage_data, 'mainpage_scrape.json')
save_data_to_json(profile_data, 'profile_scrape.json')




if "facets" in data:
                facet_list = []
            
                for facet_entry in data["facets"]:

                    facet = Facet(
                        facet_name = facet_entry['name'],
                        pick_rate = facet_entry['pickrate'],
                        win_rate = facet_entry['winrate']
                    )
                    facet_list.append(facet)

                if "lane presence" in data:
                    laning_list = []

                    for laning_entry in data["lane presence"]:
                        laning = LanePresence(
                            lane=laning_entry['lane'],
                            presence_rate=laning_entry["rate"],
                            win_rate=laning_entry["winrate"]
                        )
                        laning_list.append(laning)

                if "items" in data:
                    item_list = []

                    for item_entry in data["items"]:
                        items = Item(
                            item_name =item_entry['item'], 
                            win_rate = item_entry['winrate']
                        )
                        item_list.append(items)

                if "good match ups" in data:
                    good_matchup_list = []

                    for good_matchup_entry in data['good match ups']:
                        good_matchups  = GoodMatchups(
                            counters = good_matchup_entry["counters"],
                            win_rate = good_matchup_entry["winrate"]
                        )
                        good_matchup_list.append(good_matchups)

                if "bad match ups" in data:
                    bad_matchup_list=[]

                    for bad_matchup_entry in data['bad match ups']:
                        bad_matchups  = BadMatchups(
                            countered = bad_matchup_entry["countered"],
                            win_rate = bad_matchup_entry['winrate']
                        )
                        bad_matchup_list.append(bad_matchups)


                        hero = Hero(
                name = data["name"],
                hero_id = data["hero_id"],
                success_rate = data["win_rate"],
                pick_rate = data["pick_rate"],
                ban_rate = data["ban_rate"],
                #attribute = data["attribute"],

                #facets = facet_list,
                #laning = laning_list,
                #items = item_list ,
                #good_matchup = good_matchup_list,
                #bad_matchup = bad_matchup_list
            )


"tw-p-2 tw-align-middle [&amp;:has([role=checkbox])]:tw-pr-0 [&amp;>[role=checkbox]]:tw-translate-y-[2px]"
"tw-flex tw-flex-col tw-items-start tw-gap-1"

<a href="/heroes/ringmaster" >
'''