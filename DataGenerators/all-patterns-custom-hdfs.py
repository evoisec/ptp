import pyarrow as pa
import uuid
from random import *

#############################################################################################################
# Generates synthetic data in the standard LIBSVM data format specifically intended for Machine Learning
# while emulating specific and realistic Patterns in the data, which can then ensure realistic function and
# performnance testing of Data Science workloads
# Writes the syntehtic dataset to HDFS and doesnt suffer from RAM constraints like the
# Scikit-learn equivalent since it generates nd writes the dataset one feature vector at a time. Hence it can generate
# Data Scinece datasets of any size .....
#
# Note - even though this program uses HDFS to write its output data, it is NOT a Spark Job. It is a standalone process
# which can be executed on any machine which has network connectivity with HDFS cluster. It can also be executed on multiple
# threads, as each is given a seperate range of Feature Vectors to generate
#
# @author: Evo Eftimov
#
#############################################################################################################

# Note: if there is further demand, the program can be enhanced further to support configurablke number of Features
# and ranges for them


#Connect to an HDFS cluster. All parameters are optional and should
#only be set if the defaults need to be overridden.

#Authentication should be automatic if the HDFS cluster uses Kerberos.
#However, if a username is specified, then the ticket cache will likely
#be required.

#Parameters
#----------
#host : NameNode. Set to "default" for fs.defaultFS from core-site.xml.
#port : NameNode's port. Set to 0 for default or logical (HA) nodes.
#user : Username when connecting to HDFS; None implies login user.
#kerb_ticket : Path to Kerberos ticket cache.
#driver : {'libhdfs', 'libhdfs3'}, default 'libhdfs'
#Connect using libhdfs (JNI-based) or libhdfs3 (3rd-party C++
#library from Apache HAWQ (incubating) )
#extra_conf : dict, default None
#extra Key/Value pairs for config; Will override any
#hdfs-site.xml properties


Config = {}

f = open('all-patterns-custom-hdfs.cfg', 'r')
line = f.readline()
while (line != ""):
    line = line.rstrip()
    x = line.split('=')
    print(x[0])
    print(x[1])
    Config[x[0]] = x[1]
    line = f.readline()

file = Config['file']

i = int(Config['i'])
a = int(Config['a'])
b = int(Config['b'])
c = int(Config['c'])
d = int(Config['d'])

mlType = Config['ml.type']

#note, in Python 3, integers have unlimited precision
range1 = int(Config['range1'])
range2 = int(Config['range2'])

hdfsHost = Config['hdfs.hostname']
user = Config['user']

#kerb_ticket=kerb_ticket
fs = pa.hdfs.connect(hdfsHost, user=user)

# hdfs file access modes: rb, wb, ab
# open and write to hdfs file
with fs.open(file, 'wb') as f:

    for rowID in range(range1, range2):

        # generates labels for Feature Vectors in the form of sequential numbers
        #f.write( (str(rowID) + ' 1:' + str(random.random())  + ' 2:' + str(random.random()) + ' 3:' + str(random.random()) + '\n').encode('UTF-8') )

        # generates labels for Feature Vectors in the form of unique numbers, which are gurateed to be unique through cryptographic means
        #f.write((str(uuid.uuid4().int) + ' 1:' + str(random.random()) + ' 2:' + str(random.random()) + ' 3:' + str(random.random()) + '\n').encode('UTF-8'))

        if (mlType.lower() == "classification"):

            f.write( ( "0" + " 1:" + str(gauss(1, 0.1)) + " 2:" + str(gauss(5, 0.5)) + " 3:" + str(gauss(9, 1)) + " 4:" + str(gauss(21, 2)) + "\n").encode('UTF-8') )
            f.write( ( "1" + " 1:" + str(gauss(11, 1)) + " 2:" + str(gauss(3, 0.2)) + " 3:" + str(gauss(9, 1)) + " 4:" + str(gauss(17, 0.2)) + "\n").encode('UTF-8') )
            f.write( ( "3" + " 1:" + str(gauss(11, 1)) + " 2:" + str(gauss(7, 0.2)) + " 3:" + str(gauss(44, 1)) + " 4:" + str(gauss(33, 1)) + "\n").encode('UTF-8') )

        if (mlType.lower() == "regression"):

            x1 = float("{0:.2f}".format(uniform(1, 3)))
            x2 = float("{0:.2f}".format(uniform(5, 8)))
            x3 = float("{0:.2f}".format(uniform(12, 18)))
            x4 = float("{0:.2f}".format(uniform(1, 6)))
            noise = float("{0:.2f}".format(gauss(1, 0.1)))
            y = i + a * x1 + b * x2 + c * x3 + d * x4 + noise
            y = float("{0:.2f}".format(y))

            f.write( ( str(y) + " 1:" + str(x1) + " 2:" + str(x2) + " 3:" + str(x3) + " 4:" + str(x4) + "\n").encode('UTF-8') )

fs.close()

