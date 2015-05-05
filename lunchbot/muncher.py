# -*- coding: utf-8 -*-

import json
import time
import locale
import urllib

locale.setlocale(locale.LC_TIME, "sv_SE.UTF-8") # swedish


def get_lunch():
    data = json.load(
        urllib.urlopen("https://www.kimonolabs.com/api/arok4o9c?apikey=TzkHfvc4qEcs05HwQxP37ouQhSVbrOh7"))
    lunch_list = []
    for item in data['results']['collection1']:
        lunch_list.append(item['property1'].encode('utf-8'))
    for item in zip(*[iter(lunch_list)]*5):
        if time.strftime('%A') in item[0].lower():
            return '{0}\n{1}\n{2}\n{3}\n{4}'.format(item[0], item[1], item[2], item[3], item[4])