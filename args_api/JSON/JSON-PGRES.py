#do not change
aa={'JSON_Files.PGRES_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_657000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'input_dirs': ['-I', '--input_dirs', '', 'Input JSON directory.'], 'shard_size_kb': ['-y', '--shard_size_kb', '', 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'input_files': ['-i', '--input_files', '', 'Input JSON file(s).']}, {'to_db_name': ['-d', '--to_db_name', '', 'Target PostgreSQL database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to PostgreSQL client home bin dir.'], 'to_user': ['-u', '--to_user', '', 'Target PostgreSQL db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Target PostgreSQL db user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target PostgreSQL db instance name.'], 'target_port': ['-T', '--target_port', '', 'Connection port for target PostgreSQL.'], 'skip_header': ['-k', '--skip_header', '', 'Skip header line.'], 'to_table': ['-a', '--to_table', '', 'Target PostgreSQL table.']}], 'JSON_Files_noIDs.PGRES_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_660000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection_noIDs.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'JSON_Dirs.PGRES_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_543000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'JSON_Files.PGRES_Table_SkipHeader': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_654000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'skip_header': ('-k', '--skip_header', 1, 'Skip header line.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'JSON_ShardedDirs.PGRES_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_828000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'JSON_Files_noIDs.PGRES_Table_SkipHeader': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_659000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection_noIDs.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'skip_header': ('-k', '--skip_header', 1, 'Skip header line.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}], 'JSON_ShardedDirs.PGRES_Table_SkipHeader': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-pgres', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152343_826000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'skip_header': ('-k', '--skip_header', 1, 'Skip header line.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')}]}