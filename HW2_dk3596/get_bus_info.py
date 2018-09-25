import pylab as pl
import os
import json
import pandas as pd
import sys
import csv

key = sys.argv[1]
bus_no = sys.argv[2]
csv_file = sys.argv[3]
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

pl.rc('font', size=15)

def show_locations(key, bus_no, csv_file):

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
    #print 'Number of Active Buses :', lines
    #for i in range(len(data2)):
    #    print 'Bus ', i+1 ,'is at latitude ' , Latitude[i] , 'and ', Longitude[i]
    #    if i == lines:
     #       break

    labels = ['Latitude', 'Longitude', 'Stops', 'Status']

    status_new = []
    status_new.append(labels)
    for i in range(lines):
        status = []

        if str(data2[i]['MonitoredVehicleJourney']['OnwardCalls'])=='{}':
            st = 'N/A'
            stop = 'N/A'
        else:

            st = str(data2[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
            stop = str(data2[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        status.append(Latitude[i])
        status.append(Longitude[i])
        status.append(stop)
        status.append(st)
        status_new.append(status)
    

    with open(csv_file, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(status_new)
#print key
#print bus_no

show_locations(key,bus_no,csv_file)






