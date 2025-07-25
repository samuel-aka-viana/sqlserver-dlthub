import dlt
from dlt.sources.sql_database import sql_database

@dlt.source
def my_source():
    db = sql_database(credentials=dlt.secrets["mssql"])
    return db.with_resources("Authors", "Books")


pipeline = dlt.pipeline(
    pipeline_name="mssql_to_duckdb",
    destination="duckdb",
    dataset_name="from_sqlserver"
)

info = pipeline.run(my_source())
print(info)

