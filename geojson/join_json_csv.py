#!/usr/bin/env python
"""
Join the wealth mine data and the shapes data to create input for a fast loading map
"""

import sys
import json
import csv
import re

data1={}

input1 = 'nyc-small-residential-class-1-average-tax-burden-by-zipcode - nyc-small-residential-class-1-average-tax-burden-by-zipcode.csv'
if len(sys.argv) > 1:
    input1 = sys.argv[1]

field1 = 'City'
if len(sys.argv) > 2:
    field1 = sys.argv[2]

field2 = 'CFSAUID'
if len(sys.argv) > 3:
    field2 = sys.argv[3]

"""
"style":{
//all SVG styles allowed
"fill":"red",
"stroke-width":"3",
"fill-opacity":0.6
}
"className":{
"baseVal":"A class name"
}
"""

# print >>sys.stderr,center_polygon.center_geolocation( [( 40.7127, -74.0059 ), ( 41.8369, -87.6847), ( 38.627003, -90.199402) ])

# cleanup1 = re.compile(' .*')
with open(input1) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        print >>sys.stderr, "key1: " , row['average_tax_burden'] , row['zip']
        data1[ row['zip'] ] = row['average_tax_burden']
# 
#             if field1 == 'Province':
#                 key1=row[field1]
#             else:
#                 key1=re.sub(cleanup1,'',row[field1])
# 
#             #print >>sys.stderr, "key1: " , key1
#             if key1 != 'OtherFSA':
#                 #print key1,row['Count'],row['fCount'], float(row['fCount'])/float(row['Count'])
#                 # data1[key1]= (row['Count'],row['fCount'], float(row['fCount'])/float(row['Count']))
#                 data1[key1]= (row['Count'],row['fCount'], 
#                     float(row['fCount'])/float(row['Count']),
#                     float(row['fWealth'])/float(row['Wealth']),
#                         row['Wealth'],row['fWealth']
#                     )
#             #print >>sys.stderr, "value: key1: " , data1[key1]
#         if not row['fCount']:
#             #print 'ISSUE1',cleanup1
#             pass

file1 = json.load(sys.stdin)

for item1 in file1['features']:
    try:
        #print item1
        # print item1['properties']['postalCode']

        item1['properties']['average_tax_burden'] = data1[ item1['properties']['postalCode']]


        #print >> sys.stderr, 'XXXQQQ',item1['geometry']['coordinates'][0]
        #print >> sys.stderr, 'XXXQQQ',item1['geometry']['type']
        #
        pass
    except Exception,e:
        print >>sys.stderr, 'issue1:', e, item1


json.dump(file1,sys.stdout)
