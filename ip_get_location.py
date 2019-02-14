from urllib.request import urlopen
import json
import pandas as pd

title= ['ip','latitude','longitude','country_name','region_name']
file = '53619-2001-3000.txt'

def iplist(file):
	ipList = []
	with open(file) as f:
		lines = f.readlines()
		for line in lines:
			ipList.append(line.strip())
	return ipList


def location(iplist):
    location = []
    for ip in iplist:
        url1 = 'http://api.ipstack.com/'
        url2 = '?access_key=733c2c3dff0c4f20348d4b84ea93f28f'
        URL = url1+ip+url2
        urlobj = urlopen(URL)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
        latitude, longitude, country_name, region_name = datadict['latitude'], datadict['longitude'], datadict['country_name'], datadict['region_name']
        location.append((ip,latitude,longitude,country_name,region_name))
    return location
#        print(longitude)
#        print(country_name)
#        print(region_name)
    
def tocsv(location): 

   data = pd.DataFrame(location,columns=title)
   data.to_csv('53619-2001-3000.csv',index =None)    
if __name__ == '__main__':
	tocsv(location(iplist(file)))
    
# json.loads(requests.get(url.format(ip)).text).get('region_name')
