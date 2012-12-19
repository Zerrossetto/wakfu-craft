#Python Package
WE_BASE_URL = "http://wakfu-elements.com"
WE_ITEM_PATH = "/items/type"
SPIDER_HEADERS = [("User-agent", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Ubuntu/12.10 Chromium/22.0.1229.94 Chrome/22.0.1229.94 Safari/537.4"),
           ("Content-type", "text/html; charset=utf-8")]

LOCAL_ITEM_QUERY="INSERT INTO item (name, level, acquired, stats, icon, type, job, id_elements) VALUES (?, ?, ?, ?, ?, ?, ?)"