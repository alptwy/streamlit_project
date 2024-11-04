import streamlit as st
from PIL import Image

# "About Us" Page
def main():
    st.set_page_config(page_title="About Us", layout="wide")
    st.title("About Us")

    # Load icons (optional)
    scope_icon = Image.open('./images/scope_icon.png')
    problem_icon = Image.open('./images/problem_icon.png')
    data_icon = Image.open('./images/data_icon.png')
    feature_icon = Image.open('./images/feature_icon.png')

    # Sidebar navigation with icons (optional)
    st.sidebar.title("Navigation")
    st.sidebar.markdown("**Select a section to explore more**")
    section = st.sidebar.selectbox("Go to Section", [
        "Project Scope and Objectives", 
        "Problems the Project is Solving", 
        "Data Sources", 
        "Features"
    ])

    if section == "Project Scope and Objectives":
        st.header("Project Scope and Objectives")
        st.image(scope_icon, width=50)
        with st.expander("Detailed Project Scope and Objectives", expanded=True):
            st.write(
                """
                **Project Scope**
                
                The "Health Buddy" project is an innovative digital platform designed to centralize and simplify access to health and wellness activities within the community. It provides users with comprehensive information on a variety of workout activities available across different participating malls in the region. By offering an accessible and engaging platform, "Health Buddy" aims to become a one-stop solution for individuals seeking to maintain an active lifestyle through mall-based community fitness programs.
                
                This project aims to bridge the gap between public health initiatives and community engagement by ensuring that everyone, regardless of age or fitness level, has the opportunity to participate in health-promoting activities. By leveraging digital tools and user-friendly interfaces, "Health Buddy" seeks to enhance public health outcomes by fostering a supportive environment where physical activity is encouraged and easily accessible.
                
                **Objectives**
                
                The primary objectives of the "Health Buddy" project are as follows:
                
                - **Increase Awareness**: To raise awareness about fitness activities available in local malls, making it easier for community members to find and join these activities.
                - **Enhance Accessibility**: To provide an intuitive and easy-to-use interface where users can explore, filter, and view workout schedules based on their preferences such as activity type, location, and time.
                - **Encourage Community Participation**: To motivate individuals to participate in physical activities by providing engaging and interactive visualizations, making the discovery of local activities more appealing.
                - **Promote Community Well-Being**: To foster a fitness-oriented environment within community spaces, contributing to the overall well-being and social cohesion of the community.
                - **Support Public Health Initiatives**: To align with public health goals by promoting regular physical activity and providing accessible opportunities for exercise in public spaces.
                
                "Health Buddy" is committed to making fitness an integral part of daily life for everyone in the community by providing accurate, accessible, and engaging information.
                """
            )

    elif section == "Problems the Project is Solving":
        st.header("Problems the Project is Solving")
        st.image(problem_icon, width=50)
        with st.expander("Challenges Addressed by Health Buddy", expanded=True):
            st.write(
                """
                Despite the growing awareness of the importance of physical fitness, many individuals face significant barriers when trying to find and participate in local fitness activities. "Health Buddy" addresses the following key challenges:
                
                - **Lack of Awareness**: Many community members are unaware of the free or low-cost workout opportunities available in their vicinity. By providing a detailed and up-to-date schedule of all mall-based workout activities, "Health Buddy" empowers users to discover and participate in activities that suit their preferences and schedules.
                
                - **Fragmented Information**: Information about local fitness events is often scattered across various sources, making it difficult for individuals to find relevant activities. "Health Buddy" consolidates this information into a single, easy-to-use platform, thus reducing the effort required to stay informed about local fitness opportunities.
                
                - **Limited Engagement**: A lack of motivation or interest often prevents people from taking part in physical activities. By offering interactive tools such as heatmaps and geographical maps, "Health Buddy" aims to make the discovery process more engaging and visually appealing, encouraging users to take that first step towards a healthier lifestyle.
                
                - **Difficulty in Planning**: For those interested in maintaining an active lifestyle, planning fitness activities around a busy schedule can be challenging. The platform's intuitive filtering options allow users to easily find activities that fit their personal timetable, ensuring that fitness becomes a part of their regular routine.
                
                - **Community Disconnection**: Many individuals miss out on opportunities to connect with others through group activities. "Health Buddy" fosters a sense of community by making group fitness activities more accessible, thereby encouraging social interaction and community building.
                
                "Health Buddy" strives to eliminate these barriers, ensuring that fitness and wellness are within reach for everyone.
                """
            )

    elif section == "Data Sources":
        st.header("Data Sources")
        st.image(data_icon, width=50)
        with st.expander("Sources of Data Utilized by Health Buddy", expanded=True):
            st.write(
                """
                The data used in "Health Buddy" is sourced from a variety of trusted public health and wellness organizations, including the Health Promotion Board and local community centers. These data sources ensure that the platform provides users with reliable, up-to-date, and comprehensive information regarding the available fitness activities.
                
                The key components of the data include:
                
                - **Activity Type**: Information on the types of workout activities available, such as Yoga, Zumba, Kickboxing, Tai Chi, etc. Each activity type is categorized to help users quickly find the workouts that best suit their interests and fitness levels.
                
                - **Venue Information**: Details about the participating malls, including the specific unit or location within each mall where the activities take place. This helps users navigate to the correct spot without any hassle.
                
                - **Schedule**: The days and times when each activity is offered, including frequency (e.g., weekly, bi-weekly). This allows users to plan their fitness routines around their personal schedules effectively.
                
                - **Special Instructions**: Any special information related to each activity, such as requirements for registration, age restrictions, or recommended attire.
                
                All data is thoroughly processed and normalized to ensure consistency, allowing users to have a seamless experience while browsing the available activities. Regular updates are also incorporated to reflect any changes in schedules or venue information.
                """
            )

    elif section == "Features":
        st.header("Features")
        st.image(feature_icon, width=50)
        with st.expander("Core Features of the Health Buddy Platform", expanded=True):
            st.write(
                """
                The "Health Buddy" platform offers several key features designed to enhance the user experience and ensure easy access to fitness activities:
                
                - **Interactive Workout Schedule**: Users can filter and view workout activities by activity type, venue, day, and time. This interactive feature ensures that users can quickly find activities that match their preferences and availability. The filtering capabilities are user-friendly, allowing for dynamic exploration of various activities.
                
                - **Heatmap Visualization**: The platform includes a heatmap that visually represents the frequency and distribution of different workout activities across various venues. This feature helps users to identify popular locations and times for fitness activities, giving them insights into trends and availability.
                
                - **Geographical Map**: An integrated map feature provides a geographical view of where different workout activities are being held. Users can click on specific locations to get more information, such as activity details and schedules. The interactive nature of the map makes it easy for users to explore venues and plan their visits.
                
                - **Detailed Activity Summaries**: For each workout activity, users can access expanded details, including venue unit information, schedule specifics, and any other relevant instructions. These summaries ensure that users are well-prepared and informed before attending an activity.
                
                - **User-Friendly Interface**: The platform has been designed with simplicity and usability in mind. Whether users are tech-savvy or new to digital tools, the interface allows for intuitive navigation, ensuring that everyone can benefit from the platform.
                
                - **Community Engagement**: By providing a comprehensive list of group fitness activities, "Health Buddy" fosters community engagement and encourages users to participate in group workouts. This not only helps improve physical health but also enhances social well-being by bringing people together in a supportive environment.
                
                Overall, "Health Buddy" aims to make finding and participating in fitness activities as straightforward as possible, promoting a healthier lifestyle for all users by making physical fitness more accessible, engaging, and community-focused.
                """
            )

if __name__ == "__main__":
    main()
