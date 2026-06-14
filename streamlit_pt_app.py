import streamlit as st
from datetime import datetime

try:
    from pt_master_database_v1 import protocols
except ImportError:
    protocols = {
        "Arm": {
            "Elbow": {
                "Lateral Epicondylitis (Tennis Elbow)": {
                    "status": "indexed",
                    "phases": {}
                }
            }
        }
    }


st.set_page_config(
    page_title="PT Documentation Assistant",
    page_icon="🦴",
    layout="centered"
)

st.title("PT Documentation Assistant")
st.caption("Protocol reference, treatment plan builder, and daily note generator")

tab1, tab2, tab3 = st.tabs([
    "Browse Protocols",
    "Search Diagnosis",
    "Generate Note"
])


def get_all_diagnoses():
    results = []

    for region, areas in protocols.items():
        for area, diagnoses in areas.items():
            for diagnosis in diagnoses:
                results.append({
                    "region": region,
                    "area": area,
                    "diagnosis": diagnosis
                })

    return results


def get_protocol(region, area, diagnosis):
    return protocols[region][area][diagnosis]


def display_protocol(protocol):
    st.subheader("Protocol Information")

    if "phases" in protocol and protocol["phases"]:
        phase_names = list(protocol["phases"].keys())
        selected_phase = st.selectbox("Select Phase", phase_names)

        phase_data = protocol["phases"][selected_phase]

        for section, items in phase_data.items():
            st.markdown(f"### {section.replace('_', ' ').title()}")

            if isinstance(items, list):
                for item in items:
                    st.write(f"- {item}")
            else:
                st.write(items)
    else:
        st.info(
            "This diagnosis is indexed in the master database. "
            "Detailed phase content can be added next."
        )


with tab1:
    st.header("Browse by Category")

    region = st.selectbox("Body Region", list(protocols.keys()))
    area_options = list(protocols[region].keys())

    area = st.selectbox("Area", area_options)
    diagnosis_options = list(protocols[region][area].keys())

    if diagnosis_options:
        diagnosis = st.selectbox("Diagnosis", diagnosis_options)
        protocol = get_protocol(region, area, diagnosis)

        st.success(f"{region} → {area} → {diagnosis}")
        display_protocol(protocol)
    else:
        st.warning("No diagnoses added in this area yet.")


with tab2:
    st.header("Search Diagnosis")

    search = st.text_input("Type diagnosis name", placeholder="Example: ACL, lumbar, Bankart")

    if search:
        matches = [
            item for item in get_all_diagnoses()
            if search.lower() in item["diagnosis"].lower()
        ]

        if matches:
            for item in matches:
                with st.expander(
                    f"{item['diagnosis']} — {item['region']} / {item['area']}"
                ):
                    protocol = get_protocol(
                        item["region"],
                        item["area"],
                        item["diagnosis"]
                    )
                    display_protocol(protocol)
        else:
            st.warning("No matches found.")


with tab3:
    st.header("Generate Daily Note")

    all_diagnoses = get_all_diagnoses()

    if all_diagnoses:
        selected = st.selectbox(
            "Select Diagnosis",
            all_diagnoses,
            format_func=lambda x: f"{x['diagnosis']} ({x['region']} / {x['area']})"
        )

        treatment_focus = st.text_area(
            "Treatment Focus",
            placeholder="Example: ROM, strengthening, gait training, balance, pain control"
        )

        exercises = st.text_area(
            "Exercises Performed",
            placeholder="Example: heel slides, quad sets, step-ups, bike"
        )

        cueing = st.text_input(
            "Cueing Provided",
            value="verbal and tactile cueing for proper technique and safety"
        )

        response = st.selectbox(
            "Patient Response",
            [
                "tolerated treatment well with no adverse response",
                "reported mild fatigue but no increase in pain",
                "required rest breaks due to fatigue",
                "reported increased soreness; treatment modified accordingly"
            ]
        )

        if st.button("Generate Note"):
            note = (
                f"Therapeutic interventions were performed this visit for "
                f"{selected['diagnosis']}. Treatment focused on {treatment_focus}. "
                f"Patient completed {exercises}. Patient required {cueing}. "
                f"Patient {response}. Patient continues to benefit from skilled PT "
                f"services to address remaining impairments and progress toward "
                f"functional goals."
            )

            st.subheader("Generated Note")
            st.text_area("Copy Note", note, height=220)

            st.download_button(
                "Download Note",
                data=note,
                file_name=f"pt_note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
    else:
        st.warning("No diagnoses available.")
