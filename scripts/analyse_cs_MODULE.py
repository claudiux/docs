#!/usr/bin/env python3
# This script gets the tab names present in all cs_MODULE.py of Cinnamon.
# Then, it creates a distionnary named TAB as this one:
#TABS = {
#
# "accessibility":  {"visual": 0, "keyboard": 1, "typing": 2, "mouse": 3},
# "applets":  {"installed": 0, "more": 1},
# "backgrounds":  {"images": 0, "settings": 1},
# "default":  {"preferred": 0, "removable": 1},
# "desklets":   {"installed": 0, "more": 1, "general": 2},
# "effects":  {"effects": 0, "customize": 1},
# "extensions":   {"installed": 0, "more": 1},
# "keyboard":   {"typing": 0, "shortcuts": 1, "layouts": 2},
# "mouse":  {"mouse": 0, "touchpad": 1},
# "power":  {"power": 0, "batteries": 1, "brightness": 2},
# "screensaver":  {"settings": 0, "customize": 1},
# "sound":  {"output": 0, "input": 1, "sounds": 2, "applications": 3, "settings": 4},
# "themes":   {"themes": 0, "download": 1, "options": 2},
# "windows":  {"titlebar": 0, "behavior": 1, "alttab": 2},
# "workspaces":   {"osd": 0, "settings": 1}
#
#}

from os import popen
from os.path import *
from time import sleep

popen("cd /usr/share/cinnamon/cinnamon-settings/modules/ ; /usr/bin/ag add_titled . > ~/cs_titles.txt")
sleep(3)
home_path = expanduser("~")
f = open("%s/cs_titles.txt" % home_path, 'r')
lignes2 = f.readlines()
lignes = []
f.close()

for i in range(len(lignes2)):
  ligne = lignes2[i].strip()
  if ligne != "":
    morceaux = ligne.split(":")
    num = morceaux[1]
    if len(num) == 2:
      l = list(ligne)
      l.insert(ligne.index(":")+1, " ")
      ligne = "".join(l)
    lignes.append(ligne)

lignes.sort()
lignes.reverse()
module=""
i = 0
paires = []
chaine = ""
chaine2 = ""
_if = "\t\t\tif"
while lignes != []:
  ligne = lignes.pop().strip()
  if ligne != "":
    l_module = ligne.split(":")[0][3:-3]
    #print(l_module)
    if l_module != module:
      cles = []
      if module != "":
        chaine += "\n\t\t\t\ttabs_literal = {%s}" % ", ".join(paires)
        chaine2 += "\t{%s},\n" % ", ".join(paires)
        print(chaine)
      module = l_module
      chaine = """%s arg1 == "%s": """ % (_if, module)
      chaine2 += """\t"%s": """ % module
      _if = "\t\t\telif"
      i = -1
      paires = []
    cle = ligne.split(',')[1].replace("'", '"')
    if not cle in cles:
      cles.append(cle)
      i += 1
      paires.append("""%s: %i""" % (cle.strip(), i))
chaine += "\n\t\t\t\ttabs_literal = {%s}" % ", ".join(paires)
chaine2 += "\t{%s}\n" % ", ".join(paires)
#print(chaine)
print("TABS = {\n")
print(chaine2)
print("}\n")
