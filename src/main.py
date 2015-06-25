from util import download_file, unzip
from xmlExtractor import xml_parser

url = "http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Modified.xml.zip"
xml_file = "nvdcve-2.0-Modified.xml"
xml_zip = "nvdcve-2.0-Modified.xml.zip"


if __name__ == "__main__":
    # download_file(url, xml_zip)
    # unzip(xml_zip)
    xml_parser(xml_file)
