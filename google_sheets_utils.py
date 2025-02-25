from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = r'C:\rag3\rich-tome-451605-k3-978ee6731aa6.json'
SPREADSHEET_ID = '1X0kO-Xz6rnV4g8-SL5uLh9G1VgSxdWBH1JYg3aAPU0Q'

def get_google_sheets_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

def save_chat_to_sheets(question, answer):
    try:
        service = get_google_sheets_service()
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        values = [[
            timestamp,
            question,
            answer
        ]]
        
        body = {
            'values': values
        }
        
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range='Sheet1!A:C',  # Adjust range as needed
            valueInputOption='RAW',
            body=body
        ).execute()
        
        return True
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")
        return False