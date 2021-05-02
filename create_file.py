import os
import time

file_time = time.strftime('%Y%m%d%H%M%S')

class createFile:
    def __init__(self):
        pass
    
    def createTxt(self):
        f = open(file_time + '.txt', 'tw', encoding='utf-8')
        f.close()

class createHtml(createFile):
    def __init__(self):
        pass


    tags = ['<!DOCTYPE html>',
            '<html>',
            '<head>',
            '',
            '</head>',
            '',
            '<body>',
            '',
            '<script>',
            '',
            '</script>',
            '',
            '</body>',
            '</html>']
    
    def create_fill_and_rename(self):
        super().createTxt()
        with open(file_time + '.txt', 'w') as f:
            f.writelines("%s\n" % tag for tag in self.tags)
        os.rename(file_time + '.txt', file_time + '.html')

class createPy(createFile):
    def __init__(self):
        pass

    def create_rename(self):
        super().createTxt()
        os.rename(file_time + '.txt', file_time + '.py')

if __name__ == "__main__":
    htmlFile = createHtml()
    htmlFile.create_fill_and_rename()

    pyFile = createPy()
    pyFile.create_rename()