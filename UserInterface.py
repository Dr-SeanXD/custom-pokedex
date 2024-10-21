import csv

result = {"Bug": 1, "Dark": 1, "Dragon": 1, "Electric": 1, "Fairy": 1, "Fighting": 1, "Fire": 1, "Flying": 1, "Ghost": 1, "Grass": 1, "Ground": 1, "Ice": 1, "Normal": 1, "Poison": 1, "Psychic": 1, "Rock": 1, "Steel": 1, "Water": 1}


def Suggestion(Atk, Sp_Atk, Speed):
  '''
  This function uses the embeded variables to calculate the suitable IV training method for each Pokemon. If the attack stat. is higher than the special attack stat., this Pokemon is a physical attacker, so the function will suggest the user to train the attack stat. up. On the other hand, if the Pokemon is a special attacker, the function will suggest the user to train the special attack sstat. up. Also, if the speed of the Pokemon is higher or equal to 70, which is the average speed of all Pokemon, the function will suggest the user to train the Pokemon's speed stat. up. Conversely, if the Pokemon does not have a high speed, the function will suggest the user to train the HP stat. up so the Pokemon can survive from a hit of the opponent's attack and then attack back. This function is made because one Pokemon can only get up to 510 points for stat. boost; therefore, it is vitally important for trainers to train their Pokemon in the best way.
  
  Args:
    Atk (int): This variable stores the Pokemon's physical attack stat.
    
    Sp_Atk (int): This variable stores the Pokemon's special attack stat.
    
    Speed (int): This variable stores the Pokemon's speed stat.
  '''
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


def Calculate(type):
  '''
  This function calculates the effectiveness of the types between the Pokemons. This can be used to check if the moves of the Pokemon is effective or not against the opponent's Pokemon. The embeded variable in this function, "type," is the type of the opponent's Pokemon. The result will be entered into the dictionary initialized above.

  Args:
    type (int): Store the type of the opponent's Pokemon.
  '''
  if (type == "Bug"):
    result["Flying"] *= 2
    result["Fire"] *= 2
    result["Rock"] *= 2
    result["Ground"] *= 0.5
    result["Fighting"] *= 0.5
    result["Grass"] *= 0.5
  elif (type == "Dark"):
    result["Bug"] *= 2
    result["Fighting"] *= 2
    result["Fairy"] *= 2
    result["Ghost"] *= 0.5
    result["Dark"] *= 0.5
    result["Psychic"] *= 0
  elif (type == "Dragon"):
    result["Dragon"] *= 2
    result["Ice"] *= 2
    result["Fairy"] *= 2
    result["Fire"] *= 0.5
    result["Water"] *= 0.5
    result["Grass"] *= 0.5
    result["Electric"] *= 0.5
  elif (type == "Electric"):
    result["Ground"] *= 2
    result["Flying"] *= 0.5
    result["Electric"] *= 0.5
    result["Steel"] *= 0.5
  elif (type == "Fairy"):
    result["Poison"] *= 2
    result["Steel"] *= 2
    result["Bug"] *= 0.5
    result["Fighting"] *= 0.5
    result["Dark"] *= 0.5
    result["Dragon"] *= 0
  elif (type == "Fighting"):
    result["Flying"] *= 2
    result["Psychic"] *= 2
    result["Fairy"] *= 2
    result["Bug"] *= 0.5
    result["Dark"] *= 0.5
    result["Rock"] *= 0.5
  elif (type == "Fire"):
    result["Ground"] *= 2
    result["Rock"] *= 2
    result["Water"] *= 2
    result["Fire"] *= 0.5
    result["Grass"] *= 0.5
    result["Ice"] *= 0.5
    result["Bug"] *= 0.5
    result["Steel"] *= 0.5
    result["Fairy"] *= 0.5
  elif (type == "Flying"):
    result["Electric"] *= 2
    result["Ice"] *= 2
    result["Rock"] *= 2
    result["Bug"] *= 0.5
    result["Fighting"] *= 0.5
    result["Grass"] *= 0.5
    result["Ground"] *= 0
  elif (type == "Ghost"):
    result["Ghost"] *= 2
    result["Dark"] *= 2
    result["Bug"] *= 0.5
    result["Poison"] *= 0.5
    result["Normal"] *= 0
    result["Fighting"] *= 0
  elif (type == "Grass"):
    result["Bug"] *= 2
    result["Fire"] *= 2
    result["Flying"] *= 2
    result["Poison"] *= 2
    result["Ice"] *= 2
    result["Ground"] *= 0.5
    result["Water"] *= 0.5
    result["Electric"] *= 0.5
    result["Grass"] *= 0.5
  elif (type == "Ground"):
    result["Water"] *= 2
    result["Grass"] *= 2
    result["Ice"] *= 2
    result["Poison"] *= 0.5
    result["Rock"] *= 0.5
    result["Electric"] *= 0
  elif (type == "Ice"):
    result["Fighting"] *= 2
    result["Fire"] *= 2
    result["Steel"] *= 2
    result["Rock"] *= 2
    result["Ice"] * 0.5
  elif (type == "Normal"):
    result["Fighting"] *= 2
    result["Ghost"] *= 0
  elif (type == "Poison"):
    result["Ground"] *= 2
    result["Psychic"] *= 2
    result["Bug"] *= 0.5
    result["Poison"] *= 0.5
    result["Grass"] *= 0.5
    result["Fighting"] *= 0.5
    result["Fairy"] *= 0.5
  elif (type == "Psychic"):
    result["Bug"] *= 2
    result["Ghost"] *= 2
    result["Dark"] *= 2
    result["Fighting"] *= 0.5
    result["Psychic"] *= 0.5
  elif (type == "Rock"):
    result["Ground"] *= 2
    result["Water"] *= 2
    result["Grass"] *= 2
    result["Fighting"] *= 2
    result["Steel"] *= 2
    result["Normal"] *= 0.5
    result["Poison"] *= 0.5
    result["Flying"] *= 0.5
    result["Fire"] *= 0.5
  elif (type == "Steel"):
    result["Ground"] *= 2
    result["Fighting"] *= 2
    result["Fire"] *= 2
    result["Normal"] *= 0.5
    result["Bug"] *= 0.5
    result["Flying"] *= 0.5
    result["Grass"] *= 0.5
    result["Ice"] *= 0.5
    result["Rock"] *= 0.5
    result["Psychic"] *= 0.5
    result["Dragon"] *= 0.5
    result["Steel"] *= 0.5
    result["Fairy"] *= 0.5
    result["Poison"] *= 0
  elif (type == "Water"):
    result["Electric"] *= 2
    result["Grass"] *= 2
    result["Fire"] *= 0.5
    result["Water"] *= 0.5
    result["Ice"] *= 0.5
    result["Steel"] *= 0.5


