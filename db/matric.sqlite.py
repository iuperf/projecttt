import sqlite3

connection = sqlite3.connect('inform.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS OVEN
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS TELEZ
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS BLIZNEZI
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RAK
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS LEB
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS DEVA
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VECI
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS SKORPION
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CTRELEZ
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS KOZA
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VODOLEI
              (Title TEXT, Director TEXT, Year INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RIBA
              (Title TEXT, Director TEXT, Year INT)''')
connection.commit()
connection.close()
