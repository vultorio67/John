import json

def nature(sentence):
    words = sentence.split()
    print(words)
    for z in range(len(words)):
        word =words[z]

        with open('words/verbs-conjugations.json', 'r') as f:
            data = json.load(f)
            # data = data[1]
            # uInfo = literal_eval(data)
            uInfo = data

            for x in range(len(uInfo)):
                verbeList = uInfo[x]['indicative']['present']
                #print(verbeList)
                for i in range(len(verbeList)):
                    # print(verbeList[i])
                    #print(verbeList[i])
                    if verbeList[i] == word:
                        print("verbe: "+verbeList[i])
                        break
        with open('words/personal_nouns.json', 'r') as f:
            data = json.load(f)
            # data = data[1]
            # uInfo = literal_eval(data)
            uInfo = data

            for x in range(len(uInfo)):
                nounsList = uInfo['personalNouns'][x]
                #print(nounsList)
                for i in range(len(nounsList)):
                    # print(nounsList[i])
                    print(nounsList[i])
                    if nounsList[i] == word:
                        print("verbe: "+nounsList[i])
                        break

nature("hello how have you ")