def output(row):
  '''
  This function ouputs the result of the searching mechanics developed in this project.

  Args:
    row (dictionary): Stores the position of the Pokemon in the csv file.
  '''
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

  
def Out_Effective():
  '''
  Prints the type(s) that is/are 2 times effective against the opponent's Pokemon.
  '''
  if (result["Bug"] == 2): print("Bug")
  if (result["Dark"] == 2): print("Dark")
  if (result["Dragon"] == 2): print("Dragon")
  if (result["Electric"] == 2): print("Electric")
  if (result["Fairy"] == 2): print("Fairy")
  if (result["Fighting"] == 2): print("Fighting")
  if (result["Fire"] == 2): print("Fire")
  if (result["Flying"] == 2): print("Flying")
  if (result["Ghost"] == 2): print("Ghost")
  if (result["Grass"] == 2): print("Grass")
  if (result["Ground"] == 2): print("Ground")
  if (result["Ice"] == 2): print("Ice")
  if (result["Normal"] == 2): print("Normal")
  if (result["Poison"] == 2): print("Poison")
  if (result["Psychic"] == 2): print("Psychic")
  if (result["Rock"] == 2): print("Rock")
  if (result["Steel"] == 2): print("Steel")
  if (result["Water"] == 2): print("Water")


def Out_QuadEffective():
  '''
  Prints the type(s) that is/are 4 times effecive against the opponent's Pokemon.
  '''
  if (result["Bug"] > 2): print("Bug")
  if (result["Dark"] > 2): print("Dark")
  if (result["Dragon"] > 2): print("Dragon")
  if (result["Electric"] > 2): print("Electric")
  if (result["Fairy"] > 2): print("Fairy")
  if (result["Fighting"] > 2): print("Fighting")
  if (result["Fire"] > 2): print("Fire")
  if (result["Flying"] > 2): print("Flying")
  if (result["Ghost"] > 2): print("Ghost")
  if (result["Grass"] > 2): print("Grass")
  if (result["Ground"] > 2): print("Ground")
  if (result["Ice"] > 2): print("Ice")
  if (result["Normal"] > 2): print("Normal")
  if (result["Poison"] > 2): print("Poison")
  if (result["Psychic"] > 2): print("Psychic")
  if (result["Rock"] > 2): print("Rock")
  if (result["Steel"] > 2): print("Steel")
  if (result["Water"] > 2): print("Water")

    
