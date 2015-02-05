# Title:	ORA11G_Partition_NoClient -->> DBTDE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ora11g2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_partition': ('-P', '--from_partition', 'part_15', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', "SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))'", 'From database.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'SCOTT.Partitioned_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')})
	