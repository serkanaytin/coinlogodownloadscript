import urllib
import json
import os
import simplejson

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'coinmarket.json')


with open(my_file, 'r') as json_file:
	data = json.load(json_file)

	for p in data["data"]:
		print("%s is %s" % (p["id"], p["symbol"]))
		urllib.urlretrieve('https://s2.coinmarketcap.com/static/img/coins/128x128/'+str(p["id"])+'.png', p["symbol"] + '.png')