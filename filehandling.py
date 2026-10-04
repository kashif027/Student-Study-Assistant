file = open("study.txt", "w")

file.write("Dsa \n")
file.write("python \n")
file.write(" cyber law \n")

file.close()

file = open("study.txt" , "r")
data = file.read()
print(data)
file.close()

file = open("study.txt", "a")
file.write("javascript \n")
file.close()