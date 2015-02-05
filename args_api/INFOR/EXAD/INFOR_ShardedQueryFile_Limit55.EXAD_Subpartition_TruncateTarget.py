# Title:	INFOR_ShardedQueryFile_Limit55 -->> EXAD_Subpartition_TruncateTarget
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 55, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'infor2exad', 'Data copy direction.'), 'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\informix_query.sql', 'Input file with Informix IDS query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'Informix IDS source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home.'), 'from_user': ('-j', '--from_user', '"informix"', 'Informix IDS source user.'), 'from_passwd': ('-x', '--from_passwd', '"test_pwd"', 'Informix IDS source user password.'), 'from_db_server': ('-n', '--from_db_server', '"ol_s_121414_204157"', 'Informix IDS source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Exadata database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Sub_Partitioned_test_to', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'part_15_sp1', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Exadata client home bin dir.')})
	