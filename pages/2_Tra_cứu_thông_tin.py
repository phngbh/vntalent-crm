import streamlit as st
import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title('Trang tra cứu thông tin')

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
    sheet_schdf.columns = sheet_schdf.iloc[0] #Set first row as column names
    sheet_schdf = sheet_schdf[1:] # Remove the first row

    # Get colaborator ID and info
    cid = sheet_schdf.iloc[:, 1]
    id = st.selectbox("Chọn mã đối tác muốn hiển thị:", cid)
    inf = sheet_schdf.loc[sheet_schdf['Index'] == id]

    #Report
    st.header(inf['School/MasterAgents'].values[0],'\n\n')

    st.subheader('THÔNG TIN CHƯƠNG TRÌNH')
    st.write('Đơn vị cung cấp: ',inf['Supplier'].values[0])
    st.write('Loại trường: ', inf['SchoolType'].values[0])
    st.write('Chương trình nổi bật: ', inf['ProgramHighlight'].values[0])
    st.write('Học phí (USD): ', inf['Tuition(USD)'].values[0])
    st.write('Học bổng (USD): ', inf['Scholarship(USD)'].values[0])
    st.write('Sau học bổng (USD): ', inf['AfterScholarship(USD)'].values[0])
    st.write('Sinh hoạt phí: ', inf['LivingExpense(USD)'].values[0])
    st.write('Yêu cầu đầu vào: ', inf['Requirement'].values[0])
    st.write('Yêu cầu hồ sơ: ', inf['DocumentRequirement'].values[0])

    st.subheader('THÔNG TIN HỢP ĐỒNG')
    st.write('Folder hợp đồng: ', inf['Folder'].values[0])
    st.write('Tình trạng hợp đồng: ', inf['Status'].values[0])
    st.write('Ngày ký: ', inf['SignDate'].values[0])
    st.write('Ngày hết hạn: ', inf['ExpiDate'].values[0])
    st.write('Hoa hồng: ', inf['Com'].values[0])
    st.write('Hoa hồng thưởng thêm: ', inf['XtraCom'].values[0])
    st.write('Điều kiện hoa hồng thưởng thêm: ', inf['XtraComCond'].values[0])
    st.write('Thưởng thêm tư vấn viên: ', inf['TVVBonus'].values[0])
    st.write('Thời hạn thanh toán hoa hồng: ', inf['DurationComPay'].values[0])
    st.write('Điều kiện thanh toán hoa hồng: ', inf['ComPayCond'].values[0])
    st.write('Ghi chú hợp đồng: ', inf['NoteContr'].values[0])

    st.subheader('THÔNG TIN LIÊN HỆ')
    st.write('Người đại diện đối tác: ', inf['Rep'].values[0])
    st.write('Email: ', inf['Email'].values[0])
    st.write('Số điện thoại: ', inf['Tel'].values[0])
    st.write('Địa chỉ: ', inf['Add'].values[0])
    st.write('Website: ', inf['Website'].values[0])

    st.subheader('CHÍNH SÁCH BÁN RA')
    st.write('Giá bán ra: ', inf['Price'].values[0])
    st.write('Phí dịch vụ: ', inf['ServFee'].values[0])
    st.write('Dịch vụ bao gồm trong phí: ', inf['Serv'].values[0])
    st.write('Dịch vụ khách tự trả: ', inf['XtraServ'].values[0])
    st.write('Dịch vụ miễn phí: ', inf['FreeServ'].values[0])
    st.write('Ghi chú phí dịch vụ: ', inf['NoteServFee'].values[0])
    st.write('Hoa hồng tư vấn viên: ', inf['TVVCom'].values[0])
    st.write('Hoa hồng tư vấn viên chăm sóc: ', inf['CareTVVCom'].values[0])
    st.write('Hoa hồng cộng tác viên: ', inf['CTVCom'].values[0])
    st.write('Điều kiện trích: ', inf['WithdrawCond'].values[0])
    st.write('Thưởng thêm: ', inf['Bonus'].values[0])
    st.write('Điều kiện thưởng thêm: ', inf['BonusCond'].values[0])
    st.write('Thời hạn thanh toán hoa hồng CTV: ', inf['DurationComPayCTV'].values[0])
    st.write('Ghi chú hoa hồng: ', inf['NoteCom'].values[0])

with tab2:
    # Get the specific sheets of the Spreadsheet
    sheet_stu = sheet.get_worksheet(1)
    sheet_studf = pd.DataFrame(sheet_stu.get_all_values())
    sheet_studf.columns = sheet_studf.iloc[0] #Set first row as column names
    sheet_studf = sheet_studf[1:] # Remove the first row

    # Get colaborator ID and info
    sid = sheet_studf.iloc[:, 1]
    id = st.selectbox("Chọn mã học sinh muốn hiển thị:", sid)
    inf = sheet_studf.loc[sheet_studf['Index'] == id]

    #Report
    strg = inf['LastName'].values[0] + ' ' + inf['MiddleName'].values[0] + ' ' + inf['Name'].values[0] + '\n\n'
    st.header(strg)

    st.subheader('THÔNG TIN NGƯỜI ĐI HỌC')
    st.write('Giới tính: ',inf['Gender'].values[0])
    st.write('Ngày sinh: ', inf['DOB'].values[0])
    st.write('Số hộ chiếu: ', inf['Pass'].values[0])
    st.write('Ngày cấp hộ chiếu: ', inf['PassDa'].values[0])
    st.write('Ngày hết hạn hộ chiếu: ', inf['PassExpiDa'].values[0])
    st.write('Số CMND: ', inf['CMND'].values[0])
    st.write('Ngày cấp CMND: ', inf['CMNDDa'].values[0])
    st.write('Số điện thoại: ', inf['Tel'].values[0])
    st.write('Email: ', inf['Email'].values[0])
    st.write('Địa chỉ thường trú: ', inf['Add'].values[0])
    st.write('Địa chỉ liên hệ: ', inf['AddCont'].values[0])
    st.write('Facebook: ', inf['Facebook'].values[0])
    st.write('Zalo: ', inf['Zalo'].values[0])

    st.subheader('THÔNG TIN NGƯỜI GIÁM HỘ')
    st.write('Họ: ', inf['LastNameRel'].values[0])
    st.write('Tên: ', inf['NameRel'].values[0])
    st.write('Giới tính: ', inf['GenderRel'].values[0])
    st.write('Quan hệ với người đi học: ', inf['RelRel'].values[0])
    st.write('Số CMND/Passport: ', inf['CMND/PassRel'].values[0])
    st.write('Ngày sinh: ', inf['DOBRel'].values[0])
    st.write('Số điện thoại: ', inf['TelRel'].values[0])
    st.write('Email: ', inf['EmailRel'].values[0])
    st.write('Địa chỉ liên hệ: ', inf['AddRel'].values[0])

    st.subheader('NGUỒN/CHĂM SÓC')
    st.write('Tên CTV: ', inf['CTV'].values[0])
    st.write('Tên TVV: ', inf['TVV'].values[0])

    st.subheader('THÔNG TIN HỢP ĐỒNG')
    st.write('Ngày ký: ', inf['SignDa'].values[0])
    st.write('Số hợp đồng: ', inf['ContrNum'].values[0])
    st.write('Chương trình: ', inf['Prog'].values[0])
    st.write('Trường: ', inf['School'].values[0])
    st.write('Kỳ học: ', inf['Term'].values[0])
    st.write('Dịch vụ bao gồm trong hợp đồng: ', inf['Serv'].values[0])
    st.write('Phí dịch vụ theo hợp đồng: ', inf['ServFee'].values[0])
    st.write('Hình thức thanh toán: ', inf['PayMeans'].values[0])
    st.write('Quy định hoàn phí: ', inf['Refund'].values[0])
    st.write('Điều kiện hoàn phí: ', inf['RefundCond'].values[0])
    st.write('Folder hợp đồng: ', inf['Folder'].values[0])
    st.write('Tình trạng hợp đồng: ', inf['Status'].values[0])
    st.write('Phí thu đợt 1: ', inf['Fee1'].values[0])
    st.write('Ngày thu đợt 1: ', inf['Fee1Da'].values[0])
    st.write('Hình thức thu đợt 1: ', inf['PayMeans1'].values[0])
    st.write('Phí thu đợt 2 : ', inf['Fee2'].values[0])
    st.write('Ngày thu đợt 2: ', inf['Fee2Da'].values[0])
    st.write('Hình thức thu đợt 2: ', inf['PayMeans2'].values[0])
    st.write('Phí thu đợt 3: ', inf['Fee3'].values[0])
    st.write('Ngày thu đợt 3: ', inf['Fee3Da'].values[0])
    st.write('Hình thức thu đợt 3: ', inf['PayMeans3'].values[0])
    st.write('Tổng phí thu: ', inf['FeeTot'].values[0])

    st.subheader('THEO DÕI HOA HỒNG')
    st.write('Hoa hồng %: ', inf['ComPerc'].values[0])
    st.write('Hoa hồng thành tiền: ', inf['Com'].values[0])
    st.write('Đơn vị tiền tệ: ', inf['Curr'].values[0])
    st.write('Chuyển đổi sang VND: ', inf['CurrVND'].values[0])
    st.write('Ngày đợt 1: ', inf['Da1'].values[0])
    st.write('Ngày đợt 2: ', inf['Da2'].values[0])
    st.write('Ngày đợt 3: ', inf['Da3'].values[0])
    st.write('Ngày đợt 4: ', inf['Da4'].values[0])
    st.write('Ngày đợt 5: ', inf['Da5'].values[0])
    st.write('Ngày đợt 6: ', inf['Da6'].values[0])

    st.subheader('THÔNG TIN THANH LÝ HỢP ĐỒNG')
    st.write('Ngày thanh lý: ', inf['PayDa'].values[0])
    st.write('Số thanh lý: ', inf['PayNum'].values[0])
    st.write('Lý do thanh lý: ', inf['PayRea'].values[0])
    st.write('Link file thanh lý: ', inf['PayLink'].values[0])
    st.write('Ghi chú thanh lý: ', inf['NotePay'].values[0])

