# Title:	INFOB_QueryFile -->> EXAD_Partition_TruncateTarget
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'infob2exad', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with Infobright query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'Infobright source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to Infobright client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'Infobright source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'Infobright source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'Infobright source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Exadata database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Partitioned_test_to', 'To Oracle table.'), 'to_partition': ('-G', '--to_partition', 'part_15', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Exadata client home bin dir.')})
	