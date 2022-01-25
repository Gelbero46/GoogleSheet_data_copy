from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import io
import pandas as pd
import requests
import csv
import sys


from google.oauth2 import service_account


# sys.argv[0]
if len(sys.argv) != 3:
    print("wrong input")
    sys.exit()
"""
    Install python:
    python.org

    Run the code below to install packages needed in cmd terminal:
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

    In terminal supply sheet_ID and sheet_name to the program:
    python <program name> <sheet_id> <sheet_name>
    Example: python excel.py 1Ud-xYjmMM83hlVFjLkJxcd7jm0_fe4uEOhcep9hzyJU sheet_1
"""

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = "keys.json"

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'Put the setup google sheet ID'

service = build('sheets', 'v4', credentials=creds)


    # Call the Sheets API
sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet1!A1:H1").execute()
# print(result)




# sheet_id = "1GTFtXQVLFRigaFt2AyVFm1wIVQzUUB6C"
# sheet_name = "Sheet1"
sheet_id = sys.argv[1]
sheet_name = sys.argv[2]
# sys.argv[0]
 
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

res = requests.get(url)
print(res)
with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr_1 = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list_1 = list(cr_1)
#    print(len(my_list_1))
    my_list_1 = my_list_1[1:]
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                            range="Sheet1!A1", valueInputOption="USER_ENTERED", insertDataOption="OVERWRITE", body={"values":my_list_1})
    response = request.execute()
    print(my_list_1)
    for row in my_list_1:
        print(row)

