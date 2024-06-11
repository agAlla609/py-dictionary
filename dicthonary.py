import json
import difflib
from difflib import get_close_matches
data= json.load(open("data.json"))
def translate(word):
    word= word.lower()
    while True:
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys()))>0:
            yn=input("Did you mean %s instead? Enter Y if yes and N if no: " %get_close_matches(word, data.keys())[0])
            if yn=="Y":
                 return data[get_close_matches(word,data.keys())]
            elif yn== "N":
                return "The word does not exist. Please double check "
            else:
                return " We did not understand you query"
    
            


        else: 
            return "The word does not exist. Please double check "

word= input("Enter the word: ")
output= translate(word)

if type(output) ==list:
    for item in output:
         print(item)
        
else:
    print(output)
   