def Out_Resist():
  '''
  Prints the type(s) that is/are not effective agaginst the opponent's Pokemon.
  '''
  if (result["Bug"] == 0.5): print ("Bug")
  if (result["Dark"] == 0.5): print("Dark")
  if (result["Dragon"] == 0.5): print("Dragon")
  if (result["Electric"] == 0.5): print("Electric")
  if (result["Fairy"] == 0.5): print("Fairy")
  if (result["Fighting"] == 0.5): print("Fighting")
  if (result["Fire"] == 0.5): print("Fire")
  if (result["Flying"] == 0.5): print("Flying")
  if (result["Ghost"] == 0.5): print("Ghost")
  if (result["Grass"] == 0.5): print("Grass")
  if (result["Ground"] == 0.5): print("Ground")
  if (result["Ice"] == 0.5): print("Ice")
  if (result["Normal"] == 0.5): print("Normal")
  if (result["Poison"] == 0.5): print("Poison")
  if (result["Psychic"] == 0.5): print("Psychic")
  if (result["Rock"] == 0.5): print("Rock")
  if (result["Steel"] == 0.5): print("Steel")
  if (result["Water"] == 0.5): print("Water")
  if (result["Bug"] == 0.25): print ("Bug")
  if (result["Dark"] == 0.25): print("Dark")
  if (result["Dragon"] == 0.25): print("Dragon")
  if (result["Electric"] == 0.25): print("Electric")
  if (result["Fairy"] == 0.25): print("Fairy")
  if (result["Fighting"] == 0.25): print("Fighting")
  if (result["Fire"] == 0.25): print("Fire")
  if (result["Flying"] == 0.25): print("Flying")
  if (result["Ghost"] == 0.25): print("Ghost")
  if (result["Grass"] == 0.25): print("Grass")
  if (result["Ground"] == 0.25): print("Ground")
  if (result["Ice"] == 0.25): print("Ice")
  if (result["Normal"] == 0.25): print("Normal")
  if (result["Poison"] == 0.25): print("Poison")
  if (result["Psychic"] == 0.25): print("Psychic")
  if (result["Rock"] == 0.25): print("Rock")
  if (result["Steel"] == 0.25): print("Steel")
  if (result["Water"] == 0.25): print("Water")

    
def Out_No():
  '''
  Prints the type(s) that won't do any damage to the opponent's Pokemon.
  '''
  if (result["Bug"] == 0): print ("Bug")
  if (result["Dark"] == 0): print("Dark")
  if (result["Dragon"] == 0): print("Dragon")
  if (result["Electric"] == 0): print("Electric")
  if (result["Fairy"] == 0): print("Fairy")
  if (result["Fighting"] == 0): print("Fighting")
  if (result["Fire"] == 0): print("Fire")
  if (result["Flying"] == 0): print("Flying")
  if (result["Ghost"] == 0): print("Ghost")
  if (result["Grass"] == 0): print("Grass")
  if (result["Ground"] == 0): print("Ground")
  if (result["Ice"] == 0): print("Ice")
  if (result["Normal"] == 0): print("Normal")
  if (result["Poison"] == 0): print("Poison")
  if (result["Psychic"] == 0): print("Psychic")
  if (result["Rock"] == 0): print("Rock")
  if (result["Steel"] == 0): print("Steel")
  if (result["Water"] == 0): print("Water")


def OUT():
  '''
  Uses the functions above to print out the result of the "Typings Evaluation" mode.
  '''
  if (Judge("quad_effective")):
    print("\nHere is/are the following type(s) that is/are 4 times effective against the opponent: ")
    Out_QuadEffective()
    nextLine()
  if (Judge("super_effective")): 
    print("\nHere is/are the following type(s) that is/are 2 times effective against the opponent: ")
    Out_Effective()
    nextLine()
  if (Judge("Resist")):
    print('Here is/are the following type(s) that is/are "NOT SUPER EFFECTIVE" against the opponent: ')
    Out_Resist()
    nextLine()
  if (Judge("no_effect")):
    print("Here is/are the types that won't work against the opponent: ")
    Out_No()

