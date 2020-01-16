from random import seed
from random import random
import uuid

# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning

seed(1)

file = open("/opt/data/testfile.txt", "w")

#for x in range(11, 100): (do on a seperate thread or process / shell for the next segment)
for x in range(100):

    #file.write(str(x) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

    file.write(str(str(uuid.uuid4().int)) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

file.close()