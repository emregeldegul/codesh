from .codesh import sh
from getpass import getuser
from pyperclip import copy
from sys import argv

def main():
    app = sh(username = getuser())

    # TODO: Add Argument Parser

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

if __name__ == "__main__":
    main()
