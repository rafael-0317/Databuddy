# Title:	MARIA_QueryDir_Limit333 -->> DBTEC_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 333, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'maria2dbtec', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MariaDB source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to MariaDB client home.'), 'from_user': ('-j', '--from_user', '"root"', 'MariaDB source user.'), 'from_passwd': ('-x', '--from_passwd', '"maria_pwd"', 'MariaDB source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MariaDB source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_mysql', 'Input file with MariaDB query sql.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express C client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express C db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express C db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express C table.')})
	