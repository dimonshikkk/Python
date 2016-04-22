import urllib.request
from xml.dom import minidom

url = "http://www.rbc.ru"

webFile = urllib.request.urlopen(url)
data = webFile.read()
	
# Имя файла
FileName = "yandex.xml"

with open(FileName, "wb") as localFile:
    localFile.write(data)

webFile.close()


from xml.dom import minidom


f = parseString('yandex.xml')
