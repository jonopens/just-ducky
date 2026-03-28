import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb

    # Connect to a DuckDB database (or create an in-memory one)
    taxis_conn = duckdb.connect("taxis.db")

    # You can use a SQL cell to query dataframes or databases directly
    # In the marimo editor, create a SQL cell by clicking the SQL button
    # The result is automatically stored in a Python variable (e.g., 'df')
    # Example SQL cell content (output variable 'df'):
    # SELECT * FROM your_table_name WHERE condition;

    aggregation_query = """
        SELECT
            DATE_TRUNC('day', tpep_pickup_datetime) AS day,
            COUNT(*)                                AS total_trips,
            ROUND(AVG(trip_distance), 2)            AS avg_distance,
            ROUND(AVG(total_amount), 2)             AS avg_fare
        FROM trips
        WHERE YEAR(day) > 2023
        GROUP BY day
        ORDER BY avg_fare ASC;
    """

    # Or use Python code to run queries and work with the results
    def run_query(connection):
        # Use DuckDB to run a query and get results
        result_df = connection.sql(aggregation_query).fetchdf()
        return mo.ui.table(result_df)

    run_query(taxis_conn)
    return


if __name__ == "__main__":
    app.run()
