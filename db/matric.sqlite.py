import sqlite3

connection = sqlite3.connect('inform.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS OVEN
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS TELEZ
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BLIZNEZI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RAK
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS LEB
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS DEVA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VECI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS SKORPION
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CTRELEZ
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS KOZA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VODOLEI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RIBA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')
connection.commit()
connection.close()
