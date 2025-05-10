#5. Write a Python program to read a file line by line and store it into a list.

with open("sampletext.txt",'r') as file:
    lines = file.readlines()

print(lines)    

# 6.Write a python program to find the longest word in a text file

with open("sampletext.txt",'r') as file:
    word = file.read().split()

longestword = max(word,key = len)    
print("The longest word is:",longestword)

#7)Write a Python program to count the number of lines in a text file

with open("sampletext.txt","r") as file:
    line = file.readlines()
    line_count = len(line)

    print("Number of line:",line_count)
    print("\n")

#8). Write a Python program to count the frequency of words in a file

from collections import Counter
import string

with open("Sampledata2.txt","r") as file:
    text = file.read().lower()

for p in string.punctuation:
    text = text.replace(p,"")   

word = text.split()    
word_freq = Counter(word)

for word,count in word_freq.items():
    print(f"{word}:{count}\n")

#9)Write a Python program to copy the contents of a file to another file .

with open("sampledata2.txt",'r') as source_file:
    content = source_file.read()

with open("copy.file.txt",'w') as target_file:
    target_file.write(content)

print("File copyed successfully\n")  

#10. Write a Python program to combine each line from first file with the corresponding line in second file.

with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    for line1,line2 in zip(file1,file2):
        compined_line = line1.strip()+ " " + line2.strip()
        print(compined_line)

#11. Write a Python program that takes a text file as input and returns the numberof words of a given text file.
#Note: Some words can be separated by a comma with no space.

with open("textdemo.txt","r") as file:
    text = file.read().lower()

for p in string.punctuation:

    if p != ",":
        text = text.replace(p, " ")
text = text.replace(",", " ")

words = text.split()
word_count = len(words)

print("Total number of words:", word_count)

