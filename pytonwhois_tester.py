import pythonwhois as whois
import json

#https://stackoverflow.com/questions/29773003/check-whether-domain-is-registered
domains = ['ipinfo.io','config.io','park.io']

available = []
unavailable = []

def run():
    for dom in domains:
        if dom is not None and dom != '':
            details = whois.get_whois(dom)
            if details['registrar']is None and details['expiration_date'] is not None:
                unavailable.append(dom)
                # print(details['registrar'])
            elif details['available']:
                available.append(dom)
                # print(details)

def printAvailability():
    print ("-----------------------------")
    print ("Unavailable Domains: ")
    print ("-----------------------------")
    for un in unavailable:
        print (un)
    print ("\n")
    print ("-----------------------------")
    print ("Available Domains: ")
    print ("-----------------------------")
    for av in available:
        print (av)


if __name__ == '__main__':
    run()
    printAvailability()
    
