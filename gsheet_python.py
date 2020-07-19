import pygsheets
import pandas as pd

#authorization
gc = pygsheets.authorize(service_file='gsheet_api_key.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['col1'] = ['val1', 'val2', 'val3']
df['col2'] = ['val4', 'val5', 'val6']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sheet = gc.open('gsheet_python')

#select the first sheet 
worksheet = sheet[0]

#update the first sheet with df, starting at cell B2. 
worksheet.set_dataframe(df,(1,1))