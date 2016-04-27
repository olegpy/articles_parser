from django.shortcuts import render
import xml.etree.ElementTree as ET
from httplib import BadStatusLine
import urllib2
import urllib
import json


def parser(request):
    data_privat = pars_json(
        'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')

    url_nbu = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    url_privat = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=3"
    # url = "http://export.yandex.ru/weather-ng/forecasts/34300.xml"
    url = "https://www.gismeteo.ru/city/legacy/4368/"
    url2 = "http://informer.gismeteo.ua/xml/33345_1.xml"

    # file = open('export_weather.xml', 'w')
    # file.write(urllib.urlopen(url2).read())
    # file.close()

    try:
        s = urllib2.urlopen(url2)
        contents = s.read()
        file = open('export_weather.xml', 'w')
        file.write(contents)
        file.close()
    # do something with page
    except BadStatusLine:
        print "could not fetch %s" % url2

    # tree = ET.parse('export_weather.xml')
    # print tree.getroot()
    # root = tree.getroot()

    # for r in root.iter('fact'):
    #     print r
    # lists.append(r.attrib)

    # print root

    nbu_xml = pars_xml(url_nbu, 'export_nbu.xml')
    nbu_privat = pars_xml(url_privat, 'export_nbu.xml')

    return render(request, 'parser.html', {'data_privat': data_privat,
                                           'export_nbu_xml': nbu_xml,
                                           'export_privat_xml': nbu_privat})


def pars_json(url):
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data


def pars_xml(url, files):
    s = urllib2.urlopen(url)
    contents = s.read()
    file = open(files, 'w')
    file.write(contents)
    file.close()

    tree = ET.parse(files)
    root = tree.getroot()

    lists = []
    for r in root.iter('exchangerate'):
        lists.append(r.attrib)

    return lists
