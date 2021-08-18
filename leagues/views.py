from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),

		# Aquí van los filtros. Se hace un nombre de variable en el diccionario
		# Luego se especifica el nombre del modelo, objects, y lo que quiero
		# que se ejecute (en este caso, filtros de distinto tipo).
		# Luego name__contains indica lo que quiero filtrar

		# 1. Find all baseball leagues | 
		# International Collegiate Baseball Conference,
		# Atlantic Federation of Amateur Baseball Players

		'baseball_league' : League.objects.filter(name__contains='baseball'),



		# 2. Find all womens' leagues |
		# International Association of Womens' Basketball Players,
		# Transamerican Womens' Football Athletics Conference

		'women_league' : League.objects.filter(name__contains='women'),



		#3. Find all leagues where sport is any type of hockey |
		# International Conference of Amateur Ice Hockey,
		# Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
		
		'hockey_league' : League.objects.filter(name__contains='hockey'),
		


		# 4. Find all leagues where sport is something OTHER THAN football |
		# International Conference of Amateur Ice Hockey,
		# International Collegiate Baseball Conference,
		# Atlantic Federation of Amateur Baseball Players,
		# Atlantic Federation of Basketball Athletics,
		# Atlantic Soccer Conference,
		# International Association of Womens' Basketball Players,
		# Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
		
		'no_football_league' : League.objects.exclude(name__contains='football'),
		
		
		
		# 5. Find all leagues that call themselves "conferences" |
		# International Conference of Amateur Ice Hockey,
		# International Collegiate Baseball Conference,
		# Atlantic Soccer Conference,
		# American Conference of Amateur Football,
		# Transamerican Womens' Football Athletics Conference,
		# Pacific Ice Hockey Conference

		'conferences_league' : League.objects.filter(name__contains='conference'),
		
		
		
		# 6. Find all leagues in the Atlantic region |
		# Atlantic Federation of Amateur Baseball Players,
		# Atlantic Federation of Basketball Athletics,
		# Atlantic Soccer Conference,
		# Atlantic Amateur Field Hockey League

		'atlantic_league' : League.objects.filter(name__contains='atlantic'),



		# 7. Find all teams based in Dallas |
		# Dallas Nets,
		# Dallas Angels

		'dallas_teams' : Team.objects.filter(location__contains='dallas'),



		# 8. Find all teams named the Raptors |
		# Atlanta Raptors,
		# Golden State Raptors

		'raptor_teams' : Team.objects.filter(team_name__contains='raptors'),



		# 9. Find all teams whose location includes "City" |
		# Mexico City Cave Spiders,
		# Kansas City Spurs

		'city_teams' : Team.objects.filter(location__contains='city'),



		# 10. Find all teams whose names begin with "T" | 
		# Alberta Texans, Michigan Timberwolves,
		# Manitoba Tiger-Cats, Colorado Twins
		
		'tea_teams' : Team.objects.filter(team_name__startswith='t'),
		

		# 11. Return all teams, ordered alphabetically by location | 
		# *too many to list*

		'teams_lists' : Team.objects.order_by('location'),
		


		# 12. Return all teams, ordered by team name in reverse alphabetical order |
		# *too many to list*

		# Esto ordena por nombre de equipo al revés

		'reversed_teams' : Team.objects.all().order_by('-team_name'),



		# 13. Find every player with last name "Cooper" |
		# Joshua Cooper, Landon Cooper, Michael Cooper, Alexander Cooper
		
		'the_cooper' : Player.objects.filter(last_name__contains='Cooper'),



		# 14. Find every player with first name "Joshua" |
		# Joshua Cooper, Joshua Hayes, Joshua Henderson, Joshua Long,
		# Joshua Coleman, Joshua White, Joshua Parker, Joshua Smith

		'the_joshua' : Player.objects.filter(first_name__contains='joshua'),



		# 15. Find every player with last name "Cooper" EXCEPT FOR Joshua |
		# Landon Cooper, Michael Cooper, Alexander Cooper

		'yes_cooper_no_joshua' : Player.objects.filter(last_name__contains = 'cooper').exclude (first_name__contains ='joshua'),



		# 16. Find all players with first name "Alexander" OR first name "Wyatt" |
		# Wyatt Bell, Alexander Bailey, Wyatt Peterson, Alexander Wright,
		# Wyatt Alexander, Wyatt Bennett, Alexander Parker, Alexander Adams,
		# Alexander Walker, Alexander Flores, Alexander Cooper

		'alex_wyatt' : Player.objects.filter(first_name__contains=['Alexander', 'Wyatt'])
		
		
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
