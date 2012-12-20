import HTMLParser

class Item:
    
    def __init__(self):
        self.icon=""
        self.acquired=""
        self.stats=""
        self.lvl=0
        self.name=""
        self.type=""
        self.id_elements=0
        
    def __repr__(self):
        return "%5s %30s %21s %3s" % (self.id_elements, self.name, self.icon, self.lvl)

class ItemParser(HTMLParser.HTMLParser):
    
    def __init__(self, job, category):
        HTMLParser.HTMLParser.__init__(self)
        self.job = job
        self.category = category
        self.recording = False
        self.data = []
        self.item = None
        self.attr_scope = ""
    
    def __repr__(self):
        tmp = "%5s %30s %21s %3s %10s %10s" % ("id", "name", "icon", "lvl", "resource", "category")
        for i in self.data:
            tmp += "\n%s %10s %10s" % (i, self.job, self.category)
        return tmp
    
    def handle_starttag(self, tag, attrs):   
        if self.recording:
            try:
                getattr(self, "start_%s" % tag)(attrs)
            except AttributeError:
                pass
        else: 
            if tag == "table":
                self.recording = True 

    def handle_endtag(self, tag):
        try:
            getattr(self, "end_%s" % tag)()
        except AttributeError:
            pass

    def handle_data(self, data):
        if self.recording:
            try:
                getattr(self, "do_%s" % self.attr_scope)(data)
            except AttributeError:
                pass
                
    def start_tr(self, attrs):
        self.item = Item()
    
    def start_td(self, attrs):
        scope = [v[5:] for k, v in attrs if k=="class"][0]
        self.attr_scope = scope
        
    def start_a (self, attrs):
        if self.attr_scope == "icon":
            href = [v for k, v in attrs if k=="href"][0]
            self.item.id_elements = int(href.split("/")[-1])
            
    def start_img (self, attrs):
        if self.attr_scope == "icon":
            src = [v[5:] for k, v in attrs if k=="src"]
            self.item.icon = src[0]
    
    def end_table(self):
        self.recording = False
        
    def end_tr(self):
        self.data.append(self.item)
        
    def end_td(self):
        self.attr_scope = None
        
    def do_name(self, data):
        dstrip = data.strip()
        if dstrip:
            setattr(self.item, self.attr_scope, unicode(dstrip))
    
    def do_acquired(self, data):
        self.do_name(data)
    
    def do_lvl(self, data):
        self.item.lvl = int(data)
