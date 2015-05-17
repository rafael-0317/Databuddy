#do not change
aa={'CSV_ShardedDir_Limit10.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_203000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_1;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_2', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_ShardedFile_Limit10.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_304000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_FileSkip1.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_223000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 100, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'arg_6': ['-6', '--arg_6', '', 'Generic string argument 1.'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'arg_8': ['-8', '--arg_8', '', 'Generic string argument 3.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'arg_7': ['-7', '--arg_7', '', 'Generic string argument 2.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'input_dirs': ['-I', '--input_dirs', '', 'Input CSV directory.'], 'shard_size_kb': ['-y', '--shard_size_kb', '', 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'input_files': ['-i', '--input_files', '', 'Input CSV file(s).']}, {'to_db_name': ['-d', '--to_db_name', '', 'Oracle XE database.'], 'nls_date_format': ['-e', '--nls_date_format', '', 'nls_date_format for target.'], 'nls_timestamp_format': ['-m', '--nls_timestamp_format', '', 'nls_timestamp_format for target.'], 'to_user': ['-u', '--to_user', '', 'Target Oracle XE db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Oracle XE user password.'], 'nls_timestamp_tz_format': ['-O', '--nls_timestamp_tz_format', '', 'nls_timestamp_tz_format for target.'], 'to_table': ['-a', '--to_table', '', 'To Oracle table.']}], 'CSV_Dirs_Limit10.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_073000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_1;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_2', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_DateFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_153000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_dt.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_TimestampFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_324000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_ShardedFileSkip1.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_123000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_TimezoneFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_173000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_tz.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_DirsSkip1.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_374000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_1;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_2', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_DateFiles.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_273000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_dt.data;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_dt.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_File_Limit10.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_103000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_ShardedFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_053000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\oracle_shard_0_ts.data', 'Input CSV file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_ShardedDirSkip1.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_253000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_1;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_2', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'CSV_ShardedDir.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'csv-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'time_stamp': ('-Y', '--time_stamp', '20150514_144848_354000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_1;C:\\Python27\\data_migrator_1239_12c\\test\\v101\\data\\ora_data_dir_2', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}]}