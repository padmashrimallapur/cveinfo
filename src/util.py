import urllib2
import zipfile


def download_file(url, filename):
    xml_zip = urllib2.urlopen(url)
    with open(filename, "wb") as writeFile:
        writeFile.write(xml_zip.read())

    xml_zip.close()


def unzip(filename):
    zip_file = zipfile.ZipFile(filename)
    zip_file.extractall(".")
    zip_file.close()
