
import streamlit as st
from pt_master_database_v1 import PROTOCOLS

st.set_page_config(
    page_title="PT Protocol Database",
    page_icon="🏋️",
    layout="wide",
)

protocols = PROTOCOLS

st.title("PT Outpatient Protocol Database")
st.caption("Search, filter by body region, and review phase-based rehab protocols.")

# Sidebar controls
st.sidebar.header("Filters")
search = st.sidebar.text_input("Search diagnosis", placeholder="Example: Achilles, ACL, TKA")

body_regions = sorted(
    set(data.get("body_region", "Other") for data in protocols.values())
)
selected_region = st.sidebar.selectbox("Filter by body region", ["All"] + body_regions)

protocol_types = sorted(
    set(data.get("type", "Other") for data in protocols.values())
)
selected_type = st.sidebar.selectbox("Filter by protocol type", ["All"] + protocol_types)

# Filter protocols
filtered_protocols = {
    name: data
    for name, data in protocols.items()
    if search.lower() in name.lower()
    and (selected_region == "All" or data.get("body_region", "Other") == selected_region)
    and (selected_type == "All" or data.get("type", "Other") == selected_type)
}

st.sidebar.write(f"Showing **{len(filtered_protocols)}** of **{len(protocols)}** protocols")

if not filtered_protocols:
    st.warning("No protocols match your search/filter. Try clearing the search box or selecting All.")
    st.stop()

selected_dx = st.selectbox("Select Diagnosis", list(filtered_protocols.keys()))
protocol = filtered_protocols[selected_dx]

# Header info
st.header(selected_dx)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Body Region", protocol.get("body_region", "Not listed"))
with col2:
    st.metric("Type", protocol.get("type", "Not listed"))
with col3:
    st.metric("Duration", protocol.get("duration", "Not listed"))

st.write(f"**Frequency:** {protocol.get('frequency', 'Not listed')}")

# Outcome measures
outcome_measures = protocol.get("outcome_measures", [])
if outcome_measures:
    st.subheader("Outcome Measures")
    st.write(", ".join(outcome_measures))

# Red flags
red_flags = protocol.get("red_flags", [])
if red_flags:
    st.subheader("Red Flags")
    for item in red_flags:
        st.write(f"- {item}")

# Precautions
precautions = protocol.get("precautions", [])
if precautions:
    st.subheader("Precautions")
    for item in precautions:
        st.write(f"- {item}")

# Weeks / phases
weeks = protocol.get("weeks", {})
if weeks:
    st.subheader("Protocol by Phase / Week")
    for phase, items in weeks.items():
        with st.expander(str(phase), expanded=False):
            for item in items:
                st.write(f"- {item}")

# Copyable summary
st.subheader("Quick Summary")
summary_lines = [
    f"Diagnosis: {selected_dx}",
    f"Body Region: {protocol.get('body_region', 'Not listed')}",
    f"Type: {protocol.get('type', 'Not listed')}",
    f"Frequency: {protocol.get('frequency', 'Not listed')}",
    f"Duration: {protocol.get('duration', 'Not listed')}",
    "",
    "Precautions:",
]
summary_lines += [f"- {item}" for item in precautions] if precautions else ["- Not listed"]
summary_lines += ["", "Phases:"]
for phase, items in weeks.items():
    summary_lines.append(f"{phase}:")
    summary_lines += [f"- {item}" for item in items]

st.text_area("Copy this into a note if needed", "\n".join(summary_lines), height=300)

st.divider()
st.caption("Use clinical judgment and follow surgeon-specific restrictions when applicable.")
