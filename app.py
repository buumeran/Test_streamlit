import streamlit as st
import spreadsheet as sp

if "check" not in st.session_state:
    report = sp.createNewDayReport()
    st.session_state.check = report

sheet = st.session_state.check



st.title('日報アプリ')

if st.button('出勤'):
    sp.checkin(sheet)


if st.button('退勤'):
    sp.checkout(sheet)