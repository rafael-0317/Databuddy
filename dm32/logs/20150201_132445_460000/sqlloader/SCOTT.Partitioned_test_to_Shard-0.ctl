UNRECOVERABLE
	LOAD DATA
	APPEND
	INTO TABLE SCOTT.Partitioned_test_to 
	FIELDS TERMINATED BY '|'
	TRAILING NULLCOLS
	(ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED)