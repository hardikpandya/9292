import datetime #date and time fetching
import urllib
import webbrowser #for opening links in the in-app browser
now= datetime.datetime.now()
print datetime.time(now.hour, now.minute)
# creating shorthands for larger variable names
nh = now.hour
nm = now.minute
nd = now.day
nmonth = now.month
###############################################
#print now.day
#print now.month
#print now.year
linkq = “http://9292.nl/en/journeyadvice/delft_bushalte-aula-tu/delft_brahmslaan-95/departure/2013-%02d-%02dT%02d%02d?train=off&tram=off” % (nmonth, nd, nh, nm) #creating the URL
print linkq #optional to print the created URL
webbrowser.open(linkq) #opening URL in the in-app browser
