import numpy as np
import random as rand
import requests
import json
import Rpi.GPIO as GPIO
import time
from RPLCD import CharLD

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

Green1 = GPIO.PWM(14, 100)
Green2 = GPIO.PWM(15, 100)
Green3 = GPIO.PWM(23, 100)
Green4 = GPIO.PWM(8, 100)
Green5 = GPIO.PWM(7, 100)
Red1 = GPIO.PWM(5, 100)
Red2 = GPIO.PWM(6, 100)
Red3 = GPIO.PWM(13, 100)
Red4 = GPIO.PWM(16, 100)
Red5 = GPIO.PWM(20, 100)

Green1.start(10)
Green1.start(10)
Green1.start(10)
Green1.start(10)
Green1.start(10)
Red1.start(10)
Red1.start(10)
Red1.start(10)
Red1.start(10)
Red1.start(10)


send_url = "http://api.ipstack.com/check?access_key=9652f32a1c57f789156e98e414aaf0ec"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude12 = geo_json['latitude']
longitude12 = geo_json['longitude']
my_location = geo_json['city']

print(latitude12)
print(longitude12)
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
list.append(rest("Burrito_king", 40.1103987963004, 88.2327156257938))
list.append(rest("Bangkok_Thai", 40.1104023831122, -88.2324187391523))
list.append(rest("Maize", 40.1103992566387, -88.2389141470471))
list.append(rest("Jurrasic_grill", 40.1103900285138, -88.2331106442126))
list.append(rest("Fat_sandwich_comp", 40.1091829447208, -88.2316835163156))
list.append(rest("Cravings", 40.111328639924, -88.2290585248942))
list.append(rest("Naya_barneat", 40.110401481054, -88.2355325497705))
list.append(rest("Yogi_Korean", 40.1104061939512, -88.230009690612))

t_choice = rand.choice(list)

print(t_choice.name, t_choice.lat, t_choice.lon) 

dist_to_del = calc_dist(t_choice.lat, t_choice.lon, latitude12, longitude12)
print(dist_to_del)

