import streamlit as st
from pyperclip import copy

st.title('Abschließende BA Prüfung')

pruefer = [
    "Mario DÖLLER",
    "Michael KOHLEGGER",
    "Karsten BÖHM",
    "Johannes LÜTHI",
    "Lukas DEMETZ",
    "Robert KATHREIN",
    "Julian BIALAS",
    "Sabine ASCHER",
    "Johannes LARCHER"
]

fname = st.text_input("Vorname")
lname = st.text_input("Nachname")

st.header("BA Vorstellung und Verteidigung")

ba_punkte = st.slider('Vorstellung + Verteidigung BA', 0, 30, 20, 1)

st.header("Fragenteil 1")

frag1_pruef = st.selectbox("Prüfer des ersten Fragenblocks", pruefer)
frag1_ba = st.text_area("Fragen zur Bachelorarbeiten (P1)")
frag1_memo = st.text_area("Fragen zu Querverbindungsthemen (P1)")
frag1 = st.slider('Erster Fragenblock', 0, 100, 50, 5) / 100

st.header("Fragenteil 2")

frag2_pruef = st.selectbox("Prüfer des zweiten Fragenblocks", pruefer)
frag2_ba = st.text_area("Fragen zur Bachelorarbeiten (P2)")
frag2_memo = st.text_area("Fragen zu Querverbindungsthemen (P2)")
frag2 = st.slider('Zweiter Fragenblock', 0, 100, 50, 5) / 100

st.header("Fragenteil 3")

frag3_pruef = st.selectbox("Prüfer des dritten Fragenblocks", pruefer)
frag3_ba = st.text_area("Fragen zur Bachelorarbeiten (P3)")
frag3_memo = st.text_area("Fragen zu Querverbindungsthemen (P3)")
frag3 = st.slider('Dritter Fragenblock', 0, 100, 50, 5) / 100

st.header("Ergebnis")

fragen_punkte = frag1*70/3+frag2*70/3+frag3*70/3
memo_a = f"{frag1_pruef}: {frag1_ba}\n\n{frag2_pruef}: {frag2_ba}\n\n{frag3_pruef}: {frag3_ba}"
memo_b = f"{frag1_pruef} ({frag1*100}%): {frag1_memo}\n\n{frag2_pruef} ({frag2*100}%): {frag2_memo}\n\n{frag3_pruef} ({frag3*100}%): {frag3_memo}"
gesamt_punkte = ba_punkte + fragen_punkte

st.text_input(
    label="Punkte Verteidigung",
    value=f"{ba_punkte}"
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
        f.write("Punkte Verteidigung: "+str(ba_punkte)+"\n\n\n"+memo_a+"\n\n\n"+"Punkte Querverbindungen: "+str(fragen_punkte)+"\n\n\n"+memo_b+"\n\n\n"+str(gesamt_punkte))