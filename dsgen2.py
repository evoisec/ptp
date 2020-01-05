file = open("/opt/data/testfile.txt", "w")

for x in range(10):

    file.write(str(x) + " 1:0.0 2:0.0 3:0.0\n")

file.close()