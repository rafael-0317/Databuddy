# Title:	MYSQL_ShardedQuery -->> INFORC_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2inforc', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix Innovator C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix Innovator C client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix Innovator C db user.'), 'to_passwd': ('-p', '--to_passwd', '"infor_pwd"', 'Target Informix Innovator C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix Innovator C db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix Innovator C table.')})
	