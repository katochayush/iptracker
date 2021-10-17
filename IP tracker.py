import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print colorama.Fore.CYAN + """
  ___ ____     _____ ____      _    ____ _  _______ ____  
 |_ _|  _ \   |_   _|  _ \    / \  / ___| |/ / ____|  _ \ 
  | || |_) |____| | | |_) |  / _ \| |   | ' /|  _| | |_) |
  | ||  __/_____| | |  _ <  / ___ \ |___| . \| |___|  _ < 
 |___|_|        |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\
                                        
  Python IP Tracker - KATOCHAYUSH | github.com/katochayush
"""
print "\r"
while True:
		ip = raw_input("IP : ")
		url = "https://api.ipdata.co/"
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break
