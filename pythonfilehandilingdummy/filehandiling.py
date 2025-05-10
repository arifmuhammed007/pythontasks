#1)Write a Python program to read an entire text file
with open("mydata.txt","r") as file:
    content = file.read()
    print(content)

#2). Write a Python program to read first n lines of a file.

n = 3
with open("linereading.txt","r") as file:
    for i in range(n):
        line = file.readline()
        print(line,end='')

#3)3. Write a Python program to append text to a file and display the text.

with open("linereading.txt",'a') as file:
    file.write("\n line 4: this line was added by python")

with open("linereading.txt",'r') as file:
    print(file.read())    

#4. Write a Python program to read last n lines of a file.

with open('linereading.txt','r') as file:
    lines = file.readlines()
    last_n_line = lines[-n:]

for line in last_n_line:
    print(line,end='')



    
