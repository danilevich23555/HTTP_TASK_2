from pprint import pprint

import requests


from ya_disk import YandexDisk

TOKEN = ""




if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk("test", "test.txt")

