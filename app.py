import streamlit as st
import spreadsheet as sp
print(1)
if "check" not in st.session_state:
    print(2)
    report = sp.createNewDayReport()
    st.session_state.check = report

print(3)
sheet = st.session_state.check

print(4)

st.title('日報アプリ')

print(5)

if st.button('出勤'):
    sp.checkin(sheet)
    print(6)


if st.button('退勤'):
    sp.checkout(sheet)
    print(7)