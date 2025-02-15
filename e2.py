#!/usr/bin/env python3
import os
from funtion_tasks import (
    fetch_data_from_api_and_save,
    clone_git_repo_and_commit,
    run_sql_query_on_database,
    scrape_webpage,
    compress_image,
    transcribe_audio,
    convert_markdown_to_html,
    filter_csv,
)

# --- Task B3: Fetch data from an API and save it ---
def eval_fetch_data():
    # Using a sample public API for demonstration
    url = "https://jsonplaceholder.typicode.com/todos/1"
    output_file = "/data/fetched_data.json"
    generated_prompt = "Fetch sample API data and save it to a file"
    fetch_data_from_api_and_save(url, output_file, generated_prompt)
    print("Fetched data saved to", output_file)

# --- Task B4: Clone a git repo and make a commit ---
def eval_clone_git():
    # This example uses a public repository URL.
    # Adjust the repo_url and output_dir as needed.
    repo_url = "https://github.com/octocat/Hello-World.git"
    output_dir = "/data/cloned_repo"
    commit_message = "Automated commit from eval script"
    clone_git_repo_and_commit(repo_url, output_dir, commit_message)
    print("Cloned repo to", output_dir)

# --- Task B5: Run a SQL query on a SQLite or DuckDB database ---
def eval_sql_query():
    # Ensure that /data/sample.db exists and has a table named 'sample_table'
    database_file = "/data/sample.db"
    query = "SELECT COUNT(*) FROM sample_table;"
    output_file = "/data/query_result.txt"
    # Using SQLite here; set is_sqlite=False if using DuckDB.
    run_sql_query_on_database(database_file, query, output_file, is_sqlite=True)
    print("SQL query result saved to", output_file)

# --- Task B6: Extract data from (i.e. scrape) a website ---
def eval_scrape():
    # Use a safe, publicly accessible website for scraping.
    url = "https://example.com"
    output_file = "/data/scraped_content.html"
    scrape_webpage(url, output_file)
    print("Scraped content saved to", output_file)

# --- Task B7: Compress or resize an image ---
def eval_compress_image():
    # Ensure /data/sample_image.jpg exists. This function will create a compressed copy.
    input_file = "/data/sample_image.jpg"
    output_file = "/data/compressed_image.jpg"
    quality = 50  # Adjust quality as desired
    compress_image(input_file, output_file, quality)
    print("Compressed image saved to", output_file)

# --- Task B8: Transcribe audio from an MP3 file ---
def eval_transcribe_audio():
    # Ensure /data/sample_audio.mp3 exists.
    input_file = "/data/sample_audio.mp3"
    output_file = "/data/transcription.txt"
    transcribe_audio(input_file, output_file)
    print("Audio transcription saved to", output_file)

# --- Task B9: Convert Markdown to HTML ---
def eval_convert_md_to_html():
    # Ensure /data/sample.md exists.
    input_file = "/data/sample.md"
    output_file = "/data/sample.html"
    convert_markdown_to_html(input_file, output_file)
    print("Markdown converted to HTML and saved to", output_file)

# --- Task B10: Write an API endpoint that filters a CSV file and returns JSON data ---
def eval_filter_csv():
    # Ensure /data/sample.csv exists and contains a header with a column 'status'
    input_file = "/data/sample.csv"
    column = "status"
    value = "active"
    output_file = "/data/filtered.json"
    filter_csv(input_file, column, value, output_file)
    print("Filtered CSV saved to", output_file)

if __name__ == "__main__":
    # For evaluation, you can call any or all tasks here.
    # Ensure that the sample data (e.g. /data/sample.db, /data/sample_image.jpg, etc.) exists or adjust paths.
    try:
        eval_fetch_data()
    except Exception as e:
        print("eval_fetch_data failed:", e)

    try:
        eval_clone_git()
    except Exception as e:
        print("eval_clone_git failed:", e)

    try:
        eval_sql_query()
    except Exception as e:
        print("eval_sql_query failed:", e)

    try:
        eval_scrape()
    except Exception as e:
        print("eval_scrape failed:", e)

    try:
        eval_compress_image()
    except Exception as e:
        print("eval_compress_image failed:", e)

    try:
        eval_transcribe_audio()
    except Exception as e:
        print("eval_transcribe_audio failed:", e)

    try:
        eval_convert_md_to_html()
    except Exception as e:
        print("eval_convert_md_to_html failed:", e)

    try:
        eval_filter_csv()
    except Exception as e:
        print("eval_filter_csv failed:", e)