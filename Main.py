from __future__ import annotations
import time
import os
# 用于显示进度条
from tqdm import tqdm
# 用于发起网络请求
import requests
# 用于多线程操作
import multitasking
import signal
#导入 retry 库以方便进行下载出错重试
from retry import retry
a=os.getcwd()
try:
  os.mkdir(a+'//temp')
except:
  time.sleep(1)
if 1==1:
  jdka=input('需要jdk吗？(y/n)')
  if jdka=='y':
    print('即将下载jdk......')
    def download(url: str, file_name: str):
        '''
        根据文件直链和文件名下载文件

        Parameters
        ----------
        url: 文件直链
        file_name : 文件名（文件路径）

        '''
        # 文件下载直链
        # 请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }

        # 发起 head 请求，即只会获取响应头部信息
        head = requests.head(url, headers=headers)
        # 文件大小，以 B 为单位
        file_size = head.headers.get('Content-Length')
        if file_size is not None:
            file_size = int(file_size)
        response = requests.get(url, headers=headers, stream=True)
        # 一块文件的大小
        chunk_size = 1024
        bar = tqdm(total=file_size, desc=f'下载文件 {file_name}')
        with open(file_name, mode='wb') as f:
            # 写入分块文件
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(chunk_size)
        # 关闭进度条
        bar.close()


    if "__main__" == __name__:
        url = 'https://download.oracle.com/java/20/latest/jdk-20_windows-x64_bin.msi'
        file_name = 'jdk_setup.msi'
        download(url, file_name)
    print('安装java到相对路径java下')
    os.mkdir(a+'//java（Please setup in here）')
    os.system('jdk_setup.msi')
    os.system('pause')
  try:
    print('即将创建server文件夹......')
    os.system('pause')
    print('当前所在目录：',a)
    os.mkdir(a+'//server')
    print('创建成功！')
  except:
    print('已有server文件夹，跳过创建步骤！')
  sjr=input('需要server.jar吗(y/n)')
  if sjr=='y':
    print('即将下载server.jar......')
    def download(url: str, file_name: str):
        '''
        根据文件直链和文件名下载文件

        Parameters
        ----------
        url: 文件直链
        file_name : 文件名（文件路径）

        '''
        # 文件下载直链
        # 请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }

        # 发起 head 请求，即只会获取响应头部信息
        head = requests.head(url, headers=headers)
        # 文件大小，以 B 为单位
        file_size = head.headers.get('Content-Length')
        if file_size is not None:
            file_size = int(file_size)
        response = requests.get(url, headers=headers, stream=True)
        # 一块文件的大小
        chunk_size = 1024
        bar = tqdm(total=file_size, desc=f'下载文件 {file_name}')
        with open(file_name, mode='wb') as f:
            # 写入分块文件
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(chunk_size)
        # 关闭进度条
        bar.close()


    if "__main__" == __name__:
        url = 'https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar'
        file_name = 'server.jar'
        download(url, file_name)
    os.system('move server.jar server')
  with open('start.bat','w+') as f:
    f.write('java.exe -Xmx1024M -Xms1024M -jar server.jar nogui')
    f.close()
  os.system('move start.bat server')
  os.system('pause')
  os.system('cd server')
  os.system('java.exe -Xmx1024M -Xms1024M -jar server\server.jar nogui')
  os.system('pause')
  c=input('是否同意eula的使用协议？(y/n)')
  if c=='y':
    with open('eula.txt','w+') as f:
      f.write('eula=true')
      f.close()
    print('已更改eula.txt!')
  os.system('pause')
  print('移动各项到server文件夹......')
  os.system('pause')
  os.system('move eula.txt server')
  time.sleep(2)
  os.system('move logs server')
  time.sleep(1)
  os.system('move libraries server')
  time.sleep(3)
  os.system('move versions server')
  os.system('move server.properties server')
  print('启动server目录下的start.bat文件即可运行服务器！将server.properties的onlinemode改为false即可，或使用链接的：https://nq5n-my.sharepoint.com/personal/kangshuoxi_nq5n_onmicrosoft_com/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fkangshuoxi%5Fnq5n%5Fonmicrosoft%5Fcom%2FDocuments%2Fserver%2Eproperties')
  os.system('pause')
