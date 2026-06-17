
from datetime import date
import streamlit as st
from pt_master_database_v1 import PROTOCOLS

st.set_page_config(page_title="PTA Protocol App", page_icon="🦴", layout="wide")

def week_to_float(key: str):
    # supports "0-2", "12+", "Freezing", "See protocol"
    try:
        if "+" in key:
            return float(key.replace("+", ""))
        if "-" in key:
            return float(key.split("-")[0])
        return None
    except Exception:
        return None

def find_phase(weeks_post_op: float, weeks_dict: dict):
    numeric = []
    for k in weeks_dict:
        try:
            if "+" in k:
                start = float(k.replace("+", ""))
                end = 10_000
            elif "-" in k:
                a, b = k.split("-")
                start, end = float(a), float(b)
            else:
                continue
            numeric.append((start, end, k))
        except Exception:
            continue
    for start, end, k in sorted(numeric):
        if start <= weeks_post_op < end:
            return k
    if numeric:
        return sorted(numeric)[-1][2]
    return list(weeks_dict.keys())[0] if weeks_dict else None

def timeline_text(dos):
    today = date.today()
    days = (today - dos).days
    if days < 0:
        return days, "Surgery date is in the future."
    weeks = days // 7
    rem_days = days % 7
    months = days / 30.44
    return days, f"{days} days • {weeks} weeks {rem_days} days • {months:.1f} months"

st.title("🦴 PTA Outpatient Protocol App")
st.caption("Protocol lookup + post-op timeline calculator")

tab1, tab2, tab3 = st.tabs(["Protocol Lookup", "Post-Op Calculator", "Database"])

with tab1:
    colA, colB, colC = st.columns(3)
    regions = ["All"] + sorted(set(p["body_region"] for p in PROTOCOLS.values()))
    with colA:
        region = st.selectbox("Body Region", regions)
    types = ["All"] + sorted(set(p["type"] for p in PROTOCOLS.values()))
    with colB:
        typ = st.selectbox("Type", types)
    search = st.text_input("Search diagnosis")

    names = sorted(PROTOCOLS.keys())
    if region != "All":
        names = [n for n in names if PROTOCOLS[n]["body_region"] == region]
    if typ != "All":
        names = [n for n in names if PROTOCOLS[n]["type"] == typ]
    if search:
        names = [n for n in names if search.lower() in n.lower()]

    diagnosis = st.selectbox("Diagnosis", names)
    p = PROTOCOLS[diagnosis]

    st.subheader(diagnosis)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Region", p["body_region"])
    m2.metric("Type", p["type"])
    m3.metric("Frequency", p.get("frequency", ""))
    m4.metric("Duration", p.get("duration", ""))

    with st.expander("Precautions", expanded=True):
        for item in p.get("precautions", []):
            st.write(f"• {item}")

    with st.expander("Red Flags"):
        for item in p.get("red_flags", []):
            st.write(f"• {item}")

    with st.expander("Outcome Measures"):
        st.write(", ".join(p.get("outcome_measures", [])))

    st.markdown("### Week / Phase Progression")
    for wk, items in p.get("weeks", {}).items():
        with st.expander(f"Week/Phase: {wk}", expanded=False):
            for item in items:
                st.write(f"• {item}")

with tab2:
    st.subheader("Post-Op / Injury Date Calculator")
    diagnosis2 = st.selectbox("Select protocol", sorted(PROTOCOLS.keys()), key="calc_dx")
    dos = st.date_input("Date of surgery / injury", value=date.today())
    days, text = timeline_text(dos)
    st.info(text)

    if days >= 0:
        weeks_post = days / 7
        p2 = PROTOCOLS[diagnosis2]
        phase = find_phase(weeks_post, p2.get("weeks", {}))
        st.success(f"Current protocol phase: {phase}")
        st.markdown("### Suggested Focus")
        for item in p2.get("weeks", {}).get(phase, []):
            st.write(f"• {item}")

    st.checkbox("Manual phase override")
    chosen_phase = st.selectbox("View another phase", list(PROTOCOLS[diagnosis2].get("weeks", {}).keys()))
    st.markdown("### Selected Phase Details")
    for item in PROTOCOLS[diagnosis2].get("weeks", {}).get(chosen_phase, []):
        st.write(f"• {item}")

with tab3:
    st.subheader("Database Summary")
    st.write(f"Total protocols: **{len(PROTOCOLS)}**")
    counts = {}
    for p in PROTOCOLS.values():
        counts[p["body_region"]] = counts.get(p["body_region"], 0) + 1
    st.json(counts)
