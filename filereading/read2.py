n = int(input("how many characters to preview?"))
file = open("read.txt", "r")
print(fille.read(n))
file.close()
print()

file = openn("read.txt", "r")
lines = file.readLines()
file.close()
print("total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("skip lines starting with: ")
file = open("read.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

file = open("read.txt", "r")
lines = file.readLines()
file.close()
out = open("read.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close
print("odd lines saved to read.txt")