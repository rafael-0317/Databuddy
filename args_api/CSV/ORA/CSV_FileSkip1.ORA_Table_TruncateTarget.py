## CSV_FileSkip1 -->> ORA_Table_TruncateTarget
from args_api import args_api
api=args_api({'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2ora', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'shard_size_kb': ('-y', '--shard_size_kb', 100, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file.')}, 
	{'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.'), 'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.')})
	