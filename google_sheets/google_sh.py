import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'google_sheets/credentials.json'
base_spreadsheet_id = '10pyDQtt-kNIYUtIeH9_HTtxNyGqbBINiDi-m64lGDG0'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


def read_from_google_sheet(spreadsheet_id=base_spreadsheet_id, from_element='A1', to_element='A1'):
    data = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{from_element}:{to_element}',
        majorDimension='COLUMNS'
    ).execute()
    return data["values"]

def write_to_google_sheet(spreadsheet_id=base_spreadsheet_id, data=()):
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=base_spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": data
        }
    ).execute()