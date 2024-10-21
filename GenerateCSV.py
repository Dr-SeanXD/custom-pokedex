import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

HI = requests.get("https://wiki.52poke.com" + link)
HI.encoding = "utf-8"
doup = BeautifulSoup(HI.text, "html.parser")
body = doup.find('body')
td = body.find_all("div" , class_= 'mw-parser-output')

pokemons = []

pokemon = {"ID": "", 'Type1':"" , "Type2": "", 'Name':"" , "HP": 0, "Attack": 0, "Defense": 0, "Sp.Atk": 0, "Sp.Def": 0, "Speed": 0, "Total.Stat": 0}

for i in td:
  b = i.find_all("th")
  for a in b:
    if (a != None): text = a.text
    if ("#" in text):
      print(text)
      pokemon["ID"] = text
      break
  type = doup.find_all('span' , class_ = "type-box-9-text")
  if (len(type) == 2):
    pokemon["Type1"] = type_convert(type[0].text)
    pokemon["Type2"] = "-"
    print(pokemon["Type1"])
  else:
    for i in type:
      pokemon["Type1"] = type_convert(type[0].text)
      pokemon["Type2"] = type_convert(type[1].text)
      print(pokemon["Type1"]) 
      print(pokemon["Type2"])
      break
  Name = doup.find_all("td", class_ = "bgwhite")
  g = 0
  for i in Name:
    s = i.text.split(' ')
    for j in s:
      if g == 4 :
        print (j)
        pokemon['Name'] = j
        g += 1
      g += 1

HP = doup.find("tr", class_ = "bgl-HP")
pokemon["HP"] = HP.text.split('\n')[1].split("：")[-1]
Attack = doup.find("tr", class_ = "bgl-攻击")
pokemon["Attack"] = Attack.text.split("\n")[1].split("：")[-1]
Defense = doup.find("tr", class_ = "bgl-防御")
pokemon["Defense"] = Defense.text.split("\n")[1].split("：")[-1]
Sp_Atk = doup.find("tr", class_ = "bgl-特攻")
pokemon["Sp.Atk"] = Sp_Atk.text.split("\n")[1].split("：")[-1]
Sp_Def = doup.find("tr", class_ = "bgl-特防")
pokemon["Sp.Def"] = Sp_Def.text.split("\n")[1].split("：")[-1]
Speed = doup.find("tr", class_ = "bgl-速度")
pokemon["Speed"] = Speed.text.split("\n")[1].split("：")[-1]
pokemon["Total.Stat"] = int(pokemon["HP"]) + int(pokemon["Attack"]) +   int(pokemon["Defense"]) + int(pokemon["Sp.Atk"]) + int(pokemon["Sp.Def"]) + int(pokemon["Speed"])

pokemons.append(pokemon)




pokemons = csv.DictReader(csvfile)
type = input("Please enter the typing (Capitalize the first letter): ")
print("Here's the result:\n\n")
check = 0
for pokemon in pokemons:
  if (pokemon["Type1"] in type or pokemon["Type2"] in type):
    check = 1
  print(pokemon["ID"] + " " + pokemon["Name"])


def mode1(Serial, pokemons):
  finish = False
  Attack = 0
  Sp_Atk = 0
  Speed = 0
  for pokemon in pokemons:
    if (Serial in pokemon["ID"]):
      print("\nSerial Number: " + pokemon["ID"])
      print("Pokemon Name: " + pokemon["Name"])
      if(pokemon["Type1"] == pokemon["Type2"]):
        print("Type: " + pokemon["Type1"])
      elif (pokemon["Type2"] == "-"):
        print("Type: " + pokemon["Type1"])
      else:
        print("Types: " + pokemon["Type1"] + " and " + pokemon["Type2"])
      print("\nSpecies Strength:")
      print("HP: " + pokemon["HP"])
      print("Attack: " + pokemon["Attack"])
      print("Defense: " + pokemon["Defense"])
      print("Special Attack: " + pokemon["Sp.Atk"])
      print("Special Defense: " + pokemon["Sp.Def"])
      print("Speed: " + pokemon["Speed"])
      print("Total: " + pokemon["Total.Stat"])
      Attack = int(pokemon["Attack"])
      Sp_Atk = int(pokemon["Sp.Atk"])
      Speed = int(pokemon["Speed"])
      finish = True
  if (finish == False):
    print("Cannot find this Pokemon")
  else:
    Suggestion(Attack, Sp_Atk, Speed)


def Suggestion(Atk, Sp_Atk, Speed , pokemon = {}):
  for k in pokemon:
    print(k + ':' + pokemon[k])
  if (Atk > Sp_Atk):
    if (Speed >= 70):
      print ("IV Suggestion: Attack 252, Speed 252, HP 6")
    else:
      print ("IV Suggestion: HP 252, Attack 252, Speed 6")
  elif (Atk < Sp_Atk):
    if (Speed >= 70):
      print ("IV Suggestion: Special Attack 252, Speed 252, HP 6")
    else:
      print ("IV Suggestion: HP 252, Special Attack 252, Speed 6")
  else:
    print("IV Suggestions: This pokemon can either be a physical attack or a special attacker, and it is faster than most of the pokemon")


def output(row):
  print("\nSerial Number: " + row["ID"])
  print("Pokemon Name: " + row["Name"])
  if (row["Type1"] == row["Type2"]):
    print("Type: " + row["Type1"])
  elif (row["Type2"] == "-"):
    print("Type: " + row["Type1"])
  else:
    print("Types: " + row["Type1"] + " and " + row["Type2"])
  print("\nSpecies Strength:")
  print("HP: " + row["HP"])
  print("Attack: " + row["Attack"])
  print("Defense: " + row["Defense"])
  print("Special Attack: " + row["Sp.Atk"])
  print("Special Defense: " + row["Sp.Def"])
  print("Speed: " + row["Speed"])
  print("Total: " + row["Total.Stat"])
  Suggestion(int(row["Attack"]), int(row["Sp.Atk"]), int(row["Speed"]))