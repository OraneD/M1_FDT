#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:54:42 2023

@author: orane
"""

import os
from pathlib import Path
from xml.etree import ElementTree as et


print(os.getcwd())



with open(Path(os.getcwd() + "/Litterature/url_litterature.txt"), "w") as file : 
    xml = et.parse(os.getcwd() + "/Litterature/litterature_2010_2023.xml")
    root = xml.getroot()
    nb = 0
    for string in root.findall(".//str") :
        if string.attrib == {"name" : "num"} :
           file.write("https://www.theses.fr/" + string.text + ".xml" + "\n")
           nb += 1
        #if nb == 200 :
            #break
