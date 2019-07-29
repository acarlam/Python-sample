#download_arquivo.py
#coding: utf-8
import io
import sys 
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded {}".format((((time * BUFF_SIZE)/LENGTH)*100)))

def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break    

if __name__ == "__main__":
    
    

