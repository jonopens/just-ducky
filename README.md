## uv, DuckDB & Marimo

I saw Marimo on HN recently and wanted to try it out. I'm also testing out uv because I want it to succeed + it sounds rad.

If you want to do basically the exact same thing I just did, try the following steps:

1. `mkdir some-such` and then `cd some-such` into it
2. get you some duckdb, I used brew: `brew install duckdb`
  - now go get some data to use - I used some NYC Yellow cab parquet files from here: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
  - run `duckdb taxis.db` (or whatever filename) to make an empty database and write some queries from terminal; we want to make a table and import the parquet files
  - you should see `taxis D`
  - run `CREATE TABLE trips AS SELECT * FROM read_parquet('yellow_tripdata_2024-*.parquet');`
  - try to `select COUNT(*) FROM trips;` to confirm it's all in there
  - great, we got a lil data, you can also run `duckdb taxis.db -ui` to start a localhost to fiddle around with more queries in your brand-spankin' new dataset
3. run `uv init` in the new directory to start a new project (or something else if you're not into `uv`)
4. run `uv add "marimo[sql]" "polars[pyarrow]"` to add a couple more dependencies
5. I also had to run `uv add pandas` but I wondered if that was an issue with what I wrote; YMMV
6. now run `uvx marimo edit a-name-you-want.py` to create the notebook and open a localhost
7. write some python and enjoy your new notebook using `duckdb`, `marimo` and `uv` - celebrate!