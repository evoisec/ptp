import pyarrow as pa
import uuid
import random

##################################################################################################################################
#
# Tool for generation of synthetic data directly on HDFS. Supports generation of squentially ordered data
# Adjust the rowID range (for every thread) and run it from multiple terminal windows to emulate multiple parallel threads and thus
# generate synthetic data fast
#
# Supports the follwoing Data Science Workloads:
# gmm.py
#
###################################################################################################################################

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

# 0 1:0.2550690257394217 2:0.49543508709194095 3:0.4494910647887381

#kerb_ticket=kerb_ticket
fs = pa.hdfs.connect("localhost", user="cloudera")

# hdfs file access modes: rb, wb, ab
# open and write to hdfs file
with fs.open("/user/cloudera/synt/syntdata.csv", 'wb') as f:

    for rowID in range(0, 30):

        # generates labels for Feature Vectors in the form of sequential numbers
        #f.write( (str(rowID) + ' 1:' + str(random.random())  + ' 2:' + str(random.random()) + ' 3:' + str(random.random()) + '\n').encode('UTF-8') )

        # generates labels for Feature Vectors in the form of unique numbers, which are gurateed to be unique through cryptographic means
        f.write(str(str(uuid.uuid4().int)) + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random()) + "\n")

fs.close()

