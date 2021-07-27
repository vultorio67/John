import json
from ast import literal_eval
import json
import random


def getWord1(categorie, number, isRandom):
  with open('wordDataBase.json', 'r') as f:
    data = json.load(f)
    #uInfo = literal_eval(data)
    uInfo = data[categorie]
    if isRandom == True:
      uInfo = uInfo[str(random.randint(1,number))]
    else :
      uInfo = uInfo[str(number)]

    return uInfo

def getWord2(categorie, number, isRandom, categorie2):
  with open('wordDataBase.json', 'r') as f:
    data = json.load(f)
    #uInfo = literal_eval(data)
    uInfo = data[categorie]
    uInfo = uInfo[categorie2]
    if isRandom == True:
      uInfo = uInfo[str(random.randint(1,number))]
    else :
      uInfo = uInfo[str(number)]

    return uInfo

def getWord3(categorie, number, isRandom, categorie2, categorie3):
  with open('wordDataBase.json', 'r') as f:
    data = json.load(f)
    #uInfo = literal_eval(data)
    uInfo = data[categorie]
    uInfo = uInfo[categorie2]
    uInfo = uInfo[categorie3]
    if isRandom == True:
      uInfo = uInfo[str(random.randint(1,number))]
    else :
      uInfo = uInfo[str(number)]

    return uInfo

print(str(getWord1('byeWord', 3, True)))