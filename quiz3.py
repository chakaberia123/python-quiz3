import requests
import json

CountryCode = input("CountryCode:")
Year = int(input("Year:"))
Month = int(input("Month:"))
Day = int(input("Day:"))
key = '298768c710304d2b8d45620267bcea4f'
url = f'https://holidays.abstractapi.com/v1/?api_key={key}&country={CountryCode}&year={Year}&month={Month}&day={Day}'
r = requests.get(url)
print(r.status_code)
print(r.headers)
result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=3)
print(res_structured)
week_day = res[0]['week_day']
print('week day =', week_day)

with open('data.json', 'w') as file:
    object = json.dump(res, file, indent=4)

import sqlite3

conn = sqlite3.connect("mydata.sqlite")
cursor = conn.cursor()

Rlocation = res[0]['location']
Rname = res[0]['name']
Rdate = res[0]['date']

# cursor.execute('''CREATE TABLE Holliday
#
#         (id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Country VARCHAR(50),
#         HollidayName VARCHAR(100),
#         HollidayDate FLOAT);''')

cursor.execute('INSERT INTO Holliday(Country, HollidayName, HollidayDate) VALUES (?, ?, ?)', (Rlocation, Rname, Rdate))
conn.commit()

conn.close()
# აქედან ცხრილში შეგვაქ ქვეყნის სახელი, დღესასწაულის სახელი და თარიღი