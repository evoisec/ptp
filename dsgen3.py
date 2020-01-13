import pyarrow as pa

######################################################################
#
# Tool for generation of synthetic data directly on HDFS. Supports generation of squentially ordered data
#
######################################################################

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
fs = pa.hdfs.connect("localhost" , user="cloudera")

# hdfs file access modes: rb, wb, ab
# write to hadoop file
with fs.open("/user/cloudera/synt/syntdata.csv", 'wb') as f:

    for i in range(1, 30):

        f.write((str(i) + ', foobarbaz, dsfsfsf, dsfdsfsdf, dsfdsfd\n').encode('UTF-8')  )

fs.close()

