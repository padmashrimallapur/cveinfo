import os
import urllib2
import zipfile
from config import configs
import smtplib


def download_file():
    xml_url = urllib2.urlopen(configs['xml_url'])
    with open(configs['xml_zip'], "wb") as writeFile:
        writeFile.write(xml_url.read())
    xml_url.close()
    unzip()


def unzip():
    zip_file = zipfile.ZipFile(configs['xml_zip'])
    zip_file.extractall(".")
    zip_file.close()
    

def get_old_cves():
    old_cve_id = []
    if os.path.exists(configs['cvedb']):
        with open(configs['cvedb'], 'r') as db:
            old_cve_id = db.read().split("\n")
        
    return old_cve_id

def update_cve_database(cve):
    with open(configs['cvedb'], 'a') as db:
            db.write("%s\n" %cve)   


def parse_vulnerable_softwares(cves):
    vulnerable_cve = []

    old_cve = get_old_cves()
    for key, cve in cves.items():
        summary = cve['summary'].lower()
        for search in configs['search_keys']:
            if search in summary and key not in old_cve:
                update_cve_database(key)
                vulnerable_cve.append("https://web.nvd.nist.gov/view/vuln/detail?vulnId={} \n\t Published date: {} \n\t Summary: {} \n\t Vulnerable Softwares: \n\t\t{}".format(
                key, cve['published_datetime'], cve['summary'], "\n\t\t".join(cve['vuln_softwares'])))
    
    return list(set(vulnerable_cve))

def send_email(body_msg):
    from_id = "From: %s" % configs['from_id']
    to_id = "To: %s" % ", ".join(configs['email_id'])
    subject = "New CVE's published\n"
    
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (from_id, to_id, subject, body_msg))
    
    smpt_send = smtplib.SMTP(configs['smpt_addr'], configs['smpt_port'])
    smpt_send.sendmail(from_id, to_id, msg)
    smpt_send.quit()
    
    
    