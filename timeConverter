import sqlite3
import datetime

def convert_to_human_date(millis_str):
    time_inmilis = int(millis_str)
    time = time_inmilis / 1000.0
    date = datetime.datetime.fromtimestamp(time)
    return date.strftime('%Y-%m-%d %H:%M:%S')

database = '/home/black-water/Desktop/Time_converter/newsfeed.db'

conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("ALTER TABLE home_stories ADD COLUMN fetched_at_human_readable TEXT;")

cursor.execute("SELECT dedup_key, fetched_at FROM home_stories;")
rows = cursor.fetchall()

for dedup_key, fetched_at in rows:
    human_readable_date = convert_to_human_date(fetched_at)
    cursor.execute("UPDATE home_stories SET fetched_at_human_readable = ? WHERE dedup_key = ?;",
                   (human_readable_date, dedup_key))

conn.commit()
print("Database updated with human readable time")
conn.close()
