# Title:	DBTWS_ParallelQueryDir -->> TTEN_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Workgroup Server query files sql.')}, 
	{'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')})
	