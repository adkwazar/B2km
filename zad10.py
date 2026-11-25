from urllib.request import urlopen
from lxml import etree

##################
ID = ['??','??','??'] # id sekwencji, wpisz po przecinku, każdy w ' '
##################
for i in ID:
    baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
    query = "db=nucleotide&id="+i+"&format=xml" 
    url = baseurl+query
    f = urlopen(url) 
    resultxml = f.read() 
    xml = etree.XML(resultxml) 
    
    resultelements = xml.xpath("//GBSeq_definition") #co to jest?
    #############################################

    for element in resultelements:
        print(">"+element.text)

    #############################################
    resultelements = xml.xpath("//GBSeq_sequence") #sekwencja
    #############################################

    for element in resultelements:
        print(element.text.upper())