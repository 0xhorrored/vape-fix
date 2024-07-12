import urllib.request
import subprocess
import os
import threading

url = "https://github.com/0xhorrored/vape-fix/raw/main/RunAsDate.exe"
download_path = "RunAsDate.exe"
print("cracked by Decencies, fixed by 0xhorrored")
print("if there's any error during bind, remove the default profile")

def download(url, save_path):
    if not os.path.exists(save_path):
        with urllib.request.urlopen(url) as response, open(save_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

download(url, download_path)

spoof = r'RunAsDate.exe 19\09\2023 13:37:37 Attach:cmd.exe & RunAsDate.exe 19\09\2023 13:37:37 Attach:cmdjavaw.exe'
command = r'java --add-opens java.base/java.lang=ALL-UNNAMED -jar vape-loader.jar'

def run_spoof():
    subprocess.call(spoof)
    print("spoofed date/time")

def run_command():
    subprocess.call(command)

thread_spoof = threading.Thread(target=run_spoof)
thread_command = threading.Thread(target=run_command)

thread_spoof.start()
thread_command.start()

thread_spoof.join()
thread_command.join()
