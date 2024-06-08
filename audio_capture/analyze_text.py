#take text from voice input and parse it for questions

import nltk
import time
import re
import os

def erase_file():
    with open("./txt/q_output.txt", "w") as f:
        pass

def is_question(text):
    #tokenize (words)
    tokens = nltk.word_tokenize(text.lower())
    pos_tags = nltk.pos_tag(tokens)
    
    #grammar rules
    question_structures = [
        ('WP', 'VBZ'),  #W's + Verb
        ('WP', 'VBP'),  #W's + Verb plural
        ('WRB', 'VBP'),  #Wh-adverb + Verb
        ('MD', 'PRP'),  #Modal verb + Personal Pronoun
    ]
    
    #check if matches common format
    for structure in question_structures:
        if all(tag in [tag for (word, tag) in pos_tags] for tag in structure):
            return True

    # less conventional
    patterns = [
        r"\btell me about\b",
        r"\bexplain\b",
        r"\bhow do\b",
        r"\bhow to\b",
        r"\bcan you\b",
        r"\bcould you\b",
        r"\bwhat is\b",
        r"\bwhat are\b",
        r"\bstate\b",
        r"\did you\b",
        r"\do you\b"
    ]

    #combining and checking against it
    combined_pattern = re.compile('|'.join(patterns))

    if combined_pattern.search(text.lower()):
        return True
    
    return False

def watch_file(filename, output_filename):
    #current position within file (line)
    current_position = 0

    #last time modified
    last_mod_time = os.path.getmtime(filename)

    while True:
        current_mod_time = os.path.getmtime(filename)

        if current_mod_time != last_mod_time:
            #has been modified
            last_mod_time = current_mod_time
            time.sleep(1)  #wait -> no new write between time

            #check if still not written to
            if current_mod_time == os.path.getmtime(filename):
                with open(filename, 'r') as file, open(output_filename, 'a') as output_file:
                    #last read position
                    file.seek(current_position)
                    
                    #read lines following this
                    lines = file.readlines()
                    
                    #update position
                    current_position = file.tell()

                    for line in lines:
                        line = line.strip()
                        if is_question(line):
                            output_file.write(line)
                            output_file.write("\n")
                            
#erase previous content                            
erase_file()

#watch file start
watch_file('./txt/output.txt', './txt/q_output.txt')