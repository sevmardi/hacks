import requests
import sys
import time
import smtplib
import shelve
import hashlib
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from requests.exceptions import HTTPError

# Domains being monitored
urlList = ['http://', 'http://', 'https://betwizer.io', '']
dbfilename = 'domainVerify.db'
db = {}
dbDomains = []


def veriPyDomain(urllist):
    for url in urllist:
        try:
            r = requests.get(url, timeout=60)
            if r.status_code:
                hash0 = hashlib.md5(r.content)
                hashobj = hash0.hexdigest()
                domLis = [url, r.status_code, hashobj]
                dbDomains.append(domLis)
        except requests.exceptions.RequestException as e:
            errData = {'Domain': '%s' % url, 'Error': '%s' % e}
            db[str(time.asctime().split()[3])] = errData
            # storeDbase(db)
    return dbDomains


def smtpSender(sites):
    sender = ""  # Email account from which alert is gonna be sent
    receiver = ["", ""]  # Email recipients
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Alert - Domain"
        msg['From'] = sender
        msg['To'] = ",".join(receiver)
        text = "These domains are responding with HTTP Codes!!\n\n\n%s" % sites
        s = smtplib.SMTP('192.168.2.1')  # IP Address or hostname of SMTP server
        part1 = MIMEText(text, 'plain')
        msg.attach(part1)
        s.sendmail(sender, receiver, msg.as_string())
    except smtplib.SMTPException:
        print("Error: unable to send email")


def save_db(obj, db):
    for (n, value) in obj:
        db[n] = value
    db.close()


def load_db():
    db = shelve.open('fileHash.shelve')
    return db


def verify_db():
    file = Path('./fileHash.shelve')
    if file.is_file():
        return 1
    else:
        return 0


if __name__ == '__main__':
    urlL = veriPyDomain(urlList)
    urlU = [[url[0], url[2]] for url in urlL]
    dict_ = dict((key, value) for (key, value) in urlU)
    checkDb = verify_db()
    if checkDb == 1:
        fileHash = load_db()
        dbLasList = []
        for key in dict_.keys():
            if key in fileHash.keys():
                if not dict_[key] == fileHash[key]:
                    dbLasList.append([key, dict_[key]])
                else:
                    dbLasList.append([key, dict_[key]])
    else:
        dbSet = urlU
        smtpSender(dbSet)
        save_Db(dbSet, load_db())

    if dbLasList:
        dbSet = set([tuple(x) for x in dbLasList])
        smtpSender(dbSet)
        save_Db(dbSet, fileHash)
