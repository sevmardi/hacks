import pythonwhois
import json

#https://stackoverflow.com/questions/29773003/check-whether-domain-is-registered
domains = ['woningnethollandrijnland.nl']

for dom in domains:
    details = pythonwhois.get_whois(dom)
    if not details:
        print('not registered')
    #response = json.loads(details)    
    #parsed = json.dumps(response)
    print(details)
    