def Judge(word):
  '''
  This function is designed to know if there is/are type(s) that is/are 2 times effective, 4 times effective, not effective, or 0 times effective against the opponent Pokemon. The fucntion will return a boolean variable to let the function "OUT" know if it should print out certain sentences.

  Args:
    word (string): To let the function know what should be judged for the function "OUT."
  '''
  if (word == "super_effective"):
    if_weakness = False
    if (result["Bug"] == 2): if_weakness = True
    if (result["Dark"] == 2): if_weakness = True
    if (result["Dragon"] == 2): if_weakness = True
    if (result["Electric"] == 2): if_weakness = True
    if (result["Fairy"] == 2): if_weakness = True
    if (result["Fighting"] == 2): if_weakness = True
    if (result["Fire"] == 2): if_weakness = True
    if (result["Flying"] == 2): if_weakness = True
    if (result["Ghost"] == 2): if_weakness = True
    if (result["Grass"] == 2): if_weakness = True
    if (result["Ground"] == 2): if_weakness = True
    if (result["Ice"] == 2): if_weakness = True
    if (result["Normal"] == 2): if_weakness = True
    if (result["Poison"] == 2): if_weakness = True
    if (result["Psychic"] == 2): if_weakness = True
    if (result["Rock"] == 2): if_weakness = True
    if (result["Steel"] == 2): if_weakness = True
    if (result["Water"] == 2): if_weakness = True
    return if_weakness
  elif (word == "Resist"):
    resist = False
    if (result["Bug"] == 0.5): resist = True
    if (result["Dark"] == 0.5): resist = True
    if (result["Dragon"] == 0.5): resist = True
    if (result["Electric"] == 0.5): resist = True
    if (result["Fairy"] == 0.5): resist = True
    if (result["Fighting"] == 0.5): resist = True
    if (result["Fire"] == 0.5): resist = True
    if (result["Flying"] == 0.5): resist = True
    if (result["Ghost"] == 0.5): resist = True
    if (result["Grass"] == 0.5): resist = True
    if (result["Ground"] == 0.5): resist = True
    if (result["Ice"] == 0.5): resist = True
    if (result["Normal"] == 0.5): resist = True
    if (result["Poison"] == 0.5): resist = True
    if (result["Psychic"] == 0.5): resist = True
    if (result["Rock"] == 0.5): resist = True
    if (result["Steel"] == 0.5): resist = True
    if (result["Water"] == 0.5): resist = True
    if (result["Bug"] == 0.25): resist = True
    if (result["Dark"] == 0.25): resist = True
    if (result["Dragon"] == 0.25): resist = True
    if (result["Electric"] == 0.25): resist = True
    if (result["Fairy"] == 0.25): resist = True
    if (result["Fighting"] == 0.25): resist = True
    if (result["Fire"] == 0.25): resist = True
    if (result["Flying"] == 0.25): resist = True
    if (result["Ghost"] == 0.25): resist = True
    if (result["Grass"] == 0.25): resist = True
    if (result["Ground"] == 0.25): resist = True
    if (result["Ice"] == 0.25): resist = True
    if (result["Normal"] == 0.25): resist = True
    if (result["Poison"] == 0.25): resist = True
    if (result["Psychic"] == 0.25): resist = True
    if (result["Rock"] == 0.25): resist = True
    if (result["Steel"] == 0.25): resist = True
    if (result["Water"] == 0.25): resist = True
    return resist
  elif (word == "no_effect"):
    effect = False
    if (result["Bug"] == 0): effect = True
    if (result["Dark"] == 0): effect = True
    if (result["Dragon"] == 0): effect = True
    if (result["Electric"] == 0): effect = True
    if (result["Fairy"] == 0): effect = True
    if (result["Fighting"] == 0): effect = True
    if (result["Fire"] == 0): effect = True
    if (result["Flying"] == 0): effect = True
    if (result["Ghost"] == 0): effect = True
    if (result["Grass"] == 0): effect = True
    if (result["Ground"] == 0): effect = True
    if (result["Ice"] == 0): effect = True
    if (result["Normal"] == 0): effect = True
    if (result["Poison"] == 0): effect = True
    if (result["Psychic"] == 0): effect = True
    if (result["Rock"] == 0): effect = True
    if (result["Steel"] == 0): effect = True
    if (result["Water"] == 0): effect = True
    return effect
  elif (word == "quad_effective"):
    effective = False
    if (result["Bug"] > 2): effective = True
    if (result["Dark"] > 2): effective = True
    if (result["Dragon"] > 2): effective = True
    if (result["Electric"] > 2): effective = True
    if (result["Fairy"] > 2): effective = True
    if (result["Fighting"] > 2): effective = True
    if (result["Fire"] > 2): effective = True
    if (result["Flying"] > 2): effective = True
    if (result["Ghost"] > 2): effective = True
    if (result["Grass"] > 2): effective = True
    if (result["Ground"] > 2): effective = True
    if (result["Ice"] > 2): effective = True
    if (result["Normal"] > 2): effective = True
    if (result["Poison"] > 2): effective = True
    if (result["Psychic"] > 2): effective = True
    if (result["Rock"] > 2): effective = True
    if (result["Steel"] > 2): effective = True
    if (result["Water"] > 2): effective = True
    return effective


