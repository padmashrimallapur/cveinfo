
configs = {
           "search_keys":["ssl", "ssh", "httpd", "glibc", "xss",  "cross-site", "tomcat"],
           "cvedb": "sentemailcvedb",
           
           "xml_url": "http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-Modified.xml.zip",
           "xml_zip": "nvdcve-2.0-Modified.xml.zip",
           "xml_file": "nvdcve-2.0-modified.xml",
           "entry_schema": '{http://scap.nist.gov/schema/feed/vulnerability/2.0}entry',
           "summary_schema": '{http://scap.nist.gov/schema/vulnerability/0.4}summary',
           "cve_schema": '{http://scap.nist.gov/schema/vulnerability/0.4}cve-id',
           "vulnerable_software_list_schema": '{http://scap.nist.gov/schema/vulnerability/0.4}vulnerable-software-list',
           "products_schema":'{http://scap.nist.gov/schema/vulnerability/0.4}product',
           "published_datetime_schema":'{http://scap.nist.gov/schema/vulnerability/0.4}published-datetime',
           
           "from_id" : "",
           "email_id": [""],
           "smpt_addr": "",
           "smpt_port": ""
        }
