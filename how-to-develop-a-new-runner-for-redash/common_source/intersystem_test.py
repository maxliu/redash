
import sys

sys.path.append("/app/")
sys.path.append("/app/redash/")
sys.path.append("/app/redash/query_runner/")

from intersysiris import InterSysIris

sql = """
SELECT * from stock where 1=0
"""

# configuration={'namespace':'HSANALYTICS',
#                 'password':'SYS',
#                 'user':'_SYSTEM',
#                 'host':'172.17.106.224',
#                 'port':51773,
#                 'maxtablenumber': 10,
#                 'tablefilter': 'ENs% '
#                 }

#configuration={'namespace':'%SYS',
                #'password':'1234',
                #'user':'_SYSTEM',
                #'host':'192.168.1.1',
                #'port':51773,
                #'maxtablenumber': 10,
                #'tablefilter': 'ENs% ; Config%'
                #}

configuration={'namespace':'%SYS',
                'password':'1234',
                'user':'_SYSTEM',
                'host':'192.168.1.1',
                'port':51773,
                'maxtablenumber': 10,
                'tablefilter': 'ENs% ; Config%'
                }
ic = InterSysIris(configuration)

# data = ic.run_query(sql,'max')

# print(data)

sv = dict()
try:

    s = ic._get_tables(sv)
    print(s)

except Exception as e:
    print (e)