lcd = CharLD(cols = 16, row = 2, pin_rs = 37, pin_e = 35, pins_data = [33, 31, 29, 23])
i = 0
while i == 0:
  dist_to_del = calc_dist(t_choice.lat, t_choice.lon, latitude12, longitude12)
  lcd.write_string(u"Foodle Time")
  time.sleep(2)
  lcd.clear()
  lcd.write_string(u"Dist to Deliciousness")
  lcd.cursor_pos = (1,0)
  lcd.write_string(dist_to_del)

  if dist_to_del<= 300:
    Green1.ChangeDutyCycle(100)
    Green2.ChangeDutyCycle(100)
    Green3.ChangeDutyCycle(95)
    Green4.ChangeDutyCycle(90)
    Green5.ChangeDutyCycle(80)
    Red1.ChangeDutyCycle(15)
    Red2.ChangeDutyCycle(10)
    Red3.ChangeDutyCycle(0)
    Red4.ChangeDutyCycle(0)
    Red5.ChangeDutyCycle(0) 
    i = 1
    print("foodle!")
    break
    
  elif dist_to_del<= 600 and dist_to_del> 300:
    Green1.ChangeDutyCycle(95)
    Green2.ChangeDutyCycle(90)
    Green3.ChangeDutyCycle(85)
    Green4.ChangeDutyCycle(85)
    Green5.ChangeDutyCycle(80)
    Red1.ChangeDutyCycle(15)
    Red2.ChangeDutyCycle(15)
    Red3.ChangeDutyCycle(10)
    Red4.ChangeDutyCycle(0)
    Red5.ChangeDutyCycle(0) 
    
  elif dist_to_del<= 900 and dist_to_del> 600 :
    Green1.ChangeDutyCycle(85)
    Green2.ChangeDutyCycle(85)
    Green3.ChangeDutyCycle(80)
    Green4.ChangeDutyCycle(80)
    Green5.ChangeDutyCycle(75)
    Red1.ChangeDutyCycle(20)
    Red2.ChangeDutyCycle(20)
    Red3.ChangeDutyCycle(15)
    Red4.ChangeDutyCycle(10)
    Red5.ChangeDutyCycle(5) 
    
  elif dist_to_del<= 1200 & dist_to_del> 900:
    Green1.ChangeDutyCycle(75)
    Green2.ChangeDutyCycle(70)
    Green3.ChangeDutyCycle(65)
    Green4.ChangeDutyCycle(60)
    Green5.ChangeDutyCycle(60)
    Red1.ChangeDutyCycle(20)
    Red2.ChangeDutyCycle(15)
    Red3.ChangeDutyCycle(15)
    Red4.ChangeDutyCycle(10)
    Red5.ChangeDutyCycle(10) 

  elif dist_to_del<= 1500 & dist_to_del> 1200 :
    Green1.ChangeDutyCycle(65)
    Green2.ChangeDutyCycle(60)
    Green3.ChangeDutyCycle(55)
    Green4.ChangeDutyCycle(55)
    Green5.ChangeDutyCycle(50)
    Red1.ChangeDutyCycle(30)
    Red2.ChangeDutyCycle(30)
    Red3.ChangeDutyCycle(25)
    Red4.ChangeDutyCycle(25)
    Red5.ChangeDutyCycle(20) 
    
  elif dist_to_del<= 1800 and dist_to_del> 1500:
    Green1.ChangeDutyCycle(55)
    Green2.ChangeDutyCycle(55)
    Green3.ChangeDutyCycle(55)
    Green4.ChangeDutyCycle(57)
    Green5.ChangeDutyCycle(55)
    Red1.ChangeDutyCycle(40)
    Red2.ChangeDutyCycle(35)
    Red3.ChangeDutyCycle(30)
    Red4.ChangeDutyCycle(25)
    Red5.ChangeDutyCycle(20) 
    
  elif dist_to_del<= 2100 and dist_to_del> 1800:
    Green1.ChangeDutyCycle(50)
    Green2.ChangeDutyCycle(50)
    Green3.ChangeDutyCycle(50)
    Green4.ChangeDutyCycle(50)
    Green5.ChangeDutyCycle(50)
    Red1.ChangeDutyCycle(50)
    Red2.ChangeDutyCycle(50)
    Red3.ChangeDutyCycle(50)
    Red4.ChangeDutyCycle(50)
    Red5.ChangeDutyCycle(50) 
    
  elif dist_to_del<= 2400 and dist_to_del> 2100:
    Green1.ChangeDutyCycle(40)
    Green2.ChangeDutyCycle(40)
    Green3.ChangeDutyCycle(35)
    Green4.ChangeDutyCycle(35)
    Green5.ChangeDutyCycle(30)
    Red1.ChangeDutyCycle(70)
    Red2.ChangeDutyCycle(70)
    Red3.ChangeDutyCycle(65)
    Red4.ChangeDutyCycle(65)
    Red5.ChangeDutyCycle(60)
    
  elif dist_to_del<= 2700 and dist_to_del> 2400 :
    Green1.ChangeDutyCycle(30)
    Green2.ChangeDutyCycle(30)
    Green3.ChangeDutyCycle(25)
    Green4.ChangeDutyCycle(25)
    Green5.ChangeDutyCycle(20)
    Red1.ChangeDutyCycle(80)
    Red2.ChangeDutyCycle(80)
    Red3.ChangeDutyCycle(75)
    Red4.ChangeDutyCycle(75)
    Red5.ChangeDutyCycle(70)
    
  elif dist_to_del<= 3000 and dist_to_del> 2700:
    Green1.ChangeDutyCycle(20)
    Green2.ChangeDutyCycle(15)
    Green3.ChangeDutyCycle(10)
    Green4.ChangeDutyCycle(10)
    Green5.ChangeDutyCycle(5)
    Red1.ChangeDutyCycle(90)
    Red2.ChangeDutyCycle(93)
    Red3.ChangeDutyCycle(87)
    Red4.ChangeDutyCycle(85)
    Red5.ChangeDutyCycle(80) 
    
  elif dist_to_del<= 3300 and dist_to_del> 3000:
    Green1.ChangeDutyCycle(10)
    Green2.ChangeDutyCycle(10)
    Green3.ChangeDutyCycle(5)
    Green4.ChangeDutyCycle(5)
    Green5.ChangeDutyCycle(5)
    Red1.ChangeDutyCycle(100)
    Red2.ChangeDutyCycle(100)
    Red3.ChangeDutyCycle(100)
    Red4.ChangeDutyCycle(95)
    Red5.ChangeDutyCycle(90)
  time.sleep(300)