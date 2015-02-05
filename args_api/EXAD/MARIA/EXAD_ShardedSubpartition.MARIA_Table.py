# Title:	EXAD_ShardedSubpartition -->> MARIA_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'exad2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_sub_partition': ('-S', '--from_sub_partition', 'part_15_sp1', 'From sub-partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Exadata client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'SCOTT.Sub_Partitioned_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	