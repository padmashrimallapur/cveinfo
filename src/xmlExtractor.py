import xml.etree.ElementTree as ET
from types import NoneType
from config import configs


class XMLReader():
    
    def __init__(self, debug=False):
        self.xml_file = configs['xml_file']
        self.cves = {}
        self.debug = debug

    def xml_parser(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
    
        for element in root.findall(configs['entry_schema']):
            cve_id = element.attrib['id']
            cve = {'cve_id': element.find(configs['cve_schema']).text,
                   'summary': element.find(configs['summary_schema']).text,
                   'published_datetime': element.find(configs['published_datetime_schema']).text
                   }
            vuln_softwares = []
            try:
                vuln_products = element.find(configs['vulnerable_software_list_schema'])
                if vuln_products is not None: 
                    for product in vuln_products.findall(configs['products_schema']):
                        vuln_softwares.append(product.text)
            except NoneType:
                if self.debug:
                    print "No vulnerable software list found for ID ".format(cve_id)
            
            cve['vuln_softwares'] = vuln_softwares
            
            self.cves[cve_id] = cve
        if self.debug:
            for key, value in self.cves.items():
                print("CVE: {0} \n\t Published date: {1} \n\t Summary: {2} \n\t Vulnerable Softwares: \n\t\t{3}".format(
                    key, value['published_datetime'],
                    value['summary'], "\n\t\t".join(value['vuln_softwares'])
                ))

    def get_cves(self):
        if len(self.cves) == 0:
            self.xml_parser()
        return self.cves