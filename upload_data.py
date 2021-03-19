import pandas as pd
from sqlalchemy import create_engine
from openpyxl import load_workbook
#
# DBNAME=singer
# USERNAME=singerdb
# PASSWORD=Neenopal2018
# HOSTNAME=singerdb.cqz0ja6v7m9f.us-east-1.rds.amazonaws.com
# PORT=3306

db_uri="mysql://singerdb:Neenopal2018@singerdb.cqz0ja6v7m9f.us-east-1.rds.amazonaws.com:3306/singer"
engine = create_engine(db_uri, echo=True)

df = pd.read_excel("Copy of MMM Data Capture Format.xlsx", sheet_name="Copy of Others", engine='openpyxl')
df = df[df['Product Category'].notna()]
print(df)
df['Campaign From Date'] = df['Campaign From Date'].str.replace(' 00:00:00','')
df['Campaign To Date'] = df['Campaign To Date'].str.replace(' 00:00:00','')
df.rename(columns={'Campaign From Date': 'CAMPAIGN_FROM_DATE', 'Campaign To Date': 'CAMPAIGN_TO_DATE', 'Promotion Type': 'PROMOTION_TYPE', 'Product Category': 'PRODUCT_CATEGORY', 'Objective': 'OBJECTIVE'
, 'Campaign Type': 'CAMPAIGN_TYPE', 'SINGER Channel': 'SINGER_CHANNEL', 'Medium':'MEDIUM', 'Details (TV Channel, Newspaper, Website / Other details)': 'DETAILS', 'Time Slot / Page': 'TIME_SLOT_PAGE', 'Seconds/Size': 'SECONDS_SIZE', 'Spend in LKR': 'SPEND_LKR'
, 'Language': 'LANGUAGE' , 'Brand': 'BRAND', 'Province': 'PROVINCE', 'District': 'DISTRICT'}, inplace=True)
#df.DURATION = df.DURATION.astype(int)

print(df)
df.to_sql('marketing_mix_modeling_master', con=engine, if_exists='append', index=False  )
#engine.execute("SELECT * FROM marketing_mix_modeling_master").fetchall()

# df = df[df['Product_Group'].notna()]
# df.rename(columns={'Product_Group': 'PRODUCT_CATEGORY', 'Advertiser': 'ADVERTISER', 'varient ': 'VARIENT', 'Channel': 'CHANNEL', 'Program': 'PROGRAM'
# , 'Day': 'DAY', 'Advt_time': 'ADVT_TIME', 'Lng': 'LANGUAGE', 'Dur': 'DURATION', 'Actual Spend': 'ACTUAL_SPEND', 'Monitored Spend ': 'MONITORED_SPEND'}, inplace=True)
# df.DURATION = df.DURATION.astype(int)
# df["DATE"] = df["Yr"].astype(int).astype(str) + "-" + df["Mn"].astype(int).astype(str) + "-" + df["Dd"].astype(int).astype(str)
# del df['Dd']
# del df['Mn']
# del df['Yr']
# print(df)
# df.to_sql('neilson_data_master', con=engine, if_exists='append', index=False  )
# engine.execute("SELECT * FROM neilson_data_master").fetchall()