with tab3:
    # Get the specific sheets of the Spreadsheet
    sheet_sta = sheet.get_worksheet(2)
    sheet_stadf = pd.DataFrame(sheet_sta.get_all_values())
    sheet_stadf.columns = sheet_stadf.iloc[0] #Set first row as column names
    sheet_stadf = sheet_stadf[1:] # Remove the first row

    # Get colaborator ID and info
    stid = sheet_stadf.iloc[:, 0]
    id = st.selectbox("Chọn mã CTV muốn hiển thị:", stid)
    inf = sheet_stadf.loc[sheet_stadf['Index'] == id]

    #Report
    st.header(inf['CTV'].values[0],'\n\n')

    st.write('Người đại diện: ',inf['Rep'].values[0])
    st.write('Số điện thoại: ', inf['Tel'].values[0])
    st.write('Email: ', inf['Email'].values[0])
    st.write('Địa chỉ: ', inf['Add'].values[0])
    st.write('Tình trạng hợp đồng: ', inf['Status'].values[0])
    st.write('Ngày ký: ', inf['SignDa'].values[0])
    st.write('Ngày hết hạn hợp đồng: ', inf['ExpiDa'].values[0])
    st.write('Chương trình: ', inf['Prog'].values[0])
    st.write('Hoa hồng theo phần trăm: ', inf['ComPerc'].values[0])
    st.write('Hoa hồng thành tiền: ', inf['Com'].values[0])
    st.write('Số lượng: ', inf['Num'].values[0])
    st.write('Điều kiện hoa hồng: ', inf['ComCond'].values[0])
    st.write('Hoa hồng thưởng thêm %: ', inf['XtraComPerc'].values[0])
    st.write('Điều kiện hoa hồng thưởng thêm: ', inf['XtraComCond'].values[0])
    st.write('Phí dịch vụ: ', inf['ServFee'].values[0])
    st.write('Ghi chú phí dịch vụ: ', inf['ServFeeNote'].values[0])
    st.write('Thời hạn thanh toán hoa hồng: ', inf['DurationPayCom'].values[0])
    st.write('Folder hợp đồng: ', inf['Folder'].values[0])
    st.write('Ghi chú: ', inf['Note'].values[0])



