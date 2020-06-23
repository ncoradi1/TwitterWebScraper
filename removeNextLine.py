lineNumberList = []
i = 0
lineNumber = 0

file = open("tempFile", 'r')

data = file.readlines()
#for line in file:
#    if line.find("\n\n", 0, len(line)):
#        tempList.append(line)
#        i = i + 1
#        for item in tempList:
#            tempString = item #str(item)
#            for x in tempString:
#                if (x == '\n'):
#                    tempList.remove(item)
#                    #file.write(item)
#                    print(item)

for line in file:
    lineNumber += 1
    if line == '\n':
        #lineNumberList.append(lineNumber)
        
file.close()

file = open("newFile", 'w')

for tempNum in lineNumberList:
    data[tempNum] = 'x'
    file.writelines(data)

#print(lineNumberList)
#print(len(lineNumberList))
file.close()