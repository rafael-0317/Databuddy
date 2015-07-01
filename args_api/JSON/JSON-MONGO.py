#do not change
aa={'JSON_ShardedDirs.MONGO_Collection': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_366000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.')}], 'JSON_Files_noIDs.MONGO_Collection': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_362000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection_noIDs.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'input_dirs': ['-I', '--input_dirs', '', 'Input JSON directory.'], 'shard_size_kb': ['-y', '--shard_size_kb', '', 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'input_files': ['-i', '--input_files', '', 'Input JSON file(s).']}, {'to_db_name': ['-d', '--to_db_name', '', 'MongoDB database.'], 'to_db_port': ['-T', '--to_db_port', '', 'Target MongoDB port.'], 'to_column_names': ['-Z', '--to_column_names', '', 'To column list for MongoDB.'], 'to_collection': ['-a', '--to_collection', '', 'To table.'], 'to_user': ['-u', '--to_user', '', 'Target MongoDB db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'MongoDB user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target MongoDB instance name.'], 'numInsertionWorkers': ['-numIW', '--numInsertionWorkers', '', 'Upsert rows into MongoDB.'], 'upsert': ['-G', '--upsert', '', 'Upsert rows into MongoDB.']}], 'JSON_ShardedDirs.MONGO_Collection_Upsert': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_364000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.'), 'upsert': ('-G', '--upsert', 1, 'Upsert rows into MongoDB.')}], 'JSON_Files_noIDs.MONGO_Collection_Upsert': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_360000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection_noIDs.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.'), 'upsert': ('-G', '--upsert', 1, 'Upsert rows into MongoDB.')}], 'JSON_ShardedDirs.MONGO_Collection_3_insertionWorkers': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_367000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 3, 'Upsert rows into MongoDB.')}], 'JSON_Files_noIDs.MONGO_Collection_3_insertionWorkers': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_363000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection_noIDs.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 3, 'Upsert rows into MongoDB.')}], 'JSON_Files.MONGO_Collection': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_358000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.')}], 'JSON_Dirs.MONGO_Collection_3_insertionWorkers': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_355000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 3, 'Upsert rows into MongoDB.')}], 'JSON_Files.MONGO_Collection_Upsert': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_357000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.'), 'upsert': ('-G', '--upsert', 1, 'Upsert rows into MongoDB.')}], 'JSON_Files.MONGO_Collection_3_insertionWorkers': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_359000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_files': ('-i', '--input_files', '.\\test\\v101\\data\\JSON_Mongo_Collection.js', 'Input JSON file(s).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 3, 'Upsert rows into MongoDB.')}], 'JSON_Dirs.MONGO_Collection': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'copy_vector': ('-w', '--copy_vector', 'json-mongo', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150630_152121_354000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'input_dirs': ('-I', '--input_dirs', '.\\test\\v101\\data\\JSON_data_dir', 'Input JSON directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'MongoDB database.'), 'to_db_port': ('-T', '--to_db_port', '27017', 'Target MongoDB port.'), 'to_column_names': ('-Z', '--to_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'To column list for MongoDB.'), 'to_collection': ('-a', '--to_collection', 'test', 'To table.'), 'to_user': ('-u', '--to_user', 'test_user', 'Target MongoDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'tast_pwd', 'MongoDB user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target MongoDB instance name.'), 'numInsertionWorkers': ('-numIW', '--numInsertionWorkers', 1, 'Upsert rows into MongoDB.')}]}