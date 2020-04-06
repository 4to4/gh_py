import requests
import sys
import os
import wget

# static vars

source_file_url = "https://data.baltimorecity.gov/resource/27w9-urtv.json"


def download_save():
    resp = requests.get(source_file_url)
    print(wget.download(source_file_url, out=r'C:\Users\root\AppData\Local\Temp'))


def main():
    download_save()


if (__name__ == "__main__"):
    main()
