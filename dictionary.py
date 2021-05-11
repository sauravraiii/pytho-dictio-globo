import os
import time
import pandas
from difflib import get_close_matches
import json

data = json.load(open("C:\\Users\\Admin\\PycharmProjects\\firstproj\\data.json")) # importing json data file with json module and storing it in var 'data'
while True: #continous and neverending loop
    def translate(w, false="Please enter a word"): # function 'translate' to accept word as 'w'
        if w in data:
             return data[w] #If w is stored in data return the value of w

        elif w == "" :
            return false #if nothing is entered return false confirmation
        elif w == " " :
            return "%s excluding space" %false # false confirmation with space
        elif w.isupper(): # if w is uppercase
            word= w.lower() # convert word to lowercase and store it in variable word
            return data[word]
        elif w.istitle(): # if w is a title
            word= w.lower() # convert w to lowercase and store it in word and then, return the 'word' from data file
            return data[word]
        elif len(get_close_matches(w,data.keys())) > 0: # condition to check if the length of w is > 0
            close_match = get_close_matches(w, data.keys())[0] # putting value of getting close matches to help us
            confirmation_user = input("Did you mean %s instead? Enter Y or N: " % close_match)
            if confirmation_user == "Y": # if confirmation is Yes
                return data[close_match]
            else:
                return "There exists no such word in our database."