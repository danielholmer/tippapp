# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

import json

x=0
i=0
y=0
etta = ""
match=""
procent=[]
tio=[]
odd=[]
ev =[]
samlad_print=[]
r = requests.get("http://tipsrader.se")
site = r.text
soup = BeautifulSoup(site, "html.parser")
#print(soup.find_all(class_="teamname"))



for proc in soup.find_all(class_="percentinfo"):
	if i>0 and i < 14:
		procent.append(proc.text)
	i=i+1


result = requests.get("https://api.www.svenskaspel.se/draw/stryktipset/draws").json()
#draw = result["draws"]
#for ele in draw:
#       for e in ele:
#               print (e)

try: 
	for a in range(0,13):
		
		if (result["draws"][0]["drawEvents"][a]["tioTidningar"]) != None:
			tidning = (result["draws"][0]["drawEvents"][a]["tioTidningar"])
			if str(tidning["one"]) != "10" :
						etta = (str(tidning["one"])+ " ")
			else:
				etta = (str(tidning["one"]))
		
		if (result["draws"][0]["drawEvents"][a]["odds"]) != None:
			
			odds = (result["draws"][0]["drawEvents"][a]["odds"])
		event = (result["draws"][0]["drawEvents"][a]["eventNumber"])


		tio.append(etta +"  " +  str(tidning["x"]) +"  "+  str(tidning["two"]))
		odd.append(str(odds["one"])+"  " +  str(odds["x"]) +"  "+  str(odds["two"]))
		#odd.append(y)
		ev.append(str(event))
	

	#	print (ev)
	print("------------------------------------------------------------------------------------------------------------")
	print("{:<10}{:^30}{:^30}{:<20}{:^20}".format("Match", "Lag", "Svenska folket", "Tio tidningar", "Odds"))
	print("------------------------------------------------------------------------------------------------------------")

	for lag in soup.find_all(class_="teamname"):
		#res = soup.find_all(class_="card_red_0")

		if x == 1:
			match = match + " - " + lag.text
			#print (match + "   " + procent[y])
			print("{:<10}{:<30}{:^30}{:<20}{:<20}".format(ev[y], match, procent[y], tio[y], odd[y]))
			samlad_print.append(procent[y])
			x = 0
			y +=1
		else:
			match = (lag.text)
			x=x+1

	print("------------------------------------------------------------------------------------------------------------")	
except:
	print("Något är fel. Troligen har Svenska spel inte uppdaterat sina odds.")
#print(samlad_print)