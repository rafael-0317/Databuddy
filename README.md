# DataBuddy
Do it yourself data integration starter kit.
(Treat it as a work of art rather than something useful)

##Version

Name|OS|Platform|data-buddy (GUI) | DataBuddy CLI (command line)
---|---|---|---- | -------------
DataBuddy.exe|Windows|32bit|[0.3.5 beta](https://github.com/data-buddy/DataBuddy/releases/tag/0.3.5) | [1.23.9 beta] (https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9)
>There are 2 components. Upon "Run" Databuddy GUI (DataBuddy.exe) will kick off Databuddy CLI (`qc32\qc.exe`) out of process.

##Purpose

- It is data integration software used to define technical processes to combine data from different sources. Data is moved across RDBMS borders using CSV files.
- __DataBuddy__ facilitates data delivery from multiple relational data sources including Oracle, SQLServer, DB2, SAP Sybase, Informix, MySQL, Infobright, MariaDB, PostgreSQL, TimesTen, and SQLite.
- It requires minimal initial configuration and lets you manage data integration process using GUI or command line.
- Your data integration processes are stored as session files and can be scripted into your ETL pipelines or used in ad-hoc manner.
- Lets you develop Extract-Copy-Load processes to scrub and ingest large, distinct data sets from multiple sources into a unified data warehouse.
- Provides structured and ad-hoc access to large datasets.
- Databuddy also supports enables seamless, bi-directional integration between all major RDBMSs, such as Oracle, SQLServer, DB2, SAP Sybase, Informix, MySQL, Infobright, MariaDB, and PostgreSQL. In addition,
it supports self-service data extraction, preparation, and cleansing by database developers.

##Other scripts
  - [Oracle -> Redshift](https://github.com/alexbuz/Oracle-To-Redshift-Data-Loader/blob/master/README.md) data loader
  - [PostgreSQL -> Redshift](https://github.com/alexbuz/PostgreSQL_To_Redshift_Loader/blob/master/README.md) data loader
  - [MySQL -> Redshift](https://github.com/alexbuz/MySQL_To_Redshift_Loader/blob/master/README.md) data loader
  - [Oracle -> S3](https://github.com/alexbuz/Oracle_To_S3_Data_Uploader/blob/master/README.md) data loader
  - [CSV -> Redshift](https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/README.md) data loader
  
##Audience

Database developers, ETL developers, Data Integrators.

##Designated Environment
Pre-Prod (UAT/QA/DEV)


##Databases supported

###SQL
Database | GUI (DataBuddy) | Command line (DataBuddy CLI)
---------|---- | -------------
DB2      | yes | yes
Informix | yes  | yes
MariaDB    | yes | yes
MySQL    | yes | yes
Infobright    | yes | yes
**Oracle**   | yes | [yes](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9)
PostgreSQL| yes | yes
SQLite| yes | yes
SQLServer| yes | yes
Sybase   | yes  | yes
TimesTen| yes  | yes

###noSQL
Database | GUI (data-buddy) | Command line (DataBuddy CLI)
---------|---- | -------------
MongoDB      | yes | yes

##Data Tools
Name| GUI (data-buddy) | Command line (DataBuddy CLI)
---------|---- | -------------
CURL      | yes | yes


##File formats

###SQL
Database | DDL extract | CSV extract | CSV load
---------|---- | ------------- | -------
DB2      |  | yes  | yes
Informix |  | yes  | yes
MariaDB    |  | yes  | yes
MySQL    |  | yes  | yes
**Oracle**   | Table | yes  | yes
PostgreSQL|  | yes  | yes
SQLite|  | yes  | yes
SQLServer|   | yes  | yes
Sybase   |  | yes  | yes
TimesTen|  | yes  | yes
> DDL extract works only for Oracle tables.

###noSQL
Database |  CSV extract | CSV load | JSON extract | JSON load
---------|-------------- | -------| -------| -------
MongoDB      | yes  | yes | yes | yes

###Data Tools
Database |  CSV extract | CSV load | JSON extract | JSON load
---------|-------------- | -------| -------| -------
CURL      | yes  |   | yes |  


##Components
- GUI - data-buddy (wxPython, PyInstaller).
- Command line -[DataBuddy CLI](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9) (Python, PyInstaller).

##Features:

###Front end, GUI (data-buddy).

- Session management.

###Command line (DataBuddy CLI):
- [x] Multi-query load.
- [x] Partition/sub-partition copy
- [x] Sharded copy (turbo mode)
- [x] Custom spool location (config/user_conf.py)
- [x] config/include/oracle.py - configurable SQL*Loader args.
- [x] 3 generic arguments (use them to pass job_id or timestamp and process in config/user_config.py)
- [x] added all usecases
- [x] lame_duck/limit fix for trial runs
- [x] keep_data_file param (set it to 1 if you want to keep data dump)
- [x] White-space control.
- [x] Header line control.
- [x] Truncate target table/partition/subpartition
- [x] Ask to truncate.
- [x] No client (url) connect.
- [x] Supports CSV file load from multiple dirs.
- [x] --exit_on_key - let's you keep exec window open after load job is done
- [x] file download using curl.exe

## Pipeline types
- E __Extract__
- L __Load__
- C __Copy__

###SQL
Database | Table | Partition | Subpartition |CSV Files|Queries
---------|---- | ------------- | ---------|-----|-----
DB2      | E/L/C |   | | L/E   | E/C  
Informix | E/L/C |   |  |  L/E   | E/C 
MariaDB    | E/L/C |   |  |  L/E  | E/C 
MySQL    |E/L/C  |   |  |  L/E   | E/C 
**Oracle**   | E/L/C | E/L/C  | E/L/C |   L/E   | E/C 
PostgreSQL| E/L/C | E/L/C  | E/L/C |  L/E   | E/C 
SQLite| E/L/C |  |  |  L/E   | E/C 
SQLServer| E/L/C  | E/L/C  | |   L/E   | E/C 
Sybase   | E/L/C |   |  |   L/E   |E/C 
TimesTen| E/L/C |   |  |  L/E   | E/C 
###noSQL
Database | Collection |CSV Files|JSON Files|Queries
---------|-------------- |-----|-----|-----|---
MongoDB  | E/L/C   |    E/L   |   E/L   | E/C 


 
##Tools used to extract, load, and query data

1. __DbShell__ - queries target and source for table metadata.
2. __Spooler__  - extracts data to temp file from source.
3. __Loader__ - loads temp file to target using bulk loader.

####SQL stores.
DB family|Database | Spooler | Loader | DbShell
---------|----------|-------- | -------| -------
DB2 | DB2 Advanced Enterprise Server | db2.exe | db2.exe | db2.exe
 | DB2 Advanced Workgroup Server | db2.exe | db2.exe | db2.exe
 | DB2 Developer Edition | db2.exe | db2.exe | db2.exe
 | DB2 Express | db2.exe | db2.exe | db2.exe
 | DB2 Express C | db2.exe | db2.exe | db2.exe
 | DB2 Enterprise Server | db2.exe | db2.exe | db2.exe
 | DB2 Workgroup Server | db2.exe | db2.exe | db2.exe
MySQL | MySQL | mysql.exe | mysql.exe | mysql.exe 
 | Infobright | mysql.exe | mysql.exe | mysql.exe
 | MariaDB | mysql.exe | mysql.exe | mysql.exe 
Informix | Informix IDS | dbaccess.exe | dbaccess.exe | dbaccess.exe
 | Informix Innovator C | dbaccess.exe | dbaccess.exe | dbaccess.exe
Oracle | Oracle 12c | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Oracle 11g | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Exadata | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Oracle XE | sqlplus.exe | sqlldr.exe | sqlplus.exe
PostgreSQL | PostgreSQL | psql.exe | psql.exe | psql.exe
SQL Server | SQL Server Enterprise | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
 | SQL Server Express | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
SAP Sybase | Sybase SQL Anywhere | dbisql.com | dbisql.com | dbisql.com
 | SAP Sybase ASE | dbisql.com | dbisql.com | dbisql.com
 | Sybase IQ | dbisql.com | dbisql.com | dbisql.com
TimesTen | TimesTen | ttBulkCp.exe | ttBulkCp.exe | ttIsql.exe
SQLite | SQLite | sqlite3.exe | sqlite3.exe | sqlite3.exe

####noSQL stores.
Database | Spooler | Loader | DbShell
----------|-------- | -------| -------
 MongoDB | mongoexport.exe  | mongoimport.exe | mongo.exe
 
####Data Tools.
Database | Spooler | Loader | DbShell
----------|-------- | -------| -------
 CURL | curl.exe  | n/a | n/a


## What it doesn't do
- It does not create target table.
- It does not pipe data (it extracts into a file then loads).
- It should not be used in Prod. Trial/ad-hoc use only.


##Implementation

- Written using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller

##Configuration
- modify default host_map.py: ![host_map.py](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/edit_hostmap.png "Edit host_map.py")
- set your 'source' and 'target' dirs for local clients for each database.
```python
 'host_list': {0: {'db_env': {'ORA11G': {'source': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN',
                                         'target': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN'},
```
- you are good to go

##Execution
* data-buddy.exe

>from Windows command line or File Explorer

#Target object Truncate
- it will popup with warning window every time you try to run DataBuddy CLI truncating you target object.
![truncate](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/truncate_target.png "Truncate target")

#Templates v.s. free argument entry
##Pros
- all templates are tested with presets

##Cons
- user has to create new session if new argument has to be added/removed

>There's no way to add/remove args to your choosing. Argument combos come as templates which you select in "Create new session window"

#TODO
- [x] argument values reuse from existing session. **DONE**
- [x] clean uargs.db. **DONE**
- [x] nls_format* duplication. **DONE**
- [ ] test UI.
- [x] add --log_dir to backend. **DONE**
- [x] add "source" and "target" datasources to "New Session". **DONE**
- [ ] Copy/Paste of argument values between sessions.
- [x] generic "New Session" so user not limited by source and target templates. **DONE**
- [ ] history of values for each argument.
- [ ] cleanup all other databases but Oracle.
- [ ] more templates and better templates hierarchy.
- [x] init templates to open session for "New Session". **DONE**
- [x] validate args on Run. **DONE**.
- [ ] smaller test_api files (get default args from test routines, not canned files).
- [x] fix template filters. **DONE**
- [ ] create "Menu" button and hide "About".
- [x] create templates tab **DONE**
- [x] create sessions tab **DONE**
- [x] validate session name for chars not usable in file name. **DONE**
- [x] allow user to create multiple session libraries. **DONE**
- [x] fix mailformed path from MDD.MultiDirDialog. **DONE**
- [x] make sure all paths are windows friendly.**DONE**
- [x] open dir and open file use stale values.**DONE**
- [x] filter control keys from ones affecting field value. **DONE**
- [ ] close all existing shells/shell groups upon exit.
- [x] highlight running sessions.**DONE**
- [ ] beep on failing sessions.
- [x] free argument entry.**DONE**
- [x] let user change arg list for a given group. **DONE**
- [x] detect DONE/FAILED from cmd window. **DONE**
- [x] let user disable post-etl email (Common: email_to). **DONE**
- [ ] change copy_vector format from db2db to db-db **DONE**
- [x] fix flicker on frame freeze **DONE**
- [x] save on close **DONE**
- [x] Table DDL export for Oracle **DONE**
- [x] validate all path arguments before run **DONE**
- [x] add create template menu **DONE**
- [x] add "--host_map" arg to set hosts for each thread **DONE**
- [x] let user change host mapping **DONE**
- [x] save as template **DONE**
- [x] save as **DONE**
- [x] create main menu **DONE**
- [ ] let user configure dafault argument values  
- [x] let user chenge frame size **DONE**
- [ ] test ezconnect
- [x] add "Output" tab **DONE**
- [ ] add '--compress_spool' arg for zipped output
- [x] add sqlloader.py **DONE**
- [x] add curl.exe for file download **DONE**
- [ ] load/save app state.
- [x] remove wx.BitmapButton memory leak
- [x] fix session sort **DONE**
- [x] fix session refresh **DONE**
- [x] fix awg.flatmenu memory leak **DONE**
- [x] fix awg.scrollablepanel memory leak
- [ ] let user set primary dbs, source/target dbs
- [ ] add scp/ftp/sftp as data source/target 
- [ ] make all paths relative to transport_home **DONE**
- [ ] create wizard for "New Session" template selection
- [ ] distinguish A-Templates from B-Templates
- [x] let data copy to be executed on Linux (bash via nssh)**DONE**
- [ ] let data spool/load to be executed on Linux (bash via ssh)
- [ ] use netcat for job status instead of keeping open ssh conn
- [ ] use named file for QC status report instead of CLI title.
- [x] add [Oracle 12c Release 1](http://docs.oracle.com/database/121/index.htm) **DONE**
- [x] add [Oracle 11g Release 2](https://docs.oracle.com/cd/E11882_01/nav/portal_4.htm) **DONE**
- [x] add [SQLServer](https://msdn.microsoft.com/en-US/sqlserver)   **DONE**
- [x] add [MySQL](http://dev.mysql.com/doc/)    **DONE**
- [x] add [PostgreSQL](http://www.postgresql.org/docs/)   **DONE**
- [x] add [SQLite](https://www.sqlite.org/docs.html)   **DONE**
- [x] add [Informix](http://www-01.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.welcome.doc/welcome.htm?lang=en)   **DONE**
- [x] add [SAP ASE Sybase](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.help.ase.15.7/title.htm)   **DONE**
- [x] add [DB2](http://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.kc.doc/welcome.html)    **DONE**
- [ ] add [dBase](http://www.dbase.com/dbasesql/dbase-documentation-download/)   
- [ ] add [MS Access](https://msdn.microsoft.com/en-us/library/office/ff604965%28v=office.14%29.aspx)
- [ ] add [Pandas](http://pandas.pydata.org/pandas-docs/version/0.12.0/)   
- [ ] add [Apache Spark] (https://spark.apache.org/docs/latest/)  
- [ ] add [Apache Storm] (https://storm.apache.org/documentation/Home.html)  
- [ ] add [Hadoop](http://hadoop.apache.org/docs/r2.7.0/)  
- [ ] add [ZooKeeper](https://zookeeper.apache.org/)  
- [ ] add [HDFS](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)  
- [x] add [MariaDB](https://mariadb.com/kb/en/mariadb/documentation/)  **DONE**
- [x] add [Infobright](https://www.infobright.com/index.php/community-2/)    **DONE**
- [x] add [TimesTen](http://www.oracle.com/technetwork/database/database-technologies/timesten/documentation/index.html)    **DONE**
- [ ] add [MongoDB] (http://docs.mongodb.org/manual/)  **DONE**
- [ ] add [HBase] (http://hbase.apache.org/)  
- [ ] add [Cassandra] (http://cassandra.apache.org/)  
- [ ] add [Bigtable] (https://cloud.google.com/bigtable/docs/)  
- [ ] add [Teradata] (http://www.info.teradata.com/HTMLPubs/DB_TTU_14_00/index.html#page/Storage_Management/B035_2492_071A/2492ch01.084.17.html)  
- [ ] add [Apache Hive] (http://doc.mapr.com/display/MapR/Hive)    
- [ ] add [Vertica](http://www.vertica.com/hp-vertica-documentation/hp-vertica-7-1-x-documentation/)   
- [ ] add [Netezza](https://www-304.ibm.com/support/knowledgecenter/SSULQD_7.2.0/com.ibm.nz.welcome.doc/doc/welcome.html)   
- [ ] add Parstream
- [ ] add ParAccel
- [ ] add [Redis](http://redis.io/)   
- [ ] add [ZODB](http://www.zodb.org/en/latest/documentation/tutorial.html) 
- [ ] add [MonetDB](https://en.wikipedia.org/wiki/MonetDB)  
- [ ] add [Vectorwise](https://en.wikipedia.org/wiki/Vectorwise)   
- [ ] add [MarkLogic](http://www.marklogic.com/what-is-marklogic/features/)   
- [ ] add [Amazon SimpleDB](http://aws.amazon.com/documentation/simpledb/)  
- [ ] add [Twitter Streaming API](https://dev.twitter.com/streaming/overview)  (extract)
- [ ] add [Google Analytics](https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py)  
- [ ] add [Crate Data](https://www.openhub.net/p/cratedata)
- [ ] add Facebook (extract)
- [ ] add Taleo HR (extract) 
- [ ] add Salesforce ([load](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/), extract) 
- [ ] add [Greenplum](http://gpdb.docs.pivotal.io/gpdb-435.html)  
- [ ] add [Actian Ingres](http://esd.actian.com/product/docs)  
- [ ] add [McObject](http://www.mcobject.com/embedded-database-manuals)  
- [ ] add [NuiDB](http://doc.nuodb.com/display/doc/NuoDB+Online+Documentation)  
- [ ] add [Disco](https://www.openhub.net/p/disco)
- [ ] add [Clustrix](http://docs.clustrix.com/display/CLXDOC/Home)  
- [ ] add [OrientDB](http://orientdb.com/docs/last/)   
- [ ] add [KDB+](http://kx.com/resources.php)  
- [ ] add [Volt DB](http://docs.voltdb.com/)  
- [ ] add [Elasticsearch](https://www.found.no/foundation/elasticsearch-as-nosql/)  
- [ ] add [Azure DocumentDB](http://azure.microsoft.com/en-us/services/documentdb/)  
- [ ] add [Arango DB](https://www.arangodb.com/documentation/)   
- [ ] add [Foundation DB](https://foundationdb.com/key-value-store/documentation/index.html)  
- [ ] add [Enterprise DB](http://www.enterprisedb.com/products-services-training/products/documentation)   
- [ ] add [Altibase HDB](http://altibase.com/)   
- [ ] add [EXASOL](https://www.exasol.com/support/secure/attachment/30841/EXASolution_User_Manual-5.0.3-en.pdf)   
- [ ] add [Aster](http://www.teradata.com/Teradata-Aster/overview/)  
- [ ] add [Kinesis](http://aws.amazon.com/documentation/kinesis/) (extract)
- [ ] add [Amazon Redshift](http://aws.amazon.com/documentation/redshift/)   
- [ ] add [Amazon Aurora (RDS)](https://aws.amazon.com/blogs/aws/highly-scalable-mysql-compat-rds-db-engine/) 
- [ ] add [RethinkDB](https://www.rethinkdb.com/docs/)  
- [ ] add [Amazon DynamoDB](http://aws.amazon.com/documentation/dynamodb/)  
- [ ] add [Couchbase](http://docs.couchbase.com/admin/admin/Couchbase-intro.html)  
- [ ] add [Aerospike](http://www.aerospike.com/docs/)   
- [ ] add [Riak](https://docs.basho.com/)
- [ ] add [MemSQL](http://docs.memsql.com/latest/)
- [ ] add [InterSystems Caché](http://www.intersystems.com/our-products/cache/managing-data/),  [export](http://docs.intersystems.com/ens20131/csp/docbook/DocBook.UI.Page.cls?KEY=GSQL_shell)   
- [ ] add QV (QlikView file format)
- [ ] add MDX (file format)
- [ ] add [SQream DB](http://sqream.com/solutions/products/sqream-db/) 
- [ ] add [1010data] (https://www.1010data.com/technology)
- [ ] add [Kognitio](http://kognitio.com/analyticalplatform/)
- [ ] add [SAND Technology](http://www.sand.com/)
- [ ] add [InfiniDB](http://infinidb.co/)
- [ ] add [SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse/) 
- [ ] Create tests using [PyAutoGUI](http://pyautogui.readthedocs.org/en/latest/)
- [ ] Add Amazon Simple Storage Service [S3] (https://aws.amazon.com/s3/)
- [ ] Apache Derby (https://db.apache.org/derby/)

##Limitations
- tested to run only on Windows for now (even thou it's wxPython)
- CSV dump files are uncompressed (will add zip compression as option)
- physical copy is done on Windows. Only Oracle copy can be executed on Linux (bash via ssh)

##Performance
- data copy speed mostly depends on your NIC(Ethernet) speed and other factors like how _far_ you are from target and source servers (in terms of network topology and physically). 

>I've seen 10x performance improvement when I ran it on DEV Linux server (10Gb Ethernet) v.s. my office Windows Desktop (100Mb Ethernet).

##References
* [DataBuddy CLI for Oracle](https://github.com/QueryCopy/QueryCopy-for-Oracle) -- `qc32\qc32.exe`


##Vendor Docs

Database |Version | Export | Import | DbShell|File formats
---------|----------|-------- | -------| -------|------
[Oracle 12c](http://docs.oracle.com/database/121/index.htm)  |`12c Release 1` |[SQL*Plus ](https://docs.oracle.com/database/121/SQPUG/toc.htm)|[SQL*Loader ](https://docs.oracle.com/database/121/SUTIL/ldr_concepts.htm#SUTIL003) || CSV, DDL
[Oracle 11g](https://docs.oracle.com/cd/E11882_01/nav/portal_4.htm) | `11g Release 2`| |||
[Disco](https://www.openhub.net/p/disco)|||||
[Crate Data](https://www.openhub.net/p/cratedata)|||||
[MongoDB](http://docs.mongodb.org/manual/)| `3.0` |[mongoexport](http://docs.mongodb.org/v2.2/reference/mongoexport/)  |[mongoimport](http://docs.mongodb.org/v2.2/reference/mongoimport/) |[mongo shell](http://docs.mongodb.org/manual/faq/mongo/)  | CSV, JSON
[TimesTen](http://www.oracle.com/technetwork/database/database-technologies/timesten/documentation/index.html)|`Release 2`||||
[Amazon DynamoDB](http://aws.amazon.com/documentation/dynamodb/) |||||
[Hadoop](http://hadoop.apache.org/docs/r2.7.0/) |`r2.7.0` ||||
[EXASOL](https://www.exasol.com/support/secure/attachment/30841/EXASolution_User_Manual-5.0.3-en.pdf) |`5.0.3`||||pdf
[Kinesis](http://aws.amazon.com/documentation/kinesis/)||||
[Netezza](https://www-304.ibm.com/support/knowledgecenter/SSULQD_7.2.0/com.ibm.nz.welcome.doc/doc/welcome.html) |`7.2.0` ||||
[KDB+](http://kx.com/resources.php)|||||
[Aster](http://www.teradata.com/Teradata-Aster/overview/) |||||
[Aerospike](http://www.aerospike.com/docs/) |||||
[Couchbase](http://docs.couchbase.com/admin/admin/Couchbase-intro.html) |||||
[Redshift](http://aws.amazon.com/documentation/redshift/) |||||
[Enterprise DB](http://www.enterprisedb.com/products-services-training/products/documentation)  |||||
[Foundation DB](https://foundationdb.com/key-value-store/documentation/index.html) |||||
[Arango DB](https://www.arangodb.com/documentation/) |||||
[Volt DB](http://docs.voltdb.com/)  |||||
[OrientDB](http://orientdb.com/docs/last/) |||||
[Clustrix](http://docs.clustrix.com/display/CLXDOC/Home)  |||||
[NuiDB](http://doc.nuodb.com/display/doc/NuoDB+Online+Documentation) |||||
[McObject](http://www.mcobject.com/embedded-database-manuals) |||||
[Actian Ingres](http://esd.actian.com/product/docs) |||||
[Greenplum](http://gpdb.docs.pivotal.io/gpdb-435.html)|||||
[Salesforce](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/) ||[DataLoader](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/)|||
[Twitter Streaming API](https://dev.twitter.com/streaming/overview)|||||
[Google Analytics](https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py)|||||
[Vertica](http://www.vertica.com/hp-vertica-documentation/hp-vertica-7-1-x-documentation/)|`7-1-x`||||
[SQLServer](https://msdn.microsoft.com/en-US/sqlserver)|||||
[MySQL](http://dev.mysql.com/doc/)|||||
[PostgreSQL](http://www.postgresql.org/docs/)|||||
[SQLite](https://www.sqlite.org/docs.html)|||||
[Informix](http://www-01.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.welcome.doc/welcome.htm?lang=en)| `12.1.0`||||
[SAP ASE Sybase](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.help.ase.15.7/title.htm)|||||
[DB2](http://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.kc.doc/welcome.html)| `10.5.0`||||
[dBase](http://www.dbase.com/dbasesql/dbase-documentation-download/)|||||
[MS Access](https://msdn.microsoft.com/en-us/library/office/ff604965%28v=office.14%29.aspx)| `10.0` ||||
[Pandas](http://pandas.pydata.org/pandas-docs/version/0.12.0/)|||||
[Apache Spark](https://spark.apache.org/docs/latest/)|||||
[Apache Storm](https://storm.apache.org/documentation/Home.html)|||||
[MariaDB](https://mariadb.com/kb/en/mariadb/documentation/)|||| |
[Infobright](https://www.infobright.com/index.php/community-2/)|||||
[Cassandra] (http://cassandra.apache.org/)|||||
[HBase] (http://hbase.apache.org/)|||||
[Teradata] (http://www.info.teradata.com/HTMLPubs/DB_TTU_14_00/index.html#page/Storage_Management/B035_2492_071A/2492ch01.084.17.html)|||||
[Bigtable] (https://cloud.google.com/bigtable/docs/)|||||
[Apache Hive] (http://doc.mapr.com/display/MapR/Hive)|||||
[InterSystems Caché](http://www.intersystems.com/our-products/cache/managing-data/)||| [export](http://docs.intersystems.com/ens20131/csp/docbook/DocBook.UI.Page.cls?KEY=GSQL_shell)|||
[Altibase HDB](http://altibase.com/)|||||
[ZooKeeper](https://zookeeper.apache.org/)|||||
[HDFS](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)|||||
[Amazon SimpleDB](http://aws.amazon.com/documentation/simpledb/)|||||
[Amazon Redshift](http://aws.amazon.com/documentation/redshift/) |||||
[Azure DocumentDB](http://azure.microsoft.com/en-us/services/documentdb/)  |||||
[Elasticsearch](https://www.found.no/foundation/elasticsearch-as-nosql/)   |||||
[Riak](https://docs.basho.com/)|||||
[MemSQL](http://docs.memsql.com/latest/)|||||
[MarkLogic](http://www.marklogic.com/what-is-marklogic/features/) |||||
[SQream DB](http://sqream.com/solutions/products/sqream-db/)|||||
[1010data] (https://www.1010data.com/technology)|||||
[Kognitio](http://kognitio.com/analyticalplatform/)|||||
[SAND Technology](http://www.sand.com/)|||||
[Redis](http://redis.io/)|||||
[ZODB](http://www.zodb.org/en/latest/documentation/tutorial.html) |||||
[Amazon Simple Storage Service/S3](https://aws.amazon.com/s3/) |||||
[Amazon Aurora](https://aws.amazon.com/blogs/aws/highly-scalable-mysql-compat-rds-db-engine/) |||||
[RethinkDB](https://www.rethinkdb.com/docs/)  |||||
[Apache Derby] (https://db.apache.org/derby/) |||||
[InfiniDB](http://infinidb.co/) |||||
[SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse/) |||||



## Vendor architecture
[MongoDB Architecture Guide] (http://s3.amazonaws.com/info-mongodb-com/MongoDB_Architecture_Guide.pdf)

Data Tools |Version 
---------|----------
[cURL] (http://curl.haxx.se/download.html)| 7.33

## Screenshots

- New Session Menu: 

![New Session Menu](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/new_session_all_dbs.png "New Session Menu")


- Add New Session: 

![Add New Session](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/new_session.png "Add New Session")

- Run Session: 

![Run Session](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Run_Session_for_SQLServer_to_CSV_file_extract.png "Run Session")

- Executed Session: 

![Executed Session](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Session_Executed_for_SQLServer_to_CSV_file_extract.png "Executed Session")

- Output Tab: 

![Output Tab](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/ouput_tab.png "Output Tab")


##Copy vector matrix (via CSV)
Database | DB2 | Informix | MariaDB |MySQL| **Oracle**|PostgreSQL|SQLite|SQLServer|Sybase|TimesTen|MongoDB
---------|---- | ------- | -------|---- | ------ | -------|---- | -------| -------|----|-----
DB2      |x|x|x|x|x|x|x|x|x|x|x
Informix |x|x|x|x|x|x|x|x|x|x|x
MariaDB  |x|x|x|x|x|x|x|x|x|x|x
MySQL    |x|x|x|x|x|x|x|x|x|x|x
**Oracle** |x|x|x|x|x|x|x|x|x|x|x
PostgreSQL|x|x|x|x|x|x|x|x|x|x|x
SQLite|x|x|x|x|x|x|x|x|x|x|x
SQLServer|x|x|x|x|x|x|x|x|x|x|x
Sybase|x|x|x|x|x|x|x|x|x|x|x
TimesTen|x|x|x|x|x|x|x|x|x|x|x
Mongo DB|x|x|x|x|[X](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/MongoDB/Copy/Copy_Table_Data_From_Oracle_to_MongoDB_Collection.md)|x|x|x|x|x|x


> 'x' means feature is implemented and is part of the release [0.3.3](https://github.com/data-buddy/DataBuddy/releases/tag/v0.3.3)

##Copy vector matrix (via JSON)
Database |MongoDB
---------|-----
DB2      |x
Informix |x
MariaDB  |x
MySQL    |x
**Oracle** |x
PostgreSQL|x
SQLite|x
SQLServer|x
Sybase|x
TimesTen|x
Mongo DB|x



##Databuddy Docs
- [ ] General docs
 - [Configure_Databuddy0.3.3](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/Configure_Databuddy0.3.3.md)
 - [How_to_start_Databuddy](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/How_to_start_Databuddy.md)
 
- [ ] SQL Server
 * [Extracting_Table_Data_From_SQLServer_to_CSV_File](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/SQLServerEnterprise/Extract/Extracting_Table_Data_From_SQLServer_to_CSV_File.md) 
- [ ] MongoDB
 - [Copy_Table_Data_From_Oracle_to_MongoDB_Collection](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/MongoDB/Copy/Copy_Table_Data_From_Oracle_to_MongoDB_Collection.md)
- [ ] Oracle
 - [Copy_Table_Data_From_Oracle_to_MongoDB_Collection](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/MongoDB/Copy/Copy_Table_Data_From_Oracle_to_MongoDB_Collection.md) 

- [ ] CURL
- [Copy_data_from_Web_to_Oracle11g](https://github.com/data-buddy/Databuddy/blob/master/Docs/markdown/CURL/Copy/Copy_data_from_Web_to_Oracle11g.md) 


##Download
* `git clone https://github.com/data-buddy/DataBuddy/`
* [Data Buddy latest release](https://github.com/data-buddy/DataBuddy/releases/tag/0.3.5) -- `data-buddy 0.3.5`
* 


#   
#FAQ
#  
#### Can it load CSV file from Windows desktop to Oracle database.
Yes, it is the main purpose of this tool.

#### Can developers integrate CSV loader into their ETL pipelines?
Yes, assuming they are doing it on OS Windows.

#### How fast is data upload using `Databuddy`?
It is as fast as SQL*Loader because I'm using SQL*Loader in DIRECT mode.

####How to inscrease upload speed?
Parallelize your load by loading multiple partitions in parallel or sharding your data.

#### What are the other ways to upload file to Oracle?
You can use SQL*Loader or execute insert statements using ODBC/JDBC or SQL*Plus.

#### Can I just zip it using Windows File Explorer?
No, Redshift will not recognize *.zip file format.
You have to `gzip` it. You can use 7-Zip to do that.


#### Does it delete source file load?
No

#### Does it create target Oracle table?
No

#### I'm experiencing errors in Oracle. How can I debug?
You can set Common Args `debug_level` to a value>1

#### Explain how it works?
 - The CSV file you provided is analyzed - number of records in it is estimated.
 - Control file is created using target table column names.
 - Data is loaded using SQL*Loader


#### How do I skip the header record in input CSV file?
Use `--skip_rows  1` to ignore input rows.

#### How do i set custom timestamp format for Oracle load?
Use `--nls_date_format "MM/DD/YYYY HH12:MI:SS"` or `--nls_timestamp_format "MM/DD/YYYY HH12:MI:SS.FF2 PM"` or `--nls_timestamp_tz_format "MM/DD/YYYY HH12:MI:SS.FF2 TZH:TZM"` to control timestamp format.


#### What technology was used to create this tool
I used SQL*Loader and  wxPython to write it.


#### Where are the sources?
Please, contact me for sources.

#### Can you modify functionality and add features?
Yes, please, ask me for new features.

#### What other AWS tools you've created?
- [Oracle_To_S3_Data_Uploader] (https://github.com/alexbuz/Oracle_To_S3_Data_Uploader) - Stream Oracle data to Amazon- S3.
- [S3_Sanity_Check] (https://github.com/alexbuz/S3_Sanity_Check/blob/master/README.md) - let's you `ping` Amazon-S3 bucket to see if it's publicly readable.
- [EC2_Metrics_Plotter](https://github.com/alexbuz/EC2_Metrics_Plotter/blob/master/README.md) - plots any CloudWatch EC2 instance  metric stats.
- [S3_File_Uploader](https://github.com/alexbuz/S3_File_Uploader/blob/master/README.md) - uploads file from Windows to S3.

#### Do you have any AWS Certifications?
Yes, [AWS Certified Developer (Associate)](https://raw.githubusercontent.com/alexbuz/FAQs/master/images/AWS_Ceritied_Developer_Associate.png)

#### Can you create similar/custom data tool for our business?
Yes, you can PM me here or email at `alex_buz@yahoo.com`.
I'll get back to you within hours.

###Links
 - [Employment FAQ](https://github.com/alexbuz/FAQs/blob/master/README.md)




