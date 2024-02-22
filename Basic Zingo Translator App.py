#Basic Translator: going to take a string (phrase or a word) and translate it into a different language.

#Siris Language: vowel lingo. zingo
#vowels -> z
#---------------
#dog -> dzg
#cat -> czt

#Define a translate function:

def translate(phrase):                #we want to take the phrase that we want to translate:
    translation = ""            #we haven't defined the input phrase quite yet, so we'll assign it to nothing for now
    for each_letter in phrase:
        if each_letter.lower() in "aeiou":   #in Python, you can check if a certain element is inside something else. if each letter is a vowel
            if each_letter.isupper():       #Yes you MUST use () after the isupper and lower functions built in. they wont work otherwise
                translation = translation + "Z"   #we are going to REPLACE it with a 'Z' instead!
            else:
                translation = translation + "z"   #SYNTAX REALLY MATTERS HERE. LOOK AT THE FULLLL VERTICAL LINE. That completes it.

        else:
            translation = translation + each_letter   #otherwise, we will keep it with it's original letter intact
    return translation      #the return statement MUST line up with the for loop you want to return
                            #and we will RETURN the outcome of the now updated 'translation' function
print(translate(input("Please enter a phrase: ")))

#please enter a phrase: My head now hurts from this thing
#My hzzd nzw hzrts frzm thzs thzng









