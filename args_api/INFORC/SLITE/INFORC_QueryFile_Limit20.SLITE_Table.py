# Title:	INFORC_QueryFile_Limit20 -->> SLITE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'inforc2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\informix_query.sql', 'Input file with Informix Innovator C query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'Informix Innovator C source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix Innovator C client home.'), 'from_user': ('-j', '--from_user', '"informix"', 'Informix Innovator C source user.'), 'from_passwd': ('-x', '--from_passwd', '"test_pwd"', 'Informix Innovator C source user password.'), 'from_db_server': ('-n', '--from_db_server', '"ol_s_121414_204157"', 'Informix Innovator C source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')})
	