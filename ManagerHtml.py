class HtmlManager:
    def __init__(self, my_doc):
        self.my_doc = my_doc

    def creating_html(self):
        file = open('demo.html', 'w')
        
        content = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        file.write(content)
        file.close()


    def saving_html(self):
        with open("demo.html","w") as file:
            file.write(self.my_doc)
