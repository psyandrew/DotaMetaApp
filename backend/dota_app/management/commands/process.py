import json
import re
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Processes JSON data and outputs it to a file"

    def handle(self, *args, **kwargs):
        # Initialize data variables
        webdata = []
        data_dir = os.path.abspath('../tmp/scraped/')
        self.stdout.write(f"Checking full path: {data_dir}")

        # Check if the directory exists
        if os.path.exists(data_dir):
            self.stdout.write("Yes, the path exists")
        else:
            self.stdout.write("NO, the path does NOT exist")
            return

        # Define the file paths for the JSON files
        file_path_mp = os.path.join(data_dir, 'mainpage_scrape.json')
        file_path_profile = os.path.join(data_dir, 'profile_scrape.json')
        file_path_KDAGPMXPM = os.path.join(data_dir, 'KDAGPMXPM_scrape.json')

        # Load main page data
        if os.path.isfile(file_path_mp):
            with open(file_path_mp, 'r') as file:
                rawdatamain = json.load(file)
            self.stdout.write("Main page data loaded successfully.")
        else:
            self.stdout.write("Main page file does NOT exist at the path.")
            return

        # Load profile data
        if os.path.isfile(file_path_profile):
            with open(file_path_profile, 'r') as file:
                rawdataprofile = json.load(file)
            self.stdout.write("Profile data loaded successfully.")
        else:
            self.stdout.write("Profile file does NOT exist at the path.")
            return

        # Load KDAGPMXPM data
        if os.path.isfile(file_path_KDAGPMXPM):
            with open(file_path_KDAGPMXPM, 'r') as file:
                rawdataKDAGPMXPM = json.load(file)
            self.stdout.write("KDA GPM XPM data loaded successfully.")
        else:
            self.stdout.write("KDAGPMXPM file does NOT exist at the path.")
            return

        # Processing main page data
        def processmainpage(data):
            namepatterns = [
                r'^(.*?)\sS\s',
                r'^(.*?)\sA\s',
                r'^(.*?)\sB\s',
                r'^(.*?)\sC\s',
                r'^(.*?)\sD\s'
            ]
            result = []

            for tier in rawdatamain:
                for hero in tier:
                    rates = re.findall(r'\d+\.\d+', hero)
                    if re.search(namepatterns[0], hero):
                        result.append({
                            'name': re.findall(namepatterns[0], hero)[0],
                            'win_rate': float(rates[0]),
                            'pick_rate': float(rates[2]),
                            'ban_rate': float(rates[4]),
                        })
            return result

        result = processmainpage(rawdatamain)
        
        # Process profile data
        def processdata(data, i):
            hero = {
                'name': '',
                'hero_id': '',
                'attribute': '',
                'facets': [],
                'lane presence': '',
                'items': [],
                'good match ups': [],
                'bad match ups': [],
            }

            # Parse hero name and other properties here as in the original script
            hero['name'] = rawdataprofile[i]['herodata']['title'][0].split(' -')[0]
            hero['hero_id'] = hero['name'].replace(" ", "").lower()
            hero['attribute'] = rawdataprofile[i]['herodata']['type']
            # Add facet, lane, items, good and bad matchups processing logic here...
            webdata.append(hero)

        # Process KDAGPMXPM data
        GXPMKDA = []
        def processKDAGPMXPM(data):
            # Processing logic here...
            for x in data["Hero stats - DOTABUFF - Dota 2 Stats KDA.html"]:
                # KDA data processing
                pass

        # Process each profile and add to webdata
        for x in range(len(rawdataprofile)):
            processdata(rawdataprofile, x)

        processKDAGPMXPM(rawdataKDAGPMXPM)

        # Final processing to merge results
        result.append(webdata)

        # Save the processed data
        output_dir = os.path.abspath('../tmp/processed/')
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, 'processed.json'), 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, indent=4)
        self.stdout.write("Data processing complete and saved to processed.json.")



