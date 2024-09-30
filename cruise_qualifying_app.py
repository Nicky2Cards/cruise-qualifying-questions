import streamlit as st

# Placeholder data for cruise lines, resorts, ship size, and excursions based on destination and type
cruise_lines = {
    "Caribbean": {
        "Luxury": ["Celebrity Cruises", "Seabourn", "Regent Seven Seas"],
        "Family-Friendly": ["Disney Cruise Line", "Royal Caribbean", "Carnival"],
        "Adventure": ["Norwegian Cruise Line", "MSC Cruises", "Royal Caribbean"],
        "Romantic Getaway": ["Princess Cruises", "Holland America", "Oceania Cruises"],
        "Group Travel": ["Royal Caribbean", "Carnival", "MSC Cruises"]
    },
    "Mediterranean": {
        "Luxury": ["Regent Seven Seas", "Seabourn", "Silversea Cruises"],
        "Family-Friendly": ["Royal Caribbean", "MSC Cruises", "Norwegian Cruise Line"],
        "Adventure": ["Celebrity Cruises", "Princess Cruises", "Costa Cruises"],
        "Romantic Getaway": ["Viking Cruises", "Holland America", "Oceania Cruises"],
        "Group Travel": ["MSC Cruises", "Norwegian Cruise Line", "Costa Cruises"]
    },
    "Alaska": {
        "Luxury": ["Regent Seven Seas", "Seabourn"],
        "Family-Friendly": ["Princess Cruises", "Royal Caribbean", "Disney Cruise Line"],
        "Adventure": ["Norwegian Cruise Line", "Celebrity Cruises", "Holland America"],
        "Cultural Immersion": ["Princess Cruises", "Holland America"],
        "Group Travel": ["Princess Cruises", "Holland America", "Norwegian Cruise Line"]
    },
    "River": ["Viking River Cruises", "AmaWaterways", "Uniworld", "Avalon Waterways"],
    "Luxury": ["Regent Seven Seas", "Seabourn", "Silversea Cruises", "Oceania Cruises", "Azamara"]
}

resorts = {
    "Caribbean": ["Sandals Resorts", "Club Med", "Riu", "Hyatt Zilara", "Four Seasons"],
    "Europe": ["Marriott", "Four Seasons", "Ritz-Carlton", "Hilton"],
    "Asia": ["Aman Resorts", "Mandarin Oriental", "Shangri-La", "Six Senses"],
    "Luxury": ["Aman Resorts", "Four Seasons", "Ritz-Carlton", "Belmond"]
}

# Function to display client information screen
def client_info_screen():
    st.title("Client Information and Vacation Qualifier")

    # Collecting basic client information
    client_name = st.text_input("Client Name:")
    client_email = st.text_input("Client Email:")
    client_phone = st.text_input("Client Phone Number:")
    
    st.write("## Choose how you'd like to start:")
    
    # Starting point selection
    start_option = st.radio(
        "How would you like to proceed?",
        ("Qualifying Questions", "Direct Selection (if client already has a preference)")
    )
    
    if start_option == "Qualifying Questions":
        qualifying_flow(client_name, client_email, client_phone)
    elif start_option == "Direct Selection (if client already has a preference)":
        direct_selection(client_name, client_email, client_phone)

