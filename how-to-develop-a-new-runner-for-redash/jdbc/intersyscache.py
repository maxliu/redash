
import logging
import sys

import jaydebeapi as jdbc
import jpype
import sys

from six import reraise

from redash.query_runner import BaseSQLQueryRunner, register
from redash.utils import json_dumps, json_loads

logger = logging.getLogger(__name__)

_configuration_schema = {
                "type": "object",
                "properties": {
                    "user": {
                        "type": "string",
                        "default": "_SYSTEM"
                    },
                    "password": {
                        "type": "string",
                        "default": "SYS"

                    },
                    "host": {
                        "type": "string",
                        "default": "jdbc:IRIS://172.19.0.1"
                    },
                    "port": {
                        "type": "number",
                        "default": "51773"
                    },

                    "dbname": {
                        "type": "string",
                        "title": "Database Name",
                        "default" : "USER"
                    },
                    "driver_name": {
                       "type": "string",
                       "title": "driver name",
                       "default": "com.intersystems.jdbc.IRISDriver"
                    },
                    "driver_path": {
                       "type": "string",
                       "title": "driver path",
                       "default": "/app/intersystems-jdbc-3.0.0.jar"
                    }
                },
                "order": ['host', 'user', 'password'],
                "required": ["dbname"],
                "secret": ["password"]
            }



cfg = _configuration_schema['properties']


def get_jdbc_connection(user,
                        password,
                        host,
                        port,
                        dbname,
                        driver_name,
                        driver_path
                       ):
#     driver_path = 'intersystems-jdbc-3.0.0.jar' 
#     driver_name = 'com.intersystems.jdbc.IRISDriver' 
    cfg = InterSysCache.configuration_schema()['properties']
    
    user = user if user is not None and (len(user)>=0) \
                                else cfg['user']['default'] 
    
    password = password if password is not None and (len(password)>0) \
                                else cfg['password']['default'] 
    
    host = host if host is not None and (len(host)>0) \
                                else cfg['host']['default'] 
    
    port = port if port is not None and (len(str(port))>0) \
                                else cfg['port']['default'] 
    
    dbname = dbname if dbname is not  None and (len(dbname)>0) \
                                else cfg['dbname']['default'] 
    
    driver_name = driver_name if driver_name is not None  and  (len(driver_name)>0) \
                                else cfg['driver_name']['default'] 
    
    driver_path = driver_path if driver_path is not None and   (len(driver_path)>0) \
                                else cfg['driver_path']['default'] 
    
    if host[-1]=='/':
        host = host[:-1]

    args='-Djava.class.path=%s' % driver_path
        
    jvm = jpype.getDefaultJVMPath()
    try:
        jpype.startJVM(jvm, args)
    except:
        pass
    
    if jpype.isJVMStarted() and not jpype.isThreadAttachedToJVM():
        jpype.attachThreadToJVM()
        jpype.java.lang.Thread.currentThread().setContextClassLoader(jpype.java.lang.ClassLoader.getSystemClassLoader())
    
    conn_str = host + ':' + str(port) + '/' + dbname + '/'
    
#     logger.info("\n\n\n", conn_str)
#     logger.info("\n\n\n")
    
#     conn_str = "jdbc:IRIS://172.19.0.1:51773/USER"

    connection = jdbc.connect(
        driver_name,
        conn_str,
        {'user': user, 'password': password, 'tmode': 'TERA', 'charset': 'UTF8'},
        driver_path )
    
    return connection

       
class InterSysCache(BaseSQLQueryRunner):
    noop_query = "select 1"

    @classmethod
    def configuration_schema(cls):
        return _configuration_schema

    @classmethod
    def type(cls):
        return "intersyscache"

    def __init__(self, configuration):
        super(InterSysCache, self).__init__(configuration)


    def _get_tables(self, schema):

        query_table = """
                SELECT '"' || TABLE_SCHEMA || '"."' || TABLE_NAME || '"' as tbl_name 
                from INFORMATION_SCHEMA.TABLES
                where TABLE_TYPE='BASE TABLE' and TABLE_SCHEMA not like 'Ens%'
            """

        query_columns = "SELECT * from(%s) where 1=0"

        
        results, error = self.run_query(query_table, None)

        if error is not None:
            raise Exception("Failed getting schema.")

        results = json_loads(results)

        for row in results['rows']:

            table_name = row['tbl_name']
            schema[table_name] = {'name': table_name, 'columns': []}

            results_table, error = self.run_query(query_columns % (table_name,), None)
            if error is not None:
                raise Exception("Failed getting schema.")

        return schema.values()

    def run_query(self, query, user):

        connection = get_jdbc_connection(
                        user = self.configuration.get('user')  ,
                        password = self.configuration.get('password'),
                        host = self.configuration.get('host'),
                        port = self.configuration.get('port'),
                        dbname = self.configuration.get('dbname'),
                        driver_name = self.configuration.get('driver_name', "com.intersystems.jdbc.IRISDriver"),
                        driver_path = self.configuration.get('driver_path')
                        )
        
        cursor = connection.cursor()

        try:
            cursor.execute(query)

            if cursor.description is not None:
                columns0 =  [col[0] for col in cursor.description]
                
                columns = self.fetch_columns([(i, None) for i in columns0])
                rows = cursor.fetchall()
                row_data = [dict(zip(columns0, row)) for row in rows]             
                data = {'columns': columns, 'rows': row_data}
                error = None
                json_data = json_dumps(data)
            else:
                error = 'Query completed but it returned no data.'
                json_data = None
        except KeyboardInterrupt:
            connection.cancel()
            error = "Query cancelled by user."
            json_data = None
        except Exception as e:
            err_class = sys.exc_info()[1].__class__
            err_args = [arg.decode('utf-8') for arg in sys.exc_info()[1].args]
            unicode_err = err_class(*err_args)
            reraise(unicode_err, None, sys.exc_info()[2])
        finally:
            connection.close()
        return json_data, error
#     
register(InterSysCache)