import os
import json

from mongoengine import DoesNotExist
from django.core.management.base import BaseCommand
from myapp.models import Hero, Facet, LanePresence, Item, GoodMatchups, BadMatchups
from myapp.management.commands.process import result as meta_data



class Command(BaseCommand):
    help = 'Updates the database with new meta data'

    def handle(self, *args, **kwargs):

        
        for data in meta_data[0]:

            try:
                hero = Hero.objects.get(hero_id=data["hero_id"])
                print(f"Updating hero: {hero.name}")
                
                hero['success_rate'] = data["win_rate"]
                hero['pick_rate'] = data["pick_rate"]
                hero['ban_rate'] = data["ban_rate"]
                hero.attribute = data["attribute"]
                hero.XPM = data["XPM"]
                hero.GPM = data["GPM"]
                hero.KDA = data["KDA"]


                if "facets" in data:
                    facet_list = []
                
                    for facet_entry in data["facets"]:

                        facet = Facet(
                            facet_name = facet_entry['name'],
                            pick_rate = facet_entry['pickrate'],
                            win_rate = facet_entry['winrate']
                        )
                        facet_list.append(facet)

                    hero['facets'] = facet_list

                if "lane presence" in data:
                    laning_list = []

                    for laning_entry in data["lane presence"]:
                        laning = LanePresence(
                            lane=laning_entry['lane'],
                            presence_rate=laning_entry["rate"],
                            win_rate=laning_entry["winrate"]
                        )
                        laning_list.append(laning)

                    hero['laning'] = laning_list

                if "items" in data:
                    item_list = []

                    for item_entry in data["items"]:
                        items = Item(
                            item_name =item_entry['item'], 
                            win_rate = item_entry['winrate']
                        )
                        item_list.append(items)

                    hero['items'] = item_list

                if "good match ups" in data:
                    good_matchup_list = []

                    for good_matchup_entry in data['good match ups']:
                        good_matchups  = GoodMatchups(
                            counters = good_matchup_entry["counters"],
                            win_rate = good_matchup_entry["winrate"]
                        )
                        good_matchup_list.append(good_matchups)

                    hero['good_matchup'] = good_matchup_list

                if "bad match ups" in data:
                    bad_matchup_list=[]

                    for bad_matchup_entry in data['bad match ups']:
                        bad_matchups  = BadMatchups(
                            countered = bad_matchup_entry["countered"],
                            win_rate = bad_matchup_entry['winrate']
                        )
                        bad_matchup_list.append(bad_matchups)

                    hero['bad_matchup'] = bad_matchup_list

                hero.save()


            except Hero.DoesNotExist:
                hero = Hero(hero_id=data["hero_id"])
                print(f"Creating new hero: {data['name']}")
                
                hero.name = data["name"]
                hero.hero_id = data["hero_id"]
                hero.success_rate = data["win_rate"]
                hero.pick_rate = data["pick_rate"]
                hero.ban_rate = data["ban_rate"]
                hero.attribute = data["attribute"]
                hero.XPM = data["XPM"]
                hero.GPM = data["GPM"]
                hero.KDA = data["KDA"]
                

                if "facets" in data:
                    facet_list = []
                
                    for facet_entry in data["facets"]:

                        facet = Facet(
                            facet_name = facet_entry['name'],
                            pick_rate = facet_entry['pickrate'],
                            win_rate = facet_entry['winrate']
                        )
                        facet_list.append(facet)

                    hero['facets'] = facet_list

                if "lane presence" in data:
                    laning_list = []

                    for laning_entry in data["lane presence"]:
                        laning = LanePresence(
                            lane=laning_entry['lane'],
                            presence_rate=laning_entry["rate"],
                            win_rate=laning_entry["winrate"]
                        )
                        laning_list.append(laning)

                    hero['laning'] = laning_list

                if "items" in data:
                    item_list = []

                    for item_entry in data["items"]:
                        items = Item(
                            item_name =item_entry['item'], 
                            win_rate = item_entry['winrate']
                        )
                        item_list.append(items)

                    hero['items'] = item_list

                if "good match ups" in data:
                    good_matchup_list = []

                    for good_matchup_entry in data['good match ups']:
                        good_matchups  = GoodMatchups(
                            counters = good_matchup_entry["counters"],
                            win_rate = good_matchup_entry["winrate"]
                        )
                        good_matchup_list.append(good_matchups)

                    hero['good_matchup'] = good_matchup_list

                if "bad match ups" in data:
                    bad_matchup_list=[]

                    for bad_matchup_entry in data['bad match ups']:
                        bad_matchups  = BadMatchups(
                            countered = bad_matchup_entry["countered"],
                            win_rate = bad_matchup_entry['winrate']
                        )
                        bad_matchup_list.append(bad_matchups)

                    hero['bad_matchup'] = bad_matchup_list   
                
                

                hero.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated the database with new meta data!'))
