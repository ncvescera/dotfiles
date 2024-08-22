#!/usr/bin/python

import os
import sys
import subprocess
import urllib.request
from urllib.parse import urlparse
from urllib.request import urlopen, URLError


def validate_web_url(url="http://google"):
    try:
        urlopen(url)
        return True
    except URLError:
        return False
    except ValueError:
        return False


def main():
    # run zathura without arguments
    if len(sys.argv) <= 1:
        subprocess.run(["zathura"]) 
        return
    
    arg = sys.argv[1]

    if validate_web_url(arg):
        # valid url, download and open PDF
        file_path = "/tmp/za.pdf"
        urllib.request.urlretrieve(arg, file_path)

        os.system(f"zathura {file_path} && rm {file_path} &")

    else:
        os.system(f"zathura {arg} &")


if __name__ == "__main__":
    main()    

