#take text from voice input and parse it for questions

import spacy
import nltk


nlp = spacy.load("en_core_web_sm")

def is_question(text):
    #tokenize
    doc = nlp(text.lower())
    tokens = [(token.text, token.tag_) for token in doc]
    
    #grammar rules
    question_structures = [
        ('WP', 'VBZ'),  #W's + Verb
        ('WP', 'VBP'),  #W's + Verb plural
        ('WRB', 'VBP'),  #Wh-adverb + Verb
        ('MD', 'PRP'),  #Modal verb + Personal Pronoun
    ]
    
    #check text matching 
    for structure in question_structures:
        if all(tag in [tag for (_, tag) in tokens] for tag in structure):
            return True
    return False

#text = open("output.txt", "r")

text = "who are you"

if is_question(text):
    print("The text is a question.")
else:
    print("The text is not a question.")