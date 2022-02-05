import numpy as np
import random as rand
import requests
import json
import RPi.GPIO as GPIO
import time
from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

#send_url = "http://api.ipstack.com/check?access_key=9652f32a1c57f789156e98e414aaf0ec"
#geo_req = requests.get(send_url)
#geo_json = json.loads(geo_req.text)
#latitude12 = geo_json['latitude']
#longitude12 = geo_json['longitude']
#my_location = geo_json['city']
latitude12 = 1
longitude12 = 1
my_location = "Urbana"
#print(latitude12)
#print(longitude12)
print(my_location)

#9652f32a1c57f789156e98e414aaf0ec

class rest:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon


def calc_dist(lat1,lon1,lat2,lon2):
  conv = (180/np.pi)
  lat1_rad = lat1/conv
  lat2_rad = lat2/conv
  lon1_rad = lon1/conv
  lon2_rad = lon2/conv
  dist = 3963.0*np.arccos(np.sin(lat1_rad)*np.sin(lat2_rad)+np.cos(lat1_rad)*np.cos(lat2_rad)*np.cos(lon2_rad-lon1_rad))
  dist_feet = dist*5280
  return dist_feet

list = []
# template for appending list
#list.append(rest("rest_name", latitude, longitude))

list.append(rest("Panda_Express", 40.1104272667539, -88.2290566668243))
list.append(rest("Sakanaya", 40.1101454940592, -88.2330757751514))
list.append(rest("Burrito_king", 40.1103987963004, -88.2327156257938))
list.append(rest("Bangkok_Thai", 40.1104023831122, -88.2324187391523))
list.append(rest("Maize", 40.1103992566387, -88.2389141470471))
list.append(rest("Jurrasic_grill", 40.1103900285138, -88.2331106442126))
list.append(rest("Fat_sandwich_comp", 40.1091829447208, -88.2316835163156))
list.append(rest("Cravings", 40.111328639924, -88.2290585248942))
list.append(rest("Naya_barneat", 40.110401481054, -88.2355325497705))
list.append(rest("Yogi_Korean", 40.1104061939512, -88.230009690612))

t_choice = rand.choice(list)

print(t_choice.name, t_choice.lat, t_choice.lon) 

lat11 = 40.115058255108245
long11 = -88.22856412577781
dist_to_del = calc_dist(t_choice.lat, t_choice.lon, lat11, long11)
print("Distance to today's foodle",dist_to_del)

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)


i = 0
while i == 0:
    lcd.clear()
    time.sleep(0.5)
    dist_to_del = calc_dist(t_choice.lat, t_choice.lon, lat11, long11)
    #dist_to_del = calc_dist(t_choice.lat, t_choice.lon, lat11, long11)
    lcd_line_1 = "Dist to Foodle:\n"
    lcd_line_2 = str(int(dist_to_del))
    lcd.message = lcd_line_1 + lcd_line_2 + " ft"
    
    if dist_to_del<= 300:
        i = 1
        print("foodle!")
        lcd_line_1 = "You have found\n"
        lcd_line_2 = "Today's Foodle!"
        lcd.message = lcd_line_1 + lcd_line_2
        break
    
    time.sleep(2)
