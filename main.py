import streamlit as st

# Define the pages
page_1 = st.Page("pages/page_1.py", title="Предсказание цены")
page_2 = st.Page("pages/page_2.py", title="Поиск квартир")
page_3 = st.Page("pages/page_3.py", title="Визуализации")

# Set up navigation
pg = st.navigation([page_1, page_2, page_3])

# Run the selected page
pg.run()