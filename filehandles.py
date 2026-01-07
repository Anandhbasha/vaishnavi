# read
# file = open("new.txt",'r')
# print(file.read())
# file.close()

# readline
# newLine = open("new.txt",'r')
# print(newLine.readline())
# print(newLine.readlines())

# write
# wri = open("new.txt",'w')
# wri.write("This new Word")
# wri.writelines(["This new Word\n","This second line"])

# append
# append = open("new.txt",'a')
# append.write("\n This last line")

with open("new.txt",'r') as f:
    print(f.read())
