
import streamlit as st
import pandas as pd
import datetime
import gspread
from google.oauth2 import service_account

st.title('Trang nhập dữ liệu')

# Obtain the Google Sheet credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes = scope)
client = gspread.authorize(creds)

# Inputs
tab1, tab2, tab3 = st.tabs(["Đối tác", "Học sinh", "Cộng tác viên"])

with tab1:
    ### Schools/organizations
    ind_org = st.text_input('STT:')
    code_org = st.text_input('MÃ ĐỐI TÁC:', 'XXX')
    name_org = st.text_input('TRƯỜNG/MASTER AGENT:', 'Trường XXX')
    partner = st.text_input('ĐƠN VỊ CUNG CẤP:', 'Đối tác XXX')
    typ = st.selectbox('LOẠI TRƯỜNG:', ('K-12', '6-12', '9-12', 'COL', 'COL/UNI', 'UNI', 'LAN', 'OTHER'))
    prog = st.text_input('CHƯƠNG TRÌNH NỔI BẬT:', 'Chương trình XXX')
    tui = st.slider('HỌC PHÍ (1 năm, don vi USD1000):', min_value=1, max_value=200)
    scho = st.slider('HỌC BỔNG (1 nam, don vi USD1000):', min_value=1, max_value=200)
    exps = st.slider('SINH HOẠT PHÍ (1 nam, don vi USD1000):', min_value=1, max_value=200)
    reqr = st.text_input('YÊU CẦU ĐẦU VÀO:', 'IELTS, GPA etc...')
    doc = st.text_input('YÊU CẦU HỒ SƠ:', 'Bang tot nghiep, visa etc...')
    folder_org = st.text_input('FOLDER HỢP ĐỒNG:', 'Link folder')
    stat_org = st.selectbox('TÌNH TRẠNG HỢP TÁC', ('Đã ký', 'Liên hệ/chưa ký', 'Huỷ hợp tác', 'Chưa liên hệ'))
    signda = st.date_input("NGÀY KÝ:", datetime.date(2019, 7, 6)).strftime("%Y/%m/%d")
    expida = st.date_input("NGÀY HẾT HẠN:", datetime.date(2019, 7, 6)).strftime("%Y/%m/%d")
    com = st.slider('HOA HỒNG (1 nam, don vi USD1000):', min_value=1, max_value=200)
    comxtra = st.slider('HOA HỒNG THƯỞNG THÊM (1 nam, don vi USD1000):', min_value=1, max_value=200)
    cond = st.text_input('ĐIỀU KIỆN HOA HỒNG THƯỞNG THÊM:', 'USA')
    ttvv = st.text_input('THƯỞNG TVV:', 'TVV')
    time_org = st.text_input('THỜI HẠN THANH TOÁN HOA HỒNG:', '6 THÁNG')
    condp = st.text_input('ĐIỀU KIỆN THANH TOÁN:', 'USA')
    note_org = st.text_input('GHI CHÚ:')
    pers = st.text_input('NGƯỜI ĐẠI DIỆN ĐỐI TÁC:', 'Mr. Smith')
    email_org = st.text_input('EMAIL:', 'abc@xyz.com')
    tel_org = st.text_input('SỐ ĐIỆN THOẠI:', '+0001234567')
    add_org = st.text_input('ĐỊA CHỈ LIÊN LẠC:', '1 Main Str.')
    web = st.text_input('WEBSITE:')
    price_org = st.slider('Giá bán ra (1000USD):', min_value=1, max_value=200)
    fee_org = st.slider('Phí dịch vụ (1000USD):', min_value=1, max_value=200)
    serv = st.selectbox('Dịch vụ bao gồm trong phí trường:', ('Tư vấn chọn ngành học', 'Tư vấn chọn trường', 'Tư vấn chọn nước', 'Dịch thuật', 'Nộp hồ sơ xin trường (tối đa 3 trường)',
                                                           'Nộp hồ sơ xin visa du học', 'Nộp hồ sơ xin visa du lịch', 'Góp ý thư xin học', 'Góp ý bài luận', 'Thu hộ', 'Chi hộ',
                                                           'Hướng dẫn phỏng vấn visa', 'Hướng dẫn trước khi bay', 'Đưa đón sân bay', 'Hỗ trợ trong thời gian học', 'Gia hạn visa/ giấy phép học tập'))
    xserv = st.selectbox('Dịch vụ hỗ trợ-Khách tự trả phí:',('Dịch thuật', 'Mua bảo hiểm', 'Mua vé máy bay', 'Đưa đón sân bay', 'Góp ý thư xin học', 'Góp ý bài luận', 'Thu-đổi nội/ngoại tệ', 'Làm hộ chiếu', 'Gia hạn visa/giấy phép học tập'))
    fserv = st.text_input('Dịch vụ miễn phí:')
    nserv = st.text_input('Ghi chú phí dịch vụ:')
    hhtvv = st.text_input('HH TVV:', '500USD')
    hhtvvcs = st.text_input('HH TVV chăm sóc:', '500USD')
    hhctv = st.text_input('HH CTV:', '500USD')
    condt = st.text_input('Điều kiện trích:')
    bonus = st.text_input('Thưởng thêm:', '500USD')
    condbonus = st.text_input('Điều kiện thưởng thêm:')
    timehh = st.text_input('Thời hạn thanh toán hoa hồng:', '500USD')

    if st.button('Thêm đối tác'):
        # Open the Google Sheet
        sheet = client.open("VNTalent CRM")

        # Get the specific sheets of the Spreadsheet
        sheet_sch = sheet.get_worksheet(0)

        #Process some variables
        aft_scho = (tui - scho)* 1000

        #Append a new row to the Google sheet
        sheet_sch.append_row([ind_org, code_org, name_org, partner, typ, prog, tui*1000, scho*1000, aft_scho, exps, reqr, doc,
                               folder_org, stat_org, signda, expida, com, comxtra, cond, ttvv, time_org, condp, note_org, pers,
                               email_org, tel_org, add_org, web, price_org, fee_org, serv, xserv, fserv, nserv, hhtvv, hhtvvcs,
                               hhctv, condt, bonus, condbonus, timehh
                               ])

        st.write("Đã thêm một trường vào kho dữ liệu.\nXem tất cả dữ liệu tại: https://docs.google.com/spreadsheets/d/1Vturst7dLVikron_-4OMluPjsRUcqqSRV2hHFxytBNI/edit#gid=0")

