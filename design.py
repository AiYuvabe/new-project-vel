import streamlit as st
import requests

# Set Streamlit page config
st.set_page_config(
    page_title="World Population Dashboard",
    page_icon="🌍",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000"

st.title("🌍 World Population Dashboard")
st.subheader("Get insights into global population statistics")

# Continent selection
continents = ["Asia", "Africa", "Europe", "North America", "South America", "Australia", "Antarctica"]
selected_continent = st.selectbox("🌎 Select a Continent", continents)

if selected_continent:
    try:
        # Fetch general population stats
        response = requests.get(f"{API_URL}/{selected_continent}")
        max_pop_resp = requests.get(f"{API_URL}/continent/{selected_continent}/max_population_country")
        min_pop_resp = requests.get(f"{API_URL}/continent/{selected_continent}/min_population_country")
        avg_pop_resp = requests.get(f"{API_URL}/continent/{selected_continent}/avg_population_country")

        if response.status_code == 200:
            stats = response.json()
            max_data = max_pop_resp.json() if max_pop_resp.status_code == 200 else {}
            min_data = min_pop_resp.json() if min_pop_resp.status_code == 200 else {}
            avg_data = avg_pop_resp.json() if avg_pop_resp.status_code == 200 else {}

            st.write("### 🌟 Overall Continent Population Stats")
            st.write(f"📈 **Max Population:** {stats['max_population']:,}")
            st.write(f"📉 **Min Population:** {stats['min_population']:,}")
            st.write(f"📊 **Avg Population:** {stats['avg_population']:,}")

            st.write("---")

            # Max Population Country
            if max_data:
                st.success(f"📈 **Most Populated Country:** {max_data['country']} ({max_data['max_population']:,})")

            # Min Population Country
            if min_data:
                st.warning(f"📉 **Least Populated Country:** {min_data['country']} ({min_data['min_population']:,})")

            # Avg Population Country
            if avg_data:
                st.info(f"📊 **Closest to Avg Population:** {avg_data['country']} ({avg_data['max_population']:,})")

        else:
            st.error("⚠️ Failed to fetch population data.")

    except requests.RequestException as e:
        st.error(f"❌ API Request Failed: {e}")
