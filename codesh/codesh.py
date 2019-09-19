from os import path
from re import findall
from time import strftime
from requests import post
from json import loads, dump

class sh:
    """
        this module, shares source codes at paste.ubuntu.com

        from codesh import sh

        app = sh()
        app.main("file.txt")

        and this command lists the last shared files.

        app.jData
    """

    def __init__(self, username = 'codesh'):
        self.username = username
        self.jsonFile = path.join(path.expanduser("~"), ".codesh.json")

        if not path.exists(self.jsonFile):
            with open(self.jsonFile, 'w') as outfile:
                dump([], outfile)

        self.jData = loads(open(self.jsonFile, "r").read())

    def findUrl(self, text):
        return findall('<a class="pturl" href="/p/(.*?)/plain/">Download as text</a>', text)[0]

    def lang(self, lang):
        return {
            '.py': "python",
            '.cs': "csharp",
            '.php': "php",
            '.css': "css",
            ".pl": "perl",
            ".rb": "rb",
            ".css": "css",
            ".sh": "bash",
            ".go": "go",
            ".html": "html",
            ".js": "js"
        }.get(lang, "text")

    def share(self, file):
        fileName, ext = file
        code = open(fileName+ext, "r").read()
        syntax = self.lang(ext)

        data = {"content": code, "syntax": syntax, "poster": self.username}
        request = post("https://paste.ubuntu.com/", data=data)

        return self.findUrl(request.text)

    def main(self, file):
        if not path.exists(file):
            raise FileNotFoundError("File {0} Not Found!".format(file))
        else:
            pasteUrl = self.share(path.splitext(file))
            data = {"id": pasteUrl, "time": strftime('%c'), "poster": self.username}
            self.jData.append(data)
            with open(self.jsonFile, 'w') as outfile:
                dump(self.jData, outfile, sort_keys=True, indent=4)
            return pasteUrl
