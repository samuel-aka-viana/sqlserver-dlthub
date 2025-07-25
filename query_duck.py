import duckdb

conn = duckdb.connect("mssql_to_duckdb.duckdb")

conn.sql(f"set search_path to 'from_sqlserver'")

table = conn.sql("select * from authors").df()

print(table)
