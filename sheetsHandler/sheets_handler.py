import gspread
from oauth2client.service_account import ServiceAccountCredentials

def start_sheets_handler():
    json_keyfile = '../credentials.json'
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(creds)
    return client

def getEmails(url, client):
    sheet = client.open_by_url(url)
    worksheet = sheet.get_worksheet(0)

    return worksheet.col_values(1)

