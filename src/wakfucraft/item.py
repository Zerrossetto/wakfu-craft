import HTMLParser

class Item:
    
    def __init__(self):
        self.icon=""
        self.acquired=""
        self.stats=""
        self.level=0
        self.name=""
        self.type=""
        self.icon=""
        self.id_elements=0
        
    def __repr__(self):
        return vars(self).__repr__()

class ItemParser(HTMLParser.HTMLParser):
    
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.recording = False
        self.data = []
        self.item = None
        self.attr_scope = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.recording = True
        if self.recording:
            if tag == "tr":
                self.item = Item()
            if tag == "td":
                self.attr_scope = attrs[0][1]
            if tag == "a" and self.attr_scope == "item_icon":
                self.item.id_elements = int( attrs[0][1].split("/")[-1] )
            if tag == "img":
                self.item.icon = attrs[0][1]
                
    def handle_endtag(self, tag):
        if tag == "table":
            self.recording = False
        if tag == "tr":
            self.data.append(self.item)
        if tag == "td":
            self.attr_scope = ""
    
    def handle_data(self, data):
        if self.recording:
            if self.attr_scope in ["item_name", "item_aquire"]:
                dstrip = data.strip()
                if dstrip:
                    setattr(self.item, item_table_mapping[self.attr_scope], unicode(dstrip))
            if self.attr_scope == "item_lvl":
                self.item.level = int(data)
