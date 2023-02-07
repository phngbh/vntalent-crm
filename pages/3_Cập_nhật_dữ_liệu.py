import streamlit as st
import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title('Trang cập nhật thông tin')

# Obtain the Google Sheet credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gifted-decker-376409-712e5c6639b5.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("VNTalent CRM")

# Inputs
tab1, tab2, tab3 = st.tabs(["Đối tác", "Học sinh", "Cộng tác viên"])

with tab1:
    # Get the specific sheets of the Spreadsheet
    sheet_sch = sheet.get_worksheet(0)
    sheet_schdf = pd.DataFrame(sheet_sch.get_all_values())

    # Get all the fields
    fields = sheet_schdf.iloc[0]

    # Get colaborator ID
    cid = sheet_schdf.iloc[1:, 1]

    id = st.selectbox("Chọn mã đối tác cần cập nhật thông tin", cid)

    col1, col2 = st.columns([1.5,3])
    with col1:
        field1 = st.selectbox("Chọn thông tin cần cập nhật 1", fields)
        field2 = st.selectbox("Chọn thông tin cần cập nhật 2", fields)
        field3 = st.selectbox("Chọn thông tin cần cập nhật 3", fields)
    with col2:
        edit1 = st.text_input("Nội dung cập nhật 1:")
        edit2 = st.text_input("Nội dung cập nhật 2:")
        edit3 = st.text_input("Nội dung cập nhật 3:")

    if st.button('Cập nhật vào hệ thống'):
        tmp = np.where(cid == id)
        rownum = tmp[0][0] + 2
        d = {field1: edit1, field2: edit2, field3: edit3}
        for key, value in d.items():
            if len(key) > 0 and len(value) > 0:
                tmp = np.where(fields == key)
                colnum = tmp[0][0] + 1
                sheet_sch.update_cell(rownum, colnum, value)
                st.write("Đã cập nhật thông tin vào hệ thống")

with tab2:
    # Get the specific sheets of the Spreadsheet
    sheet_stu = sheet.get_worksheet(1)
    sheet_studf = pd.DataFrame(sheet_stu.get_all_values())

    # Get all the fields
    fieldstu = sheet_studf.iloc[0]

    # Get colaborator ID
    sid = sheet_studf.iloc[1:, 1]

    ids = st.selectbox("Chọn mã học sinh cần cập nhật thông tin", sid)

    col1, col2 = st.columns([1.5,3])
    with col1:
        field1s = st.selectbox("Chọn thông tin hs cần cập nhật 1", fieldstu)
        field2s = st.selectbox("Chọn thông tin hs cần cập nhật 2", fieldstu)
        field3s = st.selectbox("Chọn thông tin hs cần cập nhật 3", fieldstu)
    with col2:
        edit1s = st.text_input("Nội dung hs cập nhật 1:")
        edit2s = st.text_input("Nội dung hs cập nhật 2:")
        edit3s = st.text_input("Nội dung hs cập nhật 3:")

    if st.button('Cập nhật hs vào hệ thống'):
        tmp = np.where(sid == ids)
        rownum = tmp[0][0] + 2
        d = {field1s: edit1s, field2s: edit2s, field3s: edit3s}
        for key, value in d.items():
            if len(key) > 0 and len(value) > 0:
                tmp = np.where(fieldstu == key)
                colnum = tmp[0][0] + 1
                sheet_stu.update_cell(rownum, colnum, value)
                st.write("Đã cập nhật thông tin hs vào hệ thống")

with tab3:
    # Get the specific sheets of the Spreadsheet
    sheet_sta = sheet.get_worksheet(2)
    sheet_stadf = pd.DataFrame(sheet_sta.get_all_values())

    # Get all the fields
    fieldsta = sheet_stadf.iloc[0]

    # Get colaborator ID
    stid = sheet_stadf.iloc[1:, 0]

    idst = st.selectbox("Chọn mã CTV cần cập nhật thông tin", stid)

    col1, col2 = st.columns([1.5,3])
    with col1:
        field1st = st.selectbox("Chọn thông tin CTV cần cập nhật 1", fieldsta)
        field2st = st.selectbox("Chọn thông tin CTV cần cập nhật 2", fieldsta)
        field3st = st.selectbox("Chọn thông tin CTV cần cập nhật 3", fieldsta)
    with col2:
        edit1st = st.text_input("Nội dung CTV cập nhật 1:")
        edit2st = st.text_input("Nội dung CTV cập nhật 2:")
        edit3st = st.text_input("Nội dung CTV cập nhật 3:")

    if st.button('Cập nhật CTV vào hệ thống'):
        tmp = np.where(stid == idst)
        rownum = tmp[0][0] + 2
        d = {field1st: edit1st, field2st: edit2st, field3st: edit3st}
        for key, value in d.items():
            if len(key) > 0 and len(value) > 0:
                tmp = np.where(fieldsta == key)
                colnum = tmp[0][0] + 1
                sheet_sta.update_cell(rownum, colnum, value)
                st.write("Đã cập nhật thông tin CTV vào hệ thống")