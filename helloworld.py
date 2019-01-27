import subprocess
import os
from os import path


def main():
    print(path.exists("/home/flekenstine/Desktop"))
    if(str(path.exists("/home/flekenstine/Desktop/img.jpg")== "true")):
        print(path.realpath("new.txt"))
        print(subprocess.run(["gsettings", "get" ,"org.gnome.desktop.background", "picture-uri"]));
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri","file:///home/flekenstine/Desktop/img.jpg"]);
        

main()