# Function to handle the Qualifying Questions Flow
def qualifying_flow(client_name, client_email, client_phone):
    st.header("Qualifying Questions")

    # Step 1: Vacation Type
    vacation_type = st.selectbox(
        "What type of vacation experience are you looking for?",
        ["Cruise", "Land Travel", "River Cruise", "Luxury Cruise", "Group Travel", "Combination"]
    )
    
    if vacation_type:
        # Step 2: Experience Type
        experience_type = st.selectbox(
            f"What kind of {vacation_type.lower()} experience are you hoping for?",
            ["Adventure", "Relaxation", "Cultural Immersion", "Family-Friendly", "Romantic", "Other"]
        )

        # Step 3: Preferred Destination or Region
        destination = st.selectbox("What is your preferred destination or region?", list(cruise_lines.keys()) + list(resorts.keys()))
        
        if destination:
            # Step 4: Based on destination, show specific cruise lines or resorts
            if vacation_type in ["Cruise", "Luxury Cruise", "Group Travel"]:
                matching_cruise_lines = cruise_lines.get(destination, {}).get(experience_type, [])
                if matching_cruise_lines:
                    st.write(f"### Recommended Cruise Lines for {destination} ({experience_type} experience):")
                    for line in matching_cruise_lines:
                        st.markdown(f"- {line}")
                    selected_cruise_line = st.selectbox("Choose a cruise line to view details:", matching_cruise_lines)
                    if selected_cruise_line:
                        display_cruise_details(selected_cruise_line, destination)
                else:
                    st.write(f"No matching cruise lines found for {experience_type} in {destination}.")
            elif vacation_type in ["Land Travel", "Combination"]:
                matching_resorts = resorts.get(destination, [])
                if matching_resorts:
                    st.write(f"### Recommended Resorts for {destination} ({experience_type} experience):")
                    for resort in matching_resorts:
                        st.markdown(f"- {resort}")
                    selected_resort = st.selectbox("Choose a resort to view details:", matching_resorts)
                    if selected_resort:
                        display_resort_details(selected_resort, destination)
                else:
                    st.write(f"No matching resorts found for {experience_type} in {destination}.")
            elif vacation_type == "River Cruise":
                river_lines = cruise_lines.get("River", [])
                if river_lines:
                    st.write(f"### Recommended River Cruise Lines for {destination}:")
                    for line in river_lines:
                        st.markdown(f"- {line}")
                    selected_river_line = st.selectbox("Choose a river cruise line to view details:", river_lines)
                    if selected_river_line:
                        display_cruise_details(selected_river_line, "River")
                else:
                    st.write("No matching river cruise lines found.")

# Function to handle Direct Selection Flow
def direct_selection(client_name, client_email, client_phone):
    st.header("Direct Selection")

    # Step 1: Search or Select Direct Options
    st.write("Use the search bar or select from the list below to jump directly to a destination or provider:")
    direct_search = st.text_input("Search for a destination or provider (e.g., ‘Caribbean,’ ‘Royal Caribbean,’ ‘Sandals’):")
    
    # Step 2: Display matching options
    if direct_search:
        # Correctly flatten all cruise line names from the nested dictionary structure
        all_cruise_lines = [
            cruise
            for destination, experience_types in cruise_lines.items()
            for experience_type, cruises in experience_types.items()
            for cruise in cruises
        ]
        matching_cruises = [line for line in all_cruise_lines if direct_search.lower() in line.lower()]
        matching_resorts = [resort for resort in sum(resorts.values(), []) if direct_search.lower() in resort.lower()]

        if matching_cruises:
            st.write("### Matching Cruise Lines:")
            for cruise in matching_cruises:
                st.markdown(f"- {cruise}")
        if matching_resorts:
            st.write("### Matching Resorts:")
            for resort in matching_resorts:
                st.markdown(f"- {resort}")
    
    # Step 3: Direct selection
    direct_selection_type = st.selectbox("Select the type of option to view:", ["Cruise Line", "Resort"])
    if direct_selection_type == "Cruise Line":
        # Correctly flatten all cruise line names
        all_cruise_lines = [
            cruise
            for destination, experience_types in cruise_lines.items()
            for experience_type, cruises in experience_types.items()
            for cruise in cruises
        ]
        selected_cruise = st.selectbox("Select a cruise line:", all_cruise_lines)
        if selected_cruise:
            display_cruise_details(selected_cruise, "Direct Selection")
    elif direct_selection_type == "Resort":
        selected_resort = st.selectbox("Select a resort:", sum(resorts.values(), []))
        if selected_resort:
            display_resort_details(selected_resort, "Direct Selection")

# Function to display details for selected cruise line
def display_cruise_details(cruise_line, destination):
    st.subheader(f"Details for {cruise_line}")
    st.write(f"**Destination**: {destination}")
    st.write(f"**Ship Size**: Medium to Large")
    st.write(f"**Known Activities**: Specialty dining, entertainment
    st.write(f"**Known Activities**: Specialty dining, entertainment shows, spas, and more.")
    st.write(f"**Popular Excursions**: Island tours, adventure sports, cultural experiences.")

# Function to display details for selected resort
def display_resort_details(resort, destination):
    st.subheader(f"Details for {resort}")
    st.write(f"**Destination**: {destination}")
    st.write(f"**Resort Size**: Medium to Large")
    st.write(f"**Known Amenities**: Swim-up bars, golf courses, fine dining, beach access.")
    st.write(f"**Popular Activities**: Water sports, cultural tours, guided excursions.")

# Run the client info screen function to start the app
client_info_screen()
