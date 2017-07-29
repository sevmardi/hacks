import pythonwhois
import json

#https://stackoverflow.com/questions/29773003/check-whether-domain-is-registered
domains = ['betbattles.io']

for dom in domains:
    details = pythonwhois.get_whois(dom)
    if details['contacts']['registrant'] == None:
        print('not registered')
    else:
        
    	print(details['expiration_date'])
    
