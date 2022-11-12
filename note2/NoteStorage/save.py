# sample
body = ["Hi, this is a test! "
        "Testing new line."]
# writing all the lines to a text file
outputFile = open("outputFile.txt", "w")
for line in body:
    outputFile.write(line)
    outputFile.write("\n")
outputFile.close()

# reading all the lines from a text tile
body = ""
readFile = open("outputFile.txt", "r")
for line in readFile:
    print(line)
    body = body + "" + line + " "
readFile.close()

print("Body text: " + body)
