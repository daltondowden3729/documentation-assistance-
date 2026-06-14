import streamlit as st
from datetime import datetime

try:
    from pt_master_database_v2 import protocols
except ImportError:
    from pt_master_database_v1 import protocols


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


SECTION_ORDER = [
    "goals",
    "precautions",
    "brace",
    "weight_bearing",
    "rom_restrictions",
    "modalities",
    "manual_therapy",
    "therapeutic_exercise",
    "neuromuscular_reeducation",
    "functional_training",
    "cardio",
    "patient_education",
    "criteria_to_progress",
    "criteria_to_discharge",
]


SECTION_LABELS = {
    "goals": "Goals",
    "precautions": "Precautions",
    "brace": "Brace / Splint",
    "weight_bearing": "Weight Bearing",
    "rom_restrictions": "ROM Restrictions",
    "modalities": "Modalities",
    "manual_therapy": "Manual Therapy",
    "therapeutic_exercise": "Therapeutic Exercise",
    "neuromuscular_reeducation": "Neuromuscular Re-ed",
    "functional_training": "Functional Training",
    "cardio": "Cardio",
    "patient_education": "Patient Education",
    "criteria_to_progress": "Criteria to Progress",
    "criteria_to_discharge": "Criteria to Discharge",
}


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


def display_items(items):
    if isinstance(items, list):
        for item in items:
            st.write(f"- {item}")
    elif isinstance(items, dict):
        st.json(items)
    else:
        st.write(items)


def display_protocol(protocol):
    st.subheader("Protocol Information")

    phases = protocol.get("phases", {})

    if phases:
        phase_names = list(phases.keys())
        selected_phase = st.selectbox("Select Phase", phase_names)

        phase_data = phases[selected_phase]

        for section in SECTION_ORDER:
            if section in phase_data:
                label = SECTION_LABELS.get(section, section.replace("_", " ").title())

                with st.expander(label, expanded=(section == "goals")):
                    display_items(phase_data[section])

        extra_sections = [
            section for section in phase_data.keys()
            if section not in SECTION_ORDER
        ]

        for section in extra_sections:
            label = section.replace("_", " ").title()
            with st.expander(label):
                display_items(phase_data[section])

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

        protocol = get_protocol(
            selected["region"],
            selected["area"],
            selected["diagnosis"]
        )

        phase_name = "Selected phase"
        suggested_exercises = []

        phases = protocol.get("phases", {})
        if phases:
            phase_name = st.selectbox("Select Phase", list(phases.keys()))
            suggested_exercises = phases[phase_name].get("therapeutic_exercise", [])

            if suggested_exercises:
                chosen_exercises = st.multiselect(
                    "Select Exercises Performed",
                    suggested_exercises,
                    default=suggested_exercises[:3]
                )
            else:
                chosen_exercises = []
        else:
            st.info("No detailed phases available yet for this diagnosis.")
            chosen_exercises = []

        treatment_focus = st.text_area(
            "Treatment Focus",
            placeholder="Example: ROM, strengthening, gait training, balance, pain control"
        )

        extra_exercises = st.text_area(
            "Additional Exercises Performed",
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
            exercise_list = list(chosen_exercises)

            if extra_exercises.strip():
                exercise_list.append(extra_exercises.strip())

            exercise_text = ", ".join(exercise_list) if exercise_list else "skilled therapeutic exercise"

            note = (
                f"Therapeutic interventions were performed this visit for "
                f"{selected['diagnosis']} during {phase_name}. Treatment focused on "
                f"{treatment_focus}. Patient completed {exercise_text}. Patient required "
                f"{cueing}. Patient {response}. Patient continues to benefit from skilled PT "
                f"services to address remaining impairments and progress toward functional goals."
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
