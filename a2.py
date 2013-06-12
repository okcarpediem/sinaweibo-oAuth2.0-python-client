# -*- coding: utf-8 -*-
from weibo import APIClient
APP_KEY = '2419304382' # app key
APP_SECRET = 'c99a3fa26107e27102a0c5d958c9a756' # app secret
CALLBACK_URL = 'http://app.weibo.com' # callback url
code='fe455e841d67a610f1f86200435cbf48'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
print access_token
client.set_access_token(access_token, expires_in)
weibo_content=raw_input('请输入内容')
weibo_contents=weibo_content.decode('gb2312').encode('utf-8')
client.post.statuses__update(status=weibo_contents)
