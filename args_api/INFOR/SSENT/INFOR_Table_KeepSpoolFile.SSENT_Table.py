# Title:	INFOR_Table_KeepSpoolFile -->> SSENT_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'infor2ssent', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'Informix IDS source database.'), 'from_table': ('-c', '--from_table', 'Persons_pipe_datetime_1', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home.'), 'from_user': ('-j', '--from_user', '"informix"', 'Informix IDS source user.'), 'from_passwd': ('-x', '--from_passwd', '"test_pwd"', 'Informix IDS source user password.'), 'from_db_server': ('-n', '--from_db_server', '"ol_s_121414_204157"', 'Informix IDS source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server Enterprise database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server Enterprise db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server Enterprise user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')})
	