import pyarrow as pa
import uuid
import random
from datetime import datetime, timedelta
import string

##################################################################################################################################
#
# Tool for generation of synthetic data directly on HDFS. Supports generation of squentially ordered data
# Adjust the rowID range (for every thread) and run it from multiple terminal windows to emulate multiple parallel threads and thus
# generate synthetic data fast
#
# Generates business datasets for performance testing of ETL pipelines and Algorithmic Business Analytics workloads
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

Config = {}

f = open('business-schema-dataset-gen.cfg', 'r')
line = f.readline()
while (line != ""):
    line = line.rstrip()
    x = line.split('=')
    print(x[0])
    print(x[1])
    Config[x[0]] = x[1]
    line = f.readline()

file = Config['file']
#note, in Python 3, integers have unlimited precision
range1 = int(Config['range1'])
range2 = int(Config['range2'])
hdfsHost = Config['hdfs.hostname']
user = Config['user']
days = int(Config['days'])

start = datetime.now()
end = start + timedelta(days=days)

def randString(stringLength):
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=stringLength))
    return res

#kerb_ticket=kerb_ticket
fs = pa.hdfs.connect(hdfsHost, user=user)

# hdfs file access modes: rb, wb, ab
# open and write to hdfs file
with fs.open(file, 'wb') as f:

    f.write(("NIN" + ', ' + 'NAME' + ', ' + 'BENEFITS' + ', ' + 'ADDRESS' + ', ' + 'BALANCE' +  ', ' + 'ACC_NAME' + ', ' + 'CODE' + ', ' + 'DATE' + '\n').encode('UTF-8'))

    for rowID in range(range1, range2):

        random_date = start + (end - start) * random.random()

        #f.write(( str(rowID) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' + randString(15) + ', '
                 #+ str(random_date.date()) + '\n').encode('UTF-8'))

        # generates labels for Feature Vectors in the form of unique numbers, which are gurateed to be unique through cryptographic means
        #f.write((str(uuid.uuid4().int) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' + randString(15) + ', '
                 #+ str(random_date.date()) + '\n').encode('UTF-8'))

        f.write( (  str(uuid.uuid4()) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' +  randString(10) + ', ' + str(random.random()) + ', ' + randString(15) + ', '
                 + str(random.randint(1, 500)) + ', ' + str(random_date.date()) + '\n').encode('UTF-8') )

fs.close()

