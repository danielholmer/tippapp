# -*- coding: utf-8 -*-
import requests
import re
import json

site = requests.get("https://api.www.svenskaspel.se/draw/stryktipset/draws").json()

match_teams = []
svenska_folket = []
tio_tidningar = []
odds = []
stat_map = {0:"one",1:"x", 2:"two"}


def get_matches():

	matchnr = 0

	while matchnr < 13:
		match_teams.append(site["draws"][0]["drawEvents"][matchnr]["eventDescription"])
		matchnr +=1

def get_stats(type_of_stat, map_collection, stat_list):
	try:
		matchnr = 0

		while matchnr < 13:
			temp = []
			
			for x in range(0,3):

				temp.append(site["draws"][0]["drawEvents"][matchnr][type_of_stat][map_collection[x]])
			
			stat_list.append(temp)

			matchnr +=1
	except:
		for x in range(0,13):
			stat_list.append([0,0,0])
	return stat_list

get_matches()

svenska_folket = get_stats("svenskaFolket", stat_map, svenska_folket)
tio_tidningar = get_stats("tioTidningar", stat_map, tio_tidningar)
odds = get_stats("odds", stat_map, odds)


for x in range(0, 13):
	print("{:<10}{:<30}{:^30}{:<20}{:<20}".format(x+1, 
		match_teams[x], 
		" - ".join(svenska_folket[x]), 
		" - ".join(map(str, tio_tidningar[x])), 
		" - ".join(map(str, odds[x]))))