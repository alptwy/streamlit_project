import streamlit as st
from PIL import Image

# "Methodology" Page
def main():
    st.set_page_config(page_title="Methodology", layout="wide")
    st.title("Methodology")

    # Load icons (optional)
    data_flow_icon = Image.open('./images/data_flow_icon.png')
    process_icon = Image.open('./images/process_icon.png')
    summary_icon = Image.open('./images/summary_icon.png')

    # Sidebar navigation with icons (optional)
    st.sidebar.title("Navigation")
    st.sidebar.markdown("**Select a section to explore more**")
    section = st.sidebar.selectbox("Go to Section", [
        "Data Flow and Implementation Details", 
        "Process Flow Diagrams", 
        "Summary of Methodology"
    ])

    if section == "Data Flow and Implementation Details":
        st.header("Data Flow and Implementation Details")
        st.image(data_flow_icon, width=50)
        with st.expander("Detailed Overview of Data Flow", expanded=True):
            st.write(
                """
                The "Health Buddy" application is built to ensure seamless access to health and wellness activities, leveraging data-driven insights to enhance the user experience. The methodology behind "Health Buddy" focuses on effective data processing, visualization, and user interactivity to provide a comprehensive solution for community fitness activities.
                
                **Data Flow Overview**
                
                1. **Data Acquisition**: Data is sourced from trusted health organizations, including the Health Promotion Board and local community centers. The data includes details such as activity type, location, schedule, and other relevant information.
                
                2. **Data Preprocessing**: Once acquired, the data undergoes preprocessing to ensure accuracy, consistency, and reliability. This involves:
                   - **Normalization**: Standardizing the data format to ensure consistency across all records (e.g., standardizing venue names, activity titles).
                   - **Data Cleaning**: Removing duplicate entries, handling missing values, and verifying data accuracy.
                   - **Data Enrichment**: Adding additional attributes or metadata to enhance the user experience, such as adding geolocation coordinates for mapping purposes.
                
                3. **Data Storage**: The processed data is stored in a JSON format, which allows for easy retrieval and updates. JSON is chosen for its simplicity and compatibility with web technologies, enabling efficient data exchange between the server and the front-end application.
                
                4. **Data Presentation**: The processed data is presented to users through various visual and interactive tools, such as tables, heatmaps, and geographical maps. The application leverages Python libraries such as Pandas, Seaborn, Matplotlib, and Folium to provide these functionalities.
                """
            )
        
        with st.expander("Implementation Details", expanded=False):
            st.write(
                """
                - **Front-End Interface**: The front-end of "Health Buddy" is built using Streamlit, a powerful Python framework for creating interactive web applications. Streamlit enables rapid prototyping and allows for a highly interactive user experience.
                
                - **Filtering and User Interaction**: Users can filter activities based on parameters such as activity type, venue, and schedule. The filtering mechanism is implemented using Pandas to efficiently query the data and return results in real time.
                
                - **Visualizations**: The platform offers a variety of visual representations to make data more understandable and engaging for users:
                  - **Heatmaps**: Created using Seaborn, heatmaps show the frequency of activities across different venues, helping users identify popular locations and times.
                  - **Geographical Maps**: Using Folium, the platform provides an interactive map that shows where each activity is located. Users can click on markers to view more details about specific activities.
                
                - **Data Update Mechanism**: To ensure that users have access to the most up-to-date information, the platform includes a mechanism for periodic data updates. This ensures that any changes in activity schedules or venues are promptly reflected on the platform.
                """
            )
        
        with st.expander("Technology Stack", expanded=False):
            st.write(
                """
                - **Programming Language**: Python is used for both the back-end processing and the front-end user interface, allowing for streamlined development and maintenance.
                - **Data Handling**: Pandas is used extensively for data manipulation, ensuring that data is efficiently processed and filtered based on user inputs.
                - **Visualization Libraries**: Seaborn and Matplotlib are used for creating visual representations of the data, while Folium is used for geographical mapping.
                - **Web Framework**: Streamlit provides the front-end interface, offering an easy way to create web applications directly from Python scripts.
                """
            )

    elif section == "Process Flow Diagrams":
        st.header("Process Flow Diagrams")
        st.image(process_icon, width=50)
        st.write("Below are the flowcharts representing different use cases of the application, providing a visual overview of the processes involved:")
        
        st.subheader("Flowchart 1: Chat with Information")
        with st.expander("Chat Process Overview", expanded=True):
            st.write(
                """
                This flowchart illustrates how users interact with the platform to obtain information through a conversational interface:
                
                - **User Input**: The user enters a query or prompt regarding available fitness activities.
                - **Processing**: The system processes the prompt using a language model to understand the user's intent and identify relevant activities.
                - **Response Generation**: Based on the identified activity or information request, a response is generated and displayed to the user, providing relevant details or suggestions.
                
                This process ensures that users can quickly obtain information in a conversational manner, enhancing accessibility and ease of use.
                """
            )
            # Uncomment the line below if the image is available
            st.image("./images/flowchart1_icon.png", caption="Chat with Information Flowchart")
        
        st.subheader("Flowchart 2: Intelligent Search")
        with st.expander("Intelligent Search Overview", expanded=True):
            st.write(
                """
                The intelligent search functionality allows users to explore fitness activities based on specific criteria:
                
                - **User Selection**: The user selects filters such as exercise type or location to narrow down the list of available activities.
                - **Filtering Process**: The platform processes the user's selection by querying the dataset to filter out relevant activities.
                - **Output Display**: The filtered activities are then displayed in various formats, including interactive tables, maps, and visual summaries, allowing users to explore the results in a way that suits their preferences.
                
                This process ensures that users can efficiently find activities that match their interests and availability.
                """
            )
            # Uncomment the line below if the image is available
            st.image("./images/flowchart2_icon.png", caption="Intelligent Search Flowchart")

    elif section == "Summary of Methodology":
        st.header("Summary of Methodology")
        st.image(summary_icon, width=50)
        with st.expander("Overview of Health Buddy Methodology", expanded=True):
            st.write(
                """
                The "Health Buddy" platform is built upon a robust data-driven methodology that ensures accurate, reliable, and engaging access to community fitness activities. By leveraging advanced data processing, intuitive visualizations, and interactive features, the platform aims to:
                
                - **Simplify the Discovery of Fitness Activities**: Ensure that users can easily find fitness activities available in their locality.
                - **Provide an Engaging User Experience**: Use interactive tools and visualizations to keep users engaged and motivated to explore available activities.
                - **Support Community Health Initiatives**: Make physical activities more accessible, thereby contributing to better community health and wellness outcomes.
                
                The combination of data accuracy, effective visual tools, and user-friendly navigation helps make "Health Buddy" a valuable resource for anyone looking to improve their physical well-being and engage with their local community.
                """
            )

if __name__ == "__main__":
    main()
