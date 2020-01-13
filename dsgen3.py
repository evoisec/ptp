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

fs = pa.hdfs.connect("localhost" , user="cloudera")

# file access modes: rb, wb, ab
# write to hadoop file
with fs.open("/user/cloudera/synt/part-00001-3059cdce-7ae9-478c-8e1e-03dabc916a5e-c000.csv", 'ab') as f:

    f.write(b'foobarbaz, dsfsfsf, dsfdsfsdf, dsfdsfd\n')
    f.write(b'foobarbaz, sdfsdf, dsfdsfd, dsfdsf\n')
    f.write(b'foobarbaz, sdfsdf, dsfdsfd, dsfdsf\n')


