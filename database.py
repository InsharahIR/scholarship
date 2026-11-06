import sqlite3
from datetime import datetime

DB_NAME = "scholarships.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS scholarships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            country TEXT,
            degree_level TEXT,
            deadline TEXT,
            funding_type TEXT,
            source_url TEXT UNIQUE,
            last_scraped TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_scholarships(records):
    conn = sqlite3.connect(DB_NAME)

    for item in records:
        conn.execute("""
            INSERT INTO scholarships
            (
                title,
                country,
                degree_level,
                deadline,
                funding_type,
                source_url,
                last_scraped
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(source_url)
            DO UPDATE SET
                title=excluded.title,
                country=excluded.country,
                degree_level=excluded.degree_level,
                deadline=excluded.deadline,
                funding_type=excluded.funding_type,
                last_scraped=excluded.last_scraped
        """, (
            item["title"],
            item["country"],
            item["degree_level"],
            item["deadline"],
            item["funding_type"],
            item["source_url"],
            datetime.now().isoformat()
        ))

    conn.commit()
    conn.close()


def get_all_scholarships():
    conn = sqlite3.connect(DB_NAME)

    rows = conn.execute("""
        SELECT *
        FROM scholarships
        ORDER BY deadline ASC
    """).fetchall()

    conn.close()

    return rows


def get_countries():
    conn = sqlite3.connect(DB_NAME)

    rows = conn.execute("""
        SELECT DISTINCT country
        FROM scholarships
        WHERE country IS NOT NULL
    """).fetchall()

    conn.close()

    return [r[0] for r in rows if r[0]]


def get_degree_levels():
    conn = sqlite3.connect(DB_NAME)

    rows = conn.execute("""
        SELECT DISTINCT degree_level
        FROM scholarships
    """).fetchall()

    conn.close()

    return [r[0] for r in rows if r[0]]