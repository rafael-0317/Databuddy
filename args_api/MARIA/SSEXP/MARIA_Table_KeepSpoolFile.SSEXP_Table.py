# Title:	MARIA_Table_KeepSpoolFile -->> SSEXP_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'maria2ssexp', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MariaDB source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to MariaDB client home.'), 'from_user': ('-j', '--from_user', '"root"', 'MariaDB source user.'), 'from_passwd': ('-x', '--from_passwd', '"maria_pwd"', 'MariaDB source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MariaDB source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'master', 'SQL Server Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server Express db user.'), 'to_passwd': ('-p', '--to_passwd', '198Morgan', 'SQL Server Express user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')})
	