with tab2:
    ###Students
    ind_stu = st.text_input('STT:', '1')
    code_stu = st.text_input('Mã học sinh:', 'XXX')
    lname = st.text_input('Họ:', 'Nguyen')
    mname = st.text_input('Tên đệm:', 'Thị')
    name = st.text_input('Tên:', 'Hoa')
    gender = st.selectbox('Giới tính:', ('Nam', 'Nữ', 'Khác'))
    dob = st.date_input('Ngày sinh:').strftime("%Y/%m/%d")
    passp = st.text_input('Số hộ chiếu:', 'C12345678')
    passd = st.date_input('Ngày cấp hộ chiếu:').strftime("%Y/%m/%d")
    passxd = st.date_input('Ngày hết hạn hộ chiếu:').strftime("%Y/%m/%d")
    id = st.text_input('Số CMND:', 'C1234567')
    idd = st.date_input('Ngày cấp CMND:').strftime("%Y/%m/%d")
    tel_stu = st.text_input('Điện thoại:', '+00012345678')
    email_stu = st.text_input('Email:', 'abc@xyz2.com')
    cadd_stu = st.text_input('Địa chỉ thường trú:', '3 Main Str.')
    add_stu = st.text_input('Địa chỉ liên lạc (nếu khác địa chỉ thường trú):', '2 Main Str.')
    facebook = st.text_input('Facebook:')
    zalo = st.text_input('Zalo:')
    rellname = st.text_input('Họ người giám hộ:', 'Nguyễn')
    relname = st.text_input('Tên người giám hộ:', 'Văn An')
    gender_rel = st.selectbox('Giới tính người giám hộ:', ('Nam', 'Nữ', 'Khác'))
    rel = st.selectbox('Quan hệ với người du học:', ('Bố', 'Mẹ', 'Anh', 'Chị', 'Khác'))
    id_rel = st.text_input('Số CMND/hộ chiếu người giám hộ:', 'C1234567')
    dob_rel = st.date_input('Ngày sinh người giám hộ:').strftime("%Y/%m/%d")
    tel_rel = st.text_input('Điện thoại người giám hộ:', '+000123456789')
    email_rel = st.text_input('Email người giám hộ:', 'abc@xyz1.com')
    add_rel = st.text_input('Địa chỉ liên lạc người giám hộ:', '4 Main Str.')
    ctv_stu = st.text_input('Tên CTV:')
    tvv = st.text_input('Tên TVV:')
    contractd = st.date_input('Ngày ký hợp đồng:').strftime("%Y/%m/%d")
    contract = st.text_input('Số hợp đồng:')
    prog_stu = st.text_input('Chương trình:')
    school = st.text_input('Trường:')
    term = st.text_input('Kỳ học:')
    serv_stu = st.selectbox('Dịch vụ bao gồm trong phí:', ('Tư vấn chọn ngành học', 'Tư vấn chọn trường', 'Tư vấn chọn nước', 'Dịch thuật',
                                                           'Nộp hồ sơ xin trường (tối đa 3 trường)', 'Nộp hồ sơ xin visa du học', 'Nộp hồ sơ xin visa du lịch',
                                                           'Góp ý thư xin học', 'Góp ý bài luận', 'Thu hộ', 'Chi hộ', 'Hướng dẫn phỏng vấn visa',
                                                           'Hướng dẫn trước khi bay', 'Đưa đón sân bay', 'Hỗ trợ trong thời gian học', 'Gia hạn visa/ giấy phép học tập'))
    fee_stu = st.slider('Tổng phí dịch vụ theo hợp đồng (1000USD):', min_value=1, max_value=200)
    paymeans = st.selectbox('Hình thức thanh toán theo hơp đồng:',
                            ('Tiền mặt', 'Chuyển khoản', 'Tiền mặt/Chuyển khoản'))
    refund = st.selectbox('Quy định hoàn phí theo hơp đồng:',
                            ('100% phí dịch vụ', '100% cọc', '100% phí đã nhận', '100% sau khi trừ phí liên quan', 'Không hoàn phí', 'Theo quy định của trường'))
    refundcond = st.selectbox('Điều kiện refund:',
                              ('Không xin được trường', 'Không xin được visa', 'Chương trình bị huỷ', 'Theo quy định của trường'))
    folder_stu = st.text_input('Link folder hồ sơ:', 'Link folder')
    stat_stu = st.selectbox('Tình trạng hồ sơ:',('Đang tư vấn', 'Đang chờ xin trường', 'Đang chờ xin visa', 'Đang chờ bay', 'Hoàn tất/giữ liên lạc'))
    colfee1 = st.slider('Phí thu đợt 1 (1,000,000 VND):', min_value=1, max_value=200)
    colfeeda1 = st.date_input('Ngày thu phí đợt 1:').strftime("%Y/%m/%d")
    colfeemeans1 = st.selectbox('Hình thức thu đợt 1:',
                            ('Tiền mặt', 'Chuyển khoản', 'Tiền mặt/Chuyển khoản'))
    colfee2 = st.slider('Phí thu đợt 2 (1,000,000 VND):', min_value=1, max_value=200)
    colfeeda2 = st.date_input('Ngày thu phí đợt 2:').strftime("%Y/%m/%d")
    colfeemeans2 = st.selectbox('Hình thức thu đợt 2:',
                                ('Tiền mặt', 'Chuyển khoản', 'Tiền mặt/Chuyển khoản'))
    colfee3 = st.slider('Phí thu đợt 3 (1,000,000 VND):', min_value=1, max_value=200)
    colfeeda3 = st.date_input('Ngày thu phí đợt 3:').strftime("%Y/%m/%d")
    colfeemeans3 = st.selectbox('Hình thức thu đợt 3:',
                                ('Tiền mặt', 'Chuyển khoản', 'Tiền mặt/Chuyển khoản'))
    hh_stu = st.slider('Mức hoa hồng theo %:', min_value=1, max_value=100)
    hhval = st.text_input('Mức hoa hồng theo số tiền:')
    curency = st.selectbox('Đơn vị tiền tệ:', ('USD', 'AUD', 'CAD', 'GBP', 'CHF', 'EUR', 'MYR', 'SGD', 'BAHT', 'RMB', 'VND'))
    curx = st.text_input('Chuyển đổi VND:')
    da1 = st.date_input('Ngày đợt 1:').strftime("%Y/%m/%d")
    da2 = st.date_input('Ngày đợt 2:').strftime("%Y/%m/%d")
    da3 = st.date_input('Ngày đợt 3:').strftime("%Y/%m/%d")
    da4 = st.date_input('Ngày đợt 4:').strftime("%Y/%m/%d")
    da5 = st.date_input('Ngày đợt 5:').strftime("%Y/%m/%d")
    da6 = st.date_input('Ngày đợt 6:').strftime("%Y/%m/%d")
    concda = st.date_input('Ngày thanh lý:').strftime("%Y/%m/%d")
    concnum = st.text_input('Số thanh lý:')
    concrea = st.text_input('Lý do thanh lý:')
    concfold = st.text_input('Link file thanh lý:')
    concnot = st.text_input('Ghi chú thanh lý:')

    if st.button('Thêm học sinh'):
        # Open the Google Sheet
        sheet = client.open("VNTalent CRM")

        # Get the specific sheets of the Spreadsheet
        sheet_stu = sheet.get_worksheet(1)

        # Process some variables
        colfeetol = (colfee1 + colfee2 + colfee3)*1000000

        # Add a row to the Google Sheet
        sheet_stu.append_row([
            ind_stu, code_stu, lname, mname, name, gender, dob, passp, passd, passxd, id, idd, tel_stu, email_stu, cadd_stu,
            add_stu, facebook, zalo, rellname, relname, gender_rel, rel, id_rel, dob_rel, tel_rel, email_rel, add_rel, ctv_stu,
            tvv, contractd, contract, prog_stu, school, term, serv_stu, fee_stu, paymeans, refund, refundcond, folder_stu,
            stat_stu, colfee1*1000000, colfeeda1, colfeemeans1, colfee2*1000000, colfeeda2, colfeemeans2, colfee3*1000000,
            colfeeda3, colfeemeans3, hh_stu, hhval, curency, curx, da1, da2, da3, da4, da6, concda, concnum, concrea, concfold, concnot
        ])

        st.write("Đã thêm một học sinh vào kho dữ liệu.\nXem tất cả dữ liệu tại: https://docs.google.com/spreadsheets/d/1Vturst7dLVikron_-4OMluPjsRUcqqSRV2hHFxytBNI/edit#gid=884939537")

