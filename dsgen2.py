from random import seed
from random import random

seed(1)

file = open("/opt/data/testfile.txt", "w")

for x in range(10):

    file.write(str(x) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

file.close()