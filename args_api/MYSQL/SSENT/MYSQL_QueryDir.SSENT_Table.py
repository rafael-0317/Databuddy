# Title:	MYSQL_QueryDir -->> SSENT_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2ssent', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_mysql', 'Input file with MySQL query sql.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server Enterprise database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server Enterprise db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server Enterprise user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')})
	