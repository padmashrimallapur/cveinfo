#!/usr/bin/env python

from util import download_file, parse_vulnerable_softwares, send_email
from xmlExtractor import XMLReader

if __name__ == "__main__":
    download_file()
    xmlReader = XMLReader()
    xmlReader.xml_parser()
    
    vulnearble = parse_vulnerable_softwares(xmlReader.get_cves())
    
    if len(vulnearble) > 0:
        msg = "{}".format("\n".join(vulnearble[::-1]))
        print msg
        send_email(msg)
