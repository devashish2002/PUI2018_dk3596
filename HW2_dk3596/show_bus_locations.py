import pylab as pl
import os
import json
import pandas as pd
import sys

key = sys.argv[1]
bus_no = sys.argv[2]
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

def show_locations(key, bus_no):

    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + str(key) + '&VehicleMonitoringDetailLevel=calls&LineRef=' + str(bus_no)  #+ '&VehicleMonitoringDetailLevel=calls&LineRef='+ BUS_id
#print url
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)

    data1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

    data2 = data1[0]['VehicleActivity']

    lines = len(data2)

    Latitude = []
    Longitude = []


    for i in range(lines):
    
        x = data2[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        y = data2[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        Latitude.append(x)
        Longitude.append(y)

    #print Latitude, Longitude
    #print 'Bus line : B52'
    print 'Number of Active Buses :', lines
    for i in range(len(data2)):
        print 'Bus ', i+1 ,'is at latitude ' , Latitude[i] , 'and ', Longitude[i]
        if i == lines:
            break



#print key
#print bus_no

show_locations(key, bus_no)






