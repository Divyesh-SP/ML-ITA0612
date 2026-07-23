import streamlit as st

from ionosphere import estimate_virtual_height
from geolocation import locate_transmitter

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="HF Geolocation Software",
    page_icon="📡",
    layout="wide"
)

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.title("📡 HF Geolocation")

st.sidebar.markdown("""
## Project Details

**Technology Category**
- COMINT

**Thrust Area**
- Electronic Warfare

### Objective
Estimate the location of a distant HF transmitter using:

- Frequency
- Azimuth Bearing
- Elevation Bearing
- Ionosospheric Virtual Height
""")

# ---------------------------------
# Title
# ---------------------------------
st.title("📡 Single Station HF Geolocation Software")

st.write("Estimate the location of an HF transmitter using a Single Station HF Direction Finding Algorithm.")

st.markdown("---")

# ---------------------------------
# Inputs
# ---------------------------------
col1, col2 = st.columns(2)

with col1:
    frequency = st.number_input(
        "Frequency (MHz)",
        min_value=1.0,
        max_value=30.0,
        value=12.54,
        format="%.2f"
    )

    azimuth = st.number_input(
        "Azimuth (Degrees)",
        min_value=0.0,
        max_value=360.0,
        value=60.0,
        format="%.2f"
    )

with col2:
    elevation = st.number_input(
        "Elevation (Degrees)",
        min_value=1.0,
        max_value=89.0,
        value=30.0,
        format="%.2f"
    )

    station_lat = st.number_input(
        "Station Latitude",
        value=13.08,
        format="%.6f"
    )

station_lon = st.number_input(
    "Station Longitude",
    value=80.27,
    format="%.6f"
)

st.markdown("")

# ---------------------------------
# Estimate Button
# ---------------------------------
if st.button("🚀 Estimate Location", use_container_width=True):

    # Calculate virtual height
    virtual_height = estimate_virtual_height(frequency)

    # Calculate transmitter location
    result = locate_transmitter(
        station_lat,
        station_lon,
        azimuth,
        elevation,
        virtual_height
    )

    st.success("✅ Location Estimated Successfully!")

    st.markdown("---")

    st.subheader("📊 Estimated Results")

    colA, colB = st.columns(2)

    with colA:
        st.metric(
            "Virtual Height",
            f"{virtual_height} km"
        )

        st.metric(
            "Estimated Latitude",
            f"{result['latitude']}"
        )

    with colB:
        st.metric(
            "Ground Distance",
            f"{result['distance']} km"
        )

        st.metric(
            "Estimated Longitude",
            f"{result['longitude']}"
        )

    st.markdown("---")

    st.subheader("📍 Estimated Coordinates")

    st.code(f"""
Latitude  : {result['latitude']}
Longitude : {result['longitude']}
Ground Distance : {result['distance']} km
Virtual Height : {virtual_height} km
""")

    # Google Maps
    google_maps = (
        f"https://www.google.com/maps?q="
        f"{result['latitude']},{result['longitude']}"
    )

    st.link_button(
        "🌍 Open Estimated Location in Google Maps",
        google_maps
    )

    st.markdown("---")

    st.subheader("📡 Signal Flow")

    st.info("""
HF Signal
      ↓
Ionospheric Reflection
      ↓
Virtual Height Estimation
      ↓
Geolocation Algorithm
      ↓
Estimated Transmitter Location
""")

    st.markdown("---")

    st.subheader("📋 Summary")

    summary = {
        "Frequency (MHz)": frequency,
        "Azimuth (°)": azimuth,
        "Elevation (°)": elevation,
        "Station Latitude": station_lat,
        "Station Longitude": station_lon,
        "Virtual Height (km)": virtual_height,
        "Ground Distance (km)": result["distance"],
        "Estimated Latitude": result["latitude"],
        "Estimated Longitude": result["longitude"]
    }

    st.json(summary)

st.markdown("---")
st.caption("© 2026 HF Geolocation Software | Hackathon Prototype")