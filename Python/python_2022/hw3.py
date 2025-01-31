import string

f = open("two_cities_ascii.txt")                                                                # I Open the txt file.
f = f.read()                                                                                    
temp = []                                                                                       # I create a temp list.

for i in range(len(f)):
    if f[i] in string.ascii_letters or f[i] in string.whitespace:
        temp += f[i]                                                                            # We use the temp list to keep only letters and space.

f = "".join(temp)

f= f.split()                                                                                    # I split the text according the space.

i=0
j = 0
while(True):                                                                                    # Right here, using my while
    print(i,j, len(f))
    if i!=j:                                                                                    # Im checking if 2 of the words of the file
        if len(f[i])+len(f[j])==20:                                                             # Have 20 letters in total
            f.pop(i)                                                                            # So I Can delete them.
            f.pop(j)
            j = 0
        else:
            j += 1
    else:
        j += 1
    if j >= (len(f)):
        i += 1
        j = 0
    if i >= (len(f)):
        break

max_Lenght = -2                                                                                 # I Find what's the max Length of word in this file.
for i in range(len(f)):
    if max_Lenght < len(f[i]):
        max_Lenght = len(f[i])

lenght = []
for i in range(max_Lenght+1):                                                                   # I make a list named Length so we count how many
    lenght.append(0)                                                                            # Words are of one specific number of letters.

for i in range(len(f)):
    lenght[len(f[i])] += 1

for i in range(max_Lenght):
    print(lenght[i], " words of ", i+1, "letters")
