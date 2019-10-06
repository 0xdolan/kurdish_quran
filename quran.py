import sqlite3


conn = sqlite3.connect('qurankurdish.db')

# For finding an unknown db headers
##cur = conn.cursor()
##
##cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
##rows = cur.fetchall()
##for row in rows:
##    print(row[0])

"""
sqlite_sequence
quran_corpus
bywords
tafaseer
sora
audio
aya
surah_name
quran
stocks
"""

# Parse the translation_raman
cur = conn.cursor()
cur.execute("SELECT translation_raman FROM quran")
rows = cur.fetchall()
for row in rows:
    for text in row:
        with open('translation_raman.txt', 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')
    
# Parse the translation_puxta
cur = conn.cursor()
cur.execute("SELECT translation_puxta FROM quran")
rows = cur.fetchall()
for row in rows:
    for text in row:
        with open('translation_puxta.txt', 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')
            

# Parse the translation_asan
cur = conn.cursor()
cur.execute("SELECT translation_asan FROM quran")
rows = cur.fetchall()
for row in rows:
    for text in row:
        with open('translation_asan.txt', 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')
            
# Parse the translation_sanahi
cur = conn.cursor()
cur.execute("SELECT translation_sanahi FROM quran")
rows = cur.fetchall()
for row in rows:
    for text in row:
        with open('translation_sanahi.txt', 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')
            
# Parse the quran_arabic
cur = conn.cursor()
cur.execute("SELECT quran_arabic FROM quran")
rows = cur.fetchall()
for row in rows:
    for text in row:
        with open('quran_arabic.txt', 'a', encoding='utf-8') as f:
            f.write(str(text) + '\n')
            
