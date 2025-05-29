import gspread
from gspread_formatting import *
from datetime import datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials

folder_id = FOLDER_ID
file_name = 'GC_test_by_gspread'

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SETTING,
    scopes=scopes
)

gc = gspread.authorize(credentials)

def createNewDayReport():
    daysheet = gc.create('TestDayReport',folder_id)
    worksheet = daysheet.sheet1
    worksheet.update_title("日報シート")
    worksheet.update('A1',[['日報']])
    header = ["始業時間","終業時間",'作業場所',"作業内容","納品物","請求先","WorkTime","登録者"]

    for i, header in enumerate(header, 1):
        worksheet.update_cell(2,i,header)

    return worksheet

def checkin(sheet):
    current_date = datetime.now().strftime("%Y/%m/%d %H:%M:00")
    raw_value = get_next_empty_row(sheet,1)
    sheet.update(f"A{raw_value}",[[current_date]],value_input_option='USER_ENTERED')
    return sheet

def checkout(sheet):
    current_date = datetime.now().strftime("%Y/%m/%d %H:%M:00")
    raw_value = get_next_empty_row(sheet,2)
    sheet.update(f"B{raw_value}",[[current_date]],value_input_option='USER_ENTERED')
    sheet.update(f"G{raw_value}", [[f'=B{raw_value}-A{raw_value}']], value_input_option='USER_ENTERED')
    fmt = cellFormat(numberFormat=NumberFormat(type='TIME', pattern='[hh]:mm'))
    format_cell_range(sheet, f"G{raw_value}", fmt)
    return sheet

def get_next_empty_row(worksheet,col):
    """
    次の空行を取得
    """
    try:
        # 与えられた列の取得
        values = worksheet.col_values(col)
        # ヘッダー行（1-2行目）をスキップして、最初の空行を探す
        for i in range(2, len(values) + 1):
            if i >= len(values) or not values[i]:
                return i + 1
        return len(values) + 1
    except Exception as e:
        print(f"空行取得エラー: {e}")
        return 3