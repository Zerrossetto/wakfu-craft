import os, sqlite3

WE_BASE_URL = "http://wakfu-elements.com"
WE_ITEM_PATH = "/items/type"
INSERT_ITEM = "INSERT INTO item VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)"
SPIDER_HEADERS = [("User-agent", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Ubuntu/12.10 Chromium/22.0.1229.94 Chrome/22.0.1229.94 Safari/537.4"), ("Content-type", "text/html; charset=utf-8")]

DB_LOCATION = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "data", "db.sqlite")

def db_commit(data):
    db = sqlite3.connect(DB_LOCATION)
    c = db.cursor()
    c.executemany(INSERT_ITEM, data)
    db.commit()
    print "Successfully wrote %s" % data
    db.close()

