# -*- coding: utf-8 -*-
"""
本程序可以通过B站视频链接下载视频的音频

@author: Cooper
"""

import requests
import re
import json

url = input('输入该视频的有效链接地址：')
title = input('please input the title:')
head = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
              'Referer':url } # 这两个参数缺一不可
resp = requests.get(url, headers=head)
json_data = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)[0]
json_data = json.loads(json_data)
audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
audio_data = requests.get(audio_url,headers=head)
with open(title+'.mp3', mode='wb') as f:
    f.write(audio_data.content)
print('>>>音频下载完成\n') 
