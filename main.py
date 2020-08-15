class HtmlDocument:
    def __init__(self):
        pass

class HtmlManager:
    def __init__(self):
        pass
    def creating_html(self):
        file = open('demo.html', 'wb')
        
        content = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        file.write(content)
        file.close()
    


class AWSManager:
    def __init__(self):
        pass

    