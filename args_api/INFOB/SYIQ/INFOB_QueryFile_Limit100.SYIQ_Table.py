# Title:	INFOB_QueryFile_Limit100 -->> SYIQ_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 100, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'infob2syiq', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with Infobright query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'Infobright source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to Infobright client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'Infobright source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'Infobright source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'Infobright source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target Sybase IQ database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to Sybase IQ client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target Sybase IQ db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target Sybase IQ db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target Sybase IQ db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target Sybase IQ table.')})
	