import requests
import json
import re
def formatText(output):
    regex = r"(<li style=\"list-style:decimal\">\n.*)|(<b>[a-zA-Z]+)"
    output = re.findall(regex,test.text, re.MULTILINE)

    outputString = ""

    for item in output:
        if item[0] != '':
            outputString = outputString + item[0]
        else:
            outputString = outputString + item[1]
        

    #remove html tags
    regex = r"<[a-zA-Z]>" #this first so we dont remove labels
    outputString = re.sub(regex, "", outputString)
    regex = r"<?.em>"
    outputString = re.sub(regex, "", outputString)
    regex = r"<.*>"
    outputString = re.sub(regex, "", outputString)

    return outputString


#test input
testString = "We will test some words."
#sanitize the string
regex = r"[^a-zA-Z ]"
testString = re.sub(regex, "", testString)

for word in testString.split():
    test = requests.get('https://googledictionary.freecollocation.com/meaning?word=' + word)
    print("============", word, "============")
    print(formatText(test))


