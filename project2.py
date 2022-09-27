import os
import socket
from collections import Counter

path = "home/data"

f = open("home/output/result.txt", "w+")

f.write("List of all the text files:\n")
for i in os.listdir(path):
    if i.endswith('.txt'):
        f.write(i)
        f.write("\n")

print("")
f.write("\n")

file1 = open("home/data/IF.txt", "rt")
data1 = file1.read()
words1 = data1.split()

f.write("Number of words in IF.txt: ")
f.write(str(len(words1)))
f.write("\n")

file2 = open("home/data/Limerick-3.txt", "rt")
data2 = file2.read()
words2 = data2.split()

f.write("Number of words in Limerick-3.txt ")
f.write(str(len(words2)))
f.write("\n")

totalwords = len(words1) + len(words2)

f.write("Total number of words in two files: ")
f.write(str(totalwords))
f.write("\n")

count_file1 = Counter(words1)

top3_words = count_file1.most_common(3)
f.write("Top 3 words in the machine")
f.write(str(top3_words))
f.write("\n")

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
f.write("The IP address of my machine is ")
f.write(str(IPAddress))

f.close()

f = open("home/output/result.txt", "r")
print(f.read())