with tab3:
    ###Cộng tác viên
    ctvind = st.text_input("Mã CTV:")
    ctv = st.text_input('Cộng tác viên:')
    rep = st.text_input('Đại diện liên lạc:')
    tel_ctv = st.text_input('Điện thoại:')
    email_ctv = st.text_input('Email:')
    add_ctv = st.text_input('Địa chỉ:')
    stat_ctv = st.selectbox('Tình trạng hợp đồng', ('Đã ký', 'Chưa ký'))
    date_ctv = st.date_input('Ngày ký hợp đồng CTV:').strftime("%Y/%m/%d")
    xdate_ctv = st.date_input('Ngảy hết hạn:').strftime("%Y/%m/%d")
    pro_ctv = st.text_input('Chương trình phụ trách:')
    hh_ctv = st.slider('Mức hoa hồng CTV theo %:', min_value=1, max_value=100)
    hhval_ctv = st.text_input('Mức hoa hồng CTV theo số tiền:')
    num = st.text_input('Số lượng:')
    hhcond = st.text_input('Điều kiện hoa hồng CTV:')
    xhh = st.slider('% hoa hồng thưởng thêm CTV:', min_value=1, max_value=100)
    xhhcond = st.text_input('Điều kiện hoa hồng thưởng thêm CTV:')
    fee_ctv = st.slider('Phí dịch vụ CTV (1,000,000VND):', min_value=1, max_value=100)
    feenot = st.text_input('Ghi chú phí dịch vụ CTV:')
    hhtime = st.text_input('Thời hạn thanh toán hoa hồng CTV:')
    folder_ctv = st.text_input('Link folder thepo dõi hợp đồng:')
    note_ctv = st.text_input('Ghi chú CTV:')

    if st.button('Thêm CTV'):
        # Open the Google Sheet
        sheet = client.open("VNTalent CRM")

        # Get the specific sheets of the Spreadsheet
        sheet_sta = sheet.get_worksheet(2)

        # Add a row to Google sheet
        sheet_sta.append_row([
            ctvind, ctv, rep, tel_ctv, email_ctv, add_ctv, stat_ctv, date_ctv, xdate_ctv, pro_ctv, hh_ctv, hhval_ctv, num,
            hhcond, xhh, xhhcond, fee_ctv, feenot, hhtime, folder_ctv, note_ctv
        ])

        st.write("Đã thêm một CTV vào kho dữ liệu.\nXem tất cả dữ liệu tại: https://docs.google.com/spreadsheets/d/1Vturst7dLVikron_-4OMluPjsRUcqqSRV2hHFxytBNI/edit#gid=207075816")
