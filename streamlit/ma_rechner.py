import streamlit as st
from pyperclip import copy

st.title('Abschließende MA Prüfung')

pruefer = [
    "Mario DÖLLER",
    "Michael KOHLEGGER",
    "Karsten BÖHM",
    "Johannes LÜTHI",
    "Lukas HUBER",
    "Lukas DEMETZ",
    "Robert KATHREIN",
    "Michael HECHT",
    "Julian BIALAS",
    "Dietmar MILLINGER",
    "Johannes LARCHER"
]

fname = st.text_input("Vorname")
lname = st.text_input("Nachname")
ma = st.number_input("Punkte Masterarbeit",  step=1, max_value=100, min_value=60)

st.header("Präsentation der MA und Verteidigung")

pt = st.slider('Präsentationstechnik', 0, 5, 5, 1)
iv = st.slider('Inhaltsvermerk', 0, 5, 5, 1)
df = st.slider('Defensio', 0, 10, 10, 1)

col1, col2, col3 = st.columns(3)

with col1:

    st.header("Fragenteil 1")

    frag1_pruef = st.selectbox("Prüfer des ersten Fragenblocks", pruefer)
    frag1_ba = st.text_area("Fragen zur Masterarbeit (P1)")
    frag1_memo = st.text_area("Allgemeiner Fragenteil (P1)")
    frag1 = st.slider('Erster Fragenblock', 0, 100, 50, 5) / 100

with col2:

    st.header("Fragenteil 2")

    frag2_pruef = st.selectbox("Prüfer des zweiten Fragenblocks", pruefer)
    frag2_ba = st.text_area("Fragen zur Masterarbeit (P2)")
    frag2_memo = st.text_area("Allgemeiner Fragenteil (P2)")
    frag2 = st.slider('Zweiter Fragenblock', 0, 100, 50, 5) / 100

with col3:

    st.header("Fragenteil 3")

    frag3_pruef = st.selectbox("Prüfer des dritten Fragenblocks", pruefer)
    frag3_ba = st.text_area("Fragen zur Masterarbeit (P3)")
    frag3_memo = st.text_area("Allgemeiner Fragenteil (P3)")
    frag3 = st.slider('Dritter Fragenblock', 0, 100, 50, 5) / 100

st.header("Ergebnis")

ma_anteil = ma * 0.4
fragen_punkte = frag1*40/3+frag2*40/3+frag3*40/3
memo_a = f"{frag1_pruef}: {frag1_ba}\n\n{frag2_pruef}: {frag2_ba}\n\n{frag3_pruef}: {frag3_ba}"
memo_b = f"{frag1_pruef} ({frag1*100}%): {frag1_memo}\n\n{frag2_pruef} ({frag2*100}%): {frag2_memo}\n\n{frag3_pruef} ({frag3*100}%): {frag3_memo}"
gesamt_punkte = ma_anteil + pt + iv + df + fragen_punkte

st.text_input(
    label="Punkte Präsentation",
    value=f"{pt}"
)

st.text_input(
    label="Punkte Inhaltsvermerk",
    value=f"{iv}"
)

st.text_input(
    label="Punkte Defensio",
    value=f"{df}"
)

st.text_area(
    label="Dokumentation Verteidigung",
    value=memo_a
)

if st.button("Copy Verteidigung Memo"):
    copy(memo_a)


st.text_input(
    label="Punkte Fragenteil",
    value=f"{fragen_punkte}"
)

st.text_area(
    label="Dokumentation Fragenteil",
    value=memo_b
)
if st.button("Copy Fragenteil Memo"):
    copy(memo_b)

st.text_input("Gesamtpunkte", f"{gesamt_punkte}")

if st.button("Safe Results"):
    with open(f"Prüfungsprotokoll__{lname}_{fname}.txt", "w", encoding="utf-8") as f:
        f.write("Punkte Verteidigung: "+str(df)+"\n\n\n"+memo_a+"\n\n\n"+"Punkte Präsentation+Inhalt: "+str(iv+pt)+"\n\n\n"+memo_b+"\n\n\n"+str(gesamt_punkte))