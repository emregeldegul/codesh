from os import path, environ
from json import loads, dump
from time import strftime
from requests import post
from re import findall
from sys import argv
from pyperclip import copy

class sh:
    """
        this module, shares source codes at paste.ubuntu.com

        from codesh import sh

        app = sh()
        app.main("file.txt")

        and this command lists the last shared files.

        app.jData
    """
    def __init__(self, username):
        self.checkFile = lambda file: path.exists(file)
        self.parseFile = lambda file: path.splitext(file)
        self.username = username

        self.jsonFile = path.join(environ['HOME'], "codesh.json")

        if not self.checkFile(self.jsonFile):
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
        if not self.checkFile(file):
            raise FileNotFoundError("File {0} Not Found!".format(file))
        else:
            pasteUrl = self.share(self.parseFile(file))

            data = {"id": pasteUrl, "time": strftime('%c'), "poster": self.username}

            self.jData.append(data)

            with open(self.jsonFile, 'w') as outfile:
                dump(self.jData, outfile, sort_keys=True, indent=4)

            return pasteUrl

if __name__ == "__main__":
    app = sh(username=environ['USER'])

    if len(argv) == 1:
        print("Using:")
        print("\t~$ python codesh.py [*files]")
        print("\t~$ python codesh.py --list (List Of Last Shares)")
        print("\nModule Usage:")
        print("\tfrom codesh import sh\n\tapp = sh(username='nickname')\n\tapp.main('filename.txt')")
        print("\n\tapp.jData # this object returns the last link list")
    else:
        if argv[1] == "--list":
            for i in app.jData:
                print("ID: {}, Time: {}, Poster: {}".format(i["id"], i["time"], i["poster"]))
        else:
            del argv[0]
            for result in list(map(app.main, argv)):
                url = "https://paste.ubuntu.com/p/"+str(result)
                copy(url)
                print(url)