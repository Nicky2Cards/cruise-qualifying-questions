import streamlit as st

# Function to define the qualifying questions flow
def run_qualifying_questions():
    st.title("Cruise Qualifying Questions")

    # Step 1: Initial Question - Travel Destination or Region
    region = st.selectbox("What is your ideal travel destination or region?",
                          ["Select an option", "Caribbean", "Mediterranean/Greek Isles", "Alaska",
                           "Northern Europe/Scandinavia/Baltic", "Asia/South Pacific", 
                           "River Cruises (Europe, Mississippi, etc.)", "Other/Not Sure Yet"])
    
    if region == "Caribbean":
        # Step 2: Caribbean - Type of Experience
        caribbean_experience = st.selectbox("What type of experience are you looking for in the Caribbean?",
                                            ["Select an option", "Relaxing beach vacation", "Adventure", 
                                             "Cultural exploration", "Family-friendly activities"])
        if caribbean_experience != "Select an option":
            # Step 3: Caribbean - Length of Cruise
            caribbean_length = st.selectbox("How long would you like your cruise to be?",
                                            ["Select an option", "3-5 days", "6-8 days", "9+ days"])
            if caribbean_length != "Select an option":
                # Step 4: Caribbean - Specific Islands
                caribbean_islands = st.multiselect("Are there any specific islands you’d like to visit?",
                                                   ["Bahamas", "St. Thomas", "Aruba", "Jamaica", "Cozumel", "Other"])
                st.write(f"Based on your choices, you're interested in a {caribbean_length} Caribbean cruise focusing on {caribbean_experience.lower()} experiences.")
                
    elif region == "Mediterranean/Greek Isles":
        # Step 2: Mediterranean - Focus
        mediterranean_focus = st.selectbox("Are you looking for a cruise focused on historical sites and cultural experiences, or more on leisure and relaxation?",
                                           ["Select an option", "Historical and cultural", "Leisure and relaxation", "A mix of both"])
        if mediterranean_focus != "Select an option":
            # Step 3: Mediterranean - Regions
            mediterranean_regions = st.multiselect("Which regions are you most interested in?",
                                                   ["Greek Isles", "Italian coast", "French Riviera", "Spanish Coast", "Turkish Coast"])
            if mediterranean_regions:
                # Step 4: Mediterranean - Port Style
                mediterranean_port_style = st.selectbox("Do you prefer cruises that visit many ports with shorter stays, or fewer ports with more time in each location?",
                                                        ["Select an option", "Many ports", "Fewer ports with longer stays"])
                st.write(f"You're interested in exploring {', '.join(mediterranean_regions)} in a {mediterranean_focus.lower()} style.")

    elif region == "Alaska":
        # Step 2: Alaska - Attraction Focus
        alaska_focus = st.selectbox("What draws you to Alaska?",
                                    ["Select an option", "Scenery and wildlife", "Adventure activities", "Native culture and history"])
        if alaska_focus != "Select an option":
            # Step 3: Alaska - Land Tour
            alaska_land_tour = st.radio("Would you prefer a cruise that includes a land tour (e.g., Denali National Park) before or after the cruise?",
                                        ["Yes", "No"])
            if alaska_land_tour:
                # Step 4: Alaska - Activities
                alaska_activities = st.multiselect("Are there specific activities you want to experience in Alaska?",
                                                   ["Glacier viewing", "Whale watching", "Hiking", "Native cultural tours"])
                st.write(f"You're looking for an Alaskan adventure focused on {alaska_focus.lower()}, including activities like {', '.join(alaska_activities)}.")

# Run the app
run_qualifying_questions()
