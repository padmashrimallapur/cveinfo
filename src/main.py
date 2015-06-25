from download import download_file, unzip

url = "http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Modified.xml.zip"
xml_file = "nvdcve-2.0-Modified.xml"


if __name__ == "__main__":
    download_file(url, xml_file)
    unzip(xml_file)
