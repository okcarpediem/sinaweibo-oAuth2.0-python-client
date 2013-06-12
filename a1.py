from weibo import APIClient
APP_KEY = '2419304382' # app key
APP_SECRET = 'c99a3fa26107e27102a0c5d958c9a756' # app secret
CALLBACK_URL = 'http://app.weibo.com' # callback url
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print (url)
