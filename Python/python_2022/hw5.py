import string
from collections import Counter

f = open("two_cities_ascii.txt")                                                                # I Open the txt file.
f = f.read()                                                                                    
temp = []                                                                                       # I create a temp list.

for i in range(len(f)):                                                                         
    if f[i] in string.ascii_lowercase or f[i] in string.whitespace:                             # We need the lowercases and the whitespaces.
        temp += f[i]                                                                            
    elif f[i] in string.ascii_uppercase:                                                        # If we find an uppercase letter, we replace it.
        temp += f[i].lower()

f = "".join(temp)

f = f.split()                                                                                    # I split the text according the space.

counterWords = Counter(f)

print(counterWords.most_common(10))                                                             # I Get the 10 most common words :D


Two_Letters = []                                                                                # I Create a list that I will fill with the first 2 letters of each word.

for i in range(len(f)):
    Two_Letters = ""

temp_2 = []
for words in f:
    temp_2 += (words[:2]+" ")                                                                   # Right now I am using an temp list, that i am filling it with the 2 first letters and the space
                                                                                                # So it's easier to split it on the Two_Letters list

Two_Letters = "".join(temp_2)

Two_Letters = Two_Letters.split()   

counterTwoLetters = Counter(Two_Letters)                                                        # I'm using a counter to check whats the most 3 Letters start

print(counterTwoLetters.most_common(3))                                                         # I am printing the 3 most common ones :D


                                                                                                ##################################
                                                                                                #         On the same way        #
                                                                                                #   I am working with 3 letters  #
                                                                                                ##################################


Three_Letters = []

for i in range(len(f)):
    Three_Letters = ""

temp_3 = []

for words in f:
    temp_3 += (words[:3]+" ")

Three_Letters = "".join(temp_3)

Three_Letters = Three_Letters.split()

counterThreeLetters = Counter(Three_Letters)
                                                                                                ##################################
print(counterThreeLetters.most_common(3))                                                       #     The only "bug" I found     #
                                                                                                # was the fact I am not checking #
                                                                                                # if the words are at least 2/3  #
                                                                                                #         letters long           #
                                                                                                ##################################
