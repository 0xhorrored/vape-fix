import urllib.request
import subprocess
import os

url = "https://github.com/0xhorrored/vape-fix/raw/main/RunAsDate.exe"

download_path = "RunAsDate.exe"
print("cracked by Decencies,fixed by 0xhorrored")
print("if theres any error during bind,remove the default profile")
def download(url, save_path):
    if not os.path.exists(save_path):
        with urllib.request.urlopen(url) as response, open(save_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
download(url, download_path)
spoof = r'RunAsDate.exe 19\09\2023 13:37:37 Attach:javaw.exe'
command = r'java --add-opens java.base/java.lang=ALL-UNNAMED -jar vape-loader.jar'
subprocess.call(spoof)
print("spoofed date/time")
subprocess.call(command)