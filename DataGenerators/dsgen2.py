from random import seed
from random import *
import uuid
#############################################################################################################
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning
# while emulating specific and realistic Patterns in the data, which can then ensure realistic function and
# performnance testing of Data Science workloads
#
# @author: Evo Eftimov
#
#############################################################################################################

# Note: if there is further demand, the program can be enhanced further to support configurablke number of Features
# and ranges for them

seed(1)

file = open("/root/PycharmProjects/ptp/Data/regression-2.txt", "w")

i =1
a = 2
b = 4
c = 5
d = 7

mlType = "regression"

#for x in range(11, 100): (do on a seperate thread or process / shell for the next segment)
for x in range(100):

    # generates labels for Feature Vectors in the form of sequential numbers
    #file.write(str(x) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

    # generates labels for Feature Vectors in the form of unique numbers, which are gurateed to be unique through cryptographic means
    #file.write(str(str(uuid.uuid4().int)) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

    if (mlType.lower() == "classification"):

        file.write("0" + " 1:" + str(gauss(1,0.1)) + " 2:" + str(gauss(5,0.5)) + " 3:" + str(gauss(9,1)) + " 4:" + str(gauss(21,2)) + "\n")
        file.write("1" + " 1:" + str(gauss(11, 1)) + " 2:" + str(gauss(3, 0.2)) + " 3:" + str(gauss(9, 1)) + " 4:" + str(gauss(17, 0.2)) + "\n")
        file.write("3" + " 1:" + str(gauss(11, 1)) + " 2:" + str(gauss(7, 0.2)) + " 3:" + str(gauss(44, 1)) + " 4:" + str(gauss(33, 1)) + "\n")

    if (mlType.lower() == "regression"):

        x1 = float("{0:.2f}".format(uniform(1,3)))
        x2 = float("{0:.2f}".format(uniform(5, 8)))
        x3 = float("{0:.2f}".format(uniform(12, 18)))
        x4 = float("{0:.2f}".format(uniform(1, 6)))
        noise = float("{0:.2f}".format(gauss(1, 0.1)))
        y = i+ a*x1 + b*x2 + c*x3 + d*x4 + noise
        y = float("{0:.2f}".format(y))

        file.write(str(y) + " 1:" + str(x1) + " 2:" + str(x2) + " 3:" + str(x3) + " 4:" + str(x4) + "\n")


file.close()