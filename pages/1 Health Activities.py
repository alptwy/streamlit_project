import streamlit as st
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
from PIL import Image

# Load the workout data from the JSON file
def load_workout_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Streamlit App to display the workout data
def main():
    st.set_page_config(layout="wide")
    st.title("Mall Workout Schedule")
    st.write("This page displays the mall workout schedule with a filterable table, heatmap, and a geographical layout.")

    # Load data
    json_path = "./data/mall_workout_schedule.json"
    data = load_workout_data(json_path)

    # Normalize venue names in the dataset
    data['Venue'] = data['Venue'].str.strip().str.title()

    # Sidebar filters
    st.sidebar.header("Filter Options")
    activities = st.sidebar.multiselect("Select Activity", options=data['Activity'].unique(), default=data['Activity'].unique())
    venues = st.sidebar.multiselect("Select Venue", options=data['Venue'].unique(), default=data['Venue'].unique())

    # Apply filters
    filtered_data = data[(data['Activity'].isin(activities)) & (data['Venue'].isin(venues))]

    # Create layout with columns
    col1, col2 = st.columns([3, 2])

    # Display filtered data in col1
    with col1:
        st.write("### Filtered Workout Schedule")
        st.dataframe(filtered_data)

    # Display heat map of activity frequency in col1
    with col1:
        st.write("### Heat Map of Workout Activities by Venue")
        if not filtered_data.empty:
            pivot_data = filtered_data.pivot_table(index='Venue', columns='Activity', aggfunc='size', fill_value=0)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(pivot_data, annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
            plt.title("Activity Frequency by Venue")
            st.pyplot(fig)
        else:
            st.write("No data available for the selected filters.")

    # Display map layout of venues in col2
    with col2:
        map_center = [1.3521, 103.8198]  # Coordinates for Singapore
        workout_map = folium.Map(location=map_center, zoom_start=11)

        for _, row in filtered_data.iterrows():
            folium.Marker(
                location=[1.3521, 103.8198],  # Placeholder coordinates, replace with actual coordinates if available
                popup=f"{row['Venue']}: {row['Activity']} ({row['Days']} at {row['Time']})",
                tooltip=row['Venue']
            ).add_to(workout_map)

        st_folium(workout_map, width=400, height=450)

    # Additional Cards for Activities
    st.write("### Activities Summary")
    for _, row in filtered_data.iterrows():
        with st.expander(f"{row['Activity']} at {row['Venue']}"):
            st.write(f"**Venue Unit**: {row['Venue Unit']}")
            st.write(f"**Days**: {row['Days']}")
            st.write(f"**Time**: {row['Time']}")

    # Footer Image or Branding (optional)
    st.markdown("---")
    st.write("Brought to you by HealthHub")
    # Uncomment the line below if you have the logo image available
    # image = Image.open('./data/healthhub_logo.png')
    # st.image(image, width=100)

if __name__ == "__main__":
    main()
