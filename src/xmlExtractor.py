import xml.etree.ElementTree as ET


entry_schema = '{http://scap.nist.gov/schema/feed/vulnerability/2.0}entry'
summary_schema = '{http://scap.nist.gov/schema/vulnerability/0.4}summary'
cve_schema = '{http://scap.nist.gov/schema/vulnerability/0.4}cve-id'
vulnerable_software_list_schema = '{http://scap.nist.gov/schema/vulnerability/0.4}vulnerable-software-list'
products_schema = '{http://scap.nist.gov/schema/vulnerability/0.4}product'


def xml_parser(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    cves = {}

    for element in root.findall(entry_schema):
        id = element.attrib['id']
        cve = {'id': element.find(cve_schema), 'summary': element.find(summary_schema)}
        vuln_softwares = []
        for product in element.find(vulnerable_software_list_schema).findall(products_schema):
            vuln_softwares.append(product.text)
        cve['vuln_softwares'] = vuln_softwares
        cves[id] = cve

    for key, value in cves.items():
        print("CVE: {0} \n\t Summary: {} \n Vulnerable Softwares: \n\t{}".format(
            key, value['summary'], "\n".join(value['vuln_softwares'])
        ))
