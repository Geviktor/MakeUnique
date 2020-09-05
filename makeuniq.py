import argparse

parser = argparse.ArgumentParser(description="Clears words found more than once in the file and sort alphabetically.")
parser.add_argument("inputfile", help="Input file.")
parser.add_argument("outputfile", help="The name of the file to be created as output.")
args = parser.parse_args()


words = set()
inputfile = args.inputfile
outputfile = args.outputfile

f = open(inputfile,"r")
oldcount = 0

while True:
    line = f.readline()
    if not line:
        break
    elif line == "\n":
        continue
    else:
        oldcount += 1
        words.add(line)
    
words = sorted(words)
newcount = 0
uniqf = open(outputfile,"w")
for word in words:
    uniqf.write(word)
    newcount += 1

uniqf.close()
print(f"Old row count: {oldcount}\nNew row count: {newcount}")