def mode1(Serial, rows):
  '''
  This function is designed to search the Pokemon requested via their serial number (Mode 1).

  Args:
    Serial (int): Let the function knows what serial number should be found.
    rows (dictionary): Let the function search the Pokemon via their serial number using the csv file, which is imported into this project using dictionary.
  '''
  finish = False
  Attack = 0
  Sp_Atk = 0
  Speed = 0
  pokemon = 0
  for row in rows:
    if (Serial in row["ID"]):
      print("\nSerial Number: " + row["ID"])
      print("Pokemon Name: " + row["Name"])
      pokemon = row
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
      Attack = int(row["Attack"])
      Sp_Atk = int(row["Sp.Atk"])
      Speed = int(row["Speed"])
      finish = True
      break
  if (finish == False):
    print("Cannot find this Pokemon")
  else:
    Suggestion(Attack, Sp_Atk, Speed)
def nextLine():
  '''
  This function is designed to enhance the UI sequencing so that each result has an interval of 3 lines.
  '''
  print("\n\n\n")
with open('Pokemon.csv', newline='') as csvfile:
  rows = csv.DictReader(csvfile)
  mode = int(input("Please choose the mode:\n1. Search via serial number\n2. Search via name\n3. Search via pokemon type(s)\n4. Typing Evaluation\nPlease enter the correct number: "))
  print("\n")
  if (mode == 1):
    Serial = input("Please enter the serial number (please add '#' before the serial number): ")
    mode1(Serial, rows)
  if (mode == 2):
    Name = input("Please enter the name: ")
    for row in rows:
      if (Name in row["Name"]):
        output(row)
  if (mode == 3):
    number = int(input("How many typing(s) do you want to use to search for: "))
    print("\n")
    if (number == 1):
      type = input("Please enter the typing (Capitalize the first letter): ")
      print("Here's the result:\n\n")
      check = 0
      for row in rows:
        if (row["Type1"] in type or row["Type2"] in type):
          check = 1
          print(row["ID"] + " " + row["Name"])
      if (check == 0):
        print("N/A No result found...")
    if (number == 2):
      type1 = input("Please enter the first typing (Capitalize the first letter): ")
      type2 = input("Please enter the second typing (Capitalize the first letter): ")
      print("Here's the result\n")
      check = 0
      for row in rows:
        if (type1 in row["Type1"] and type2 in row["Type2"]):
          check = 1
          print(row["ID"] + " " + row["Name"])
        elif (type1 in row["Type2"] and type2 in row["Type1"]):
          check = 1
          print(row["ID"] + " " + row["Name"])
      if (check == 0):
        print("N/A No result found...")
  if (mode == 4):
    type_num = int(input("Please enter the number of types of the opponent: "))
    if (type_num == 1):
      Type = input("\nPlease enter the type of the opponent: ")
      Calculate(Type)
    elif (type_num == 2):
      Type1 = input("\nPlease enter the first type of the opponent: ")
      Calculate(Type1)
      Type2 = input("\nPlease enter the second type of the opponent: ")
      Calculate(Type2)
    OUT()