import streamlit as st
import sys
import spreadsheet as sp
sys.stdout.write("1\n")
if "check" not in st.session_state:
    sys.stdout.write("2\n")
    report = sp.createNewDayReport()
    st.session_state.check = report

sys.stdout.write("3\n")
sheet = st.session_state.check

sys.stdout.write("4\n")

st.title('日報アプリ(sysいれた)')

sys.stdout.write("5\n")

if st.button('出勤'):
    sp.checkin(sheet)
    sys.stdout.write("6\n")


if st.button('退勤'):
    sp.checkout(sheet)
    sys.stdout.write("7\n")