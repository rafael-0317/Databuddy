# Title:	MARIA_QueryFile -->> EXAD_Subpartition
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'maria2exad', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mariadb_query.sql', 'Input file with MariaDB query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MariaDB source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to MariaDB client home.'), 'from_user': ('-j', '--from_user', '"root"', 'MariaDB source user.'), 'from_passwd': ('-x', '--from_passwd', '"maria_pwd"', 'MariaDB source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MariaDB source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Exadata database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'part_15_sp1', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Exadata client home bin dir.')})
	