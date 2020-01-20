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
# @author: Evo Eftimov
#
#############################################################################################################

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


#kerb_ticket=kerb_ticket
fs = pa.hdfs.connect("localhost", user="cloudera")

# hdfs file access modes: rb, wb, ab
# open and write to hdfs file
with fs.open("/user/cloudera/synt/syntdata.csv", 'wb') as f:

    for rowID in range(0, 30):

        # generates labels for Feature Vectors in the form of sequential numbers
        #f.write( (str(rowID) + ' 1:' + str(random.random())  + ' 2:' + str(random.random()) + ' 3:' + str(random.random()) + '\n').encode('UTF-8') )

        # generates labels for Feature Vectors in the form of unique numbers, which are gurateed to be unique through cryptographic means
        #f.write((str(uuid.uuid4().int) + ' 1:' + str(random.random()) + ' 2:' + str(random.random()) + ' 3:' + str(random.random()) + '\n').encode('UTF-8'))

        f.write("0" + " 1:" + str(gauss(1, 0.1)) + " 2:" + str(gauss(5, 0.5)) + " 3:" + str(gauss(9, 1)) + "\n")
        f.write("1" + " 1:" + str(gauss(11, 1)) + " 2:" + str(gauss(3, 0.2)) + " 3:" + str(gauss(9, 1)) + "\n")

fs.close()

