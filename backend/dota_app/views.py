from django.http import JsonResponse
from mongoengine import DoesNotExist
from .models import  Hero

def test(request):
	return JsonResponse({'message': 'hi'}, safe=False, status=200)


def get_rosterdata(request):
	hero_roster = Hero.objects.all()
	
	hero_metadata = []


	for hero in hero_roster:
		hero_metadata.append({
				'name': hero['name'],
				'hero_id':hero['hero_id'],
				'success_rate':hero['success_rate'],
				'pick_rate':hero['pick_rate'],
				'ban_rate':hero['ban_rate'],
				'GPM':hero['GPM'],
				'XPM':hero['XPM'],
				'KDA':hero['KDA'],
				'attribute': hero['attribute'],
				
			})

	return JsonResponse(hero_metadata, safe=False, status=200)




def get_herodata(request, hero_id):
    try:
        hero = Hero.objects.get(hero_id=hero_id)  # Fetch the book by its ID

        hero_data = { 'name': hero['name'],
		'hero_id': hero['hero_id'],
    	'success_rate': hero['success_rate'],
    	'pick_rate': hero['pick_rate'],
    	'attribute': hero['attribute'],
    	'ban_rate':hero['ban_rate'],
    	'GPM':hero['GPM'],
		'XPM':hero['XPM'],
		'KDA':hero['KDA'],
		
    	'facets': [facet.to_dict() for facet in hero['facets']],
    	'laning': [laning.to_dict() for laning in hero['laning']],
    	'items': [items.to_dict() for items in hero['items']],
    	'good_matchup': [good_matchup.to_dict() for good_matchup in hero['good_matchup']],
    	'bad_matchup': [bad_matchup.to_dict() for bad_matchup in hero['bad_matchup']],
    	}	

        return JsonResponse(hero_data, safe=False, status=200)  # Return the book in JSON format
    except DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
