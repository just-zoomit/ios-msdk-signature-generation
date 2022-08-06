import jwt
import time
import datetime
import os


iat = float(int(time.time()))
exp = float((datetime.datetime.today() + datetime.timedelta(days=2)).strftime("%s"))
tokenExp = float((datetime.datetime.today() + datetime.timedelta(hours=10)).strftime("%s"))


'''
In terminal, test if env variable is set:

echo $ZOOM_SDK_KEY
echo $ZOOM_SDK_SECRET

'''
key= os.environ['ZOOM_SDK_KEY']
secret= os.environ['ZOOM_SDK_SECRET']

print("key", key)
print("secret", secret)

payload = {
   'appKey': key,
    'iat': iat,
    'exp': exp,
    'tokenExp': tokenExp
  }

encoded = jwt.encode(payload, secret, algorithm='HS256')
print(encoded)