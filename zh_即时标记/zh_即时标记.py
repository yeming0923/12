class Handler:
    def callback(self,prefix,name,*args):
        method =getattr(self,prefix+name,None)
        if callable(method):return method(*args)
    def start(self,name):
        self.callback('start_',name)
    def end(self,name):
        self.callback('end_',name)
    def sub(self, name):
        def substitution(match):
            result=self.callback('sub_',name,match)
            if result is None:match.group(0)
            return result
        return substitution
class HTMRenderer(Handler):
    def start_document(self):
        print ('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body><html>')
    def start_paragraph(self):
        print('<p>')
