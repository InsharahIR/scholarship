\# 🎓 University Scholarship Finder



Build a Streamlit dashboard that scrapes real scholarship listings, stores them in a local SQLite database, and allows users to filter and explore scholarships through a simple web interface.



\---



\## Objective



Create a complete Python application that:



\* Scrapes scholarship opportunities from multiple websites.

\* Stores and updates scholarship records in SQLite.

\* Provides a Streamlit dashboard for browsing and filtering opportunities.

\* Supports refreshing data directly from the dashboard.



\---



\## Data Sources



Scrape scholarship listings from:



1\. \[https://brightscholarship.com/](https://brightscholarship.com/)

2\. \[https://opportunitiescorners.com/](https://opportunitiescorners.com/)



The HTML structure, listing pages, and pagination must be discovered by inspecting the websites using browser DevTools.



Do not use unofficial APIs or manually created datasets.



\---



\## Tech Stack



\### Required



\* Python 3.11+

\* Streamlit

\* Requests

\* BeautifulSoup4

\* SQLite (sqlite3)

\* Pandas



\### Installation



```bash

pip install streamlit requests beautifulsoup4 pandas

```



\---



\## Project Structure



```text

scholarship\_finder/



├── app.py

├── scraper.py

├── database.py

├── scholarships.db

├── requirements.txt

└── README.md

```



\---



\# 1. Scraper (`scraper.py`)



Implement a scraper that collects scholarship opportunities from both websites.



\### Requirements



\* Use `requests` and `BeautifulSoup`.

\* Scrape all available pages through pagination.

\* Extract the following information from each scholarship listing:



```text

Title

Country

Degree Level

Deadline

Funding Type

Source URL

```



\### Functions



Provide functions that:



```python

scrape\_brightscholarship()

scrape\_opportunitiescorners()

```



And a master function:



```python

scrape\_all()

```



that combines data from all sources.



\### Notes



\* Handle missing values gracefully.

\* Skip invalid records.

\* Avoid crashing if one source temporarily fails.



\---



\# 2. Database (`database.py`)



Store scholarship records in SQLite.



\### Database Requirements



Use the built-in `sqlite3` module.



\### Suggested Table Structure



```sql

CREATE TABLE scholarships (

&#x20;   id INTEGER PRIMARY KEY AUTOINCREMENT,

&#x20;   title TEXT,

&#x20;   country TEXT,

&#x20;   degree\_level TEXT,

&#x20;   deadline TEXT,

&#x20;   funding\_type TEXT,

&#x20;   source\_url TEXT UNIQUE,

&#x20;   last\_scraped TEXT

);

```



\### Requirements



\* Create the database automatically if it does not exist.

\* Prevent duplicate records.

\* If a scholarship already exists, update the existing record instead of inserting a duplicate.

\* Track the timestamp of the latest scrape using:



```text

last\_scraped

```



\### Functions



Examples:



```python

create\_database()

save\_scholarships()

get\_all\_scholarships()

get\_countries()

get\_degree\_levels()

```



\---



\# 3. Streamlit Dashboard (`app.py`)



Create a clean and simple dashboard for browsing scholarships.



\---



\## Sidebar Filters



Provide filters populated dynamically from the database.



\### Country Filter



```text

All Countries

Pakistan

Malaysia

Hungary

Germany

...

```



\### Degree Level Filter



```text

All Levels

Bachelor

Master

PhD

...

```



\---



\## Scholarship Results



Display scholarships as cards containing:



```text

Title

Country

Degree Level

Deadline

Funding Type

Apply Link

```



Each card should include a clickable link to the original scholarship page.



\---



\## Result Count



Display the number of matching scholarships.



Example:



```text

23 scholarships found

```



\---



\## Refresh Data Button



Add a button:



```text

Refresh Data

```



When clicked:



1\. Run all scrapers.

2\. Update the database.

3\. Refresh the displayed results.



\---



\## Sorting



Sort scholarships by deadline.



\### Order



```text

Soonest deadline first

```





\---



✅ Run locally with:



```bash

streamlit run app.py

```



