# IMDb Movie Metadata Fetcher

This Python script enriches a local dataset of movie titles by fetching metadata from the [IMDb API](https://rest.imdbapi.dev/). It processes each movie title and appends the resulting data to a CSV file.

---

## 📂 Overview

- Reads movie titles from `movies.csv` (up to 10,000 rows).
- Sends requests to the IMDb API to search for each title.
- Extracts and saves metadata from the first search result.
- Appends data to `imdb.csv`.
- Includes rate-limiting (15-second delay every 7 requests).
- Logs and skips failed requests without stopping the script.

---

## 📄 File Structure

| File         | Description                                       |
|--------------|---------------------------------------------------|
| `movies.csv` | Input file containing a list of movie titles.     |
| `imdb.csv`   | Output file where fetched IMDb data is stored.    |
| `main.py`    | Main script that runs the fetching process.       |

---

## 🚀 How It Works

1. **Reads Input**  
   The script reads up to 10,000 titles from `movies.csv`, using only the `title` column.

2. **Fetches Metadata**  
   For each title, a GET request is made to the IMDb API (`/search/titles?query=...`). The first result is used.

3. **Appends Data**  
   Metadata is appended to `imdb.csv`. The file includes a header if it doesn’t already exist.

4. **Rate Limiting**  
   After every 7 requests, the script pauses for 15 seconds to avoid hitting API limits.

5. **Error Handling**  
   If the request fails or data is missing, the error is printed and the script continues with the next title.

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install pandas requests
