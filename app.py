import streamlit as st
import pandas as pd

from scraper import scrape_all
from database import (
    create_database,
    save_scholarships,
    get_all_scholarships,
    get_countries,
    get_degree_levels
)

create_database()

st.title("🎓 University Scholarship Finder")

if st.sidebar.button("Refresh Data"):

    data = scrape_all()

    save_scholarships(data)

    st.success(f"{len(data)} scholarships updated")


countries = ["All Countries"] + get_countries()
levels = ["All Levels"] + get_degree_levels()

selected_country = st.sidebar.selectbox(
    "Country",
    countries
)

selected_level = st.sidebar.selectbox(
    "Degree Level",
    levels
)

rows = get_all_scholarships()

columns = [
    "id",
    "title",
    "country",
    "degree_level",
    "deadline",
    "funding_type",
    "source_url",
    "last_scraped"
]

df = pd.DataFrame(rows, columns=columns)

if selected_country != "All Countries":
    df = df[df["country"] == selected_country]

if selected_level != "All Levels":
    df = df[df["degree_level"] == selected_level]

st.subheader(f"{len(df)} scholarships found")

for _, row in df.iterrows():

    st.markdown(f"""
    ### {row['title']}

    **Country:** {row['country']}

    **Degree Level:** {row['degree_level']}

    **Deadline:** {row['deadline']}

    **Funding Type:** {row['funding_type']}

    [Apply Here]({row['source_url']})

    ---
    """)