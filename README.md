# Sample Zoom Meeting SDK IOS Signature Generator

This is a sample python script that generates an encrypted SDK JSON Web Token (JWT) for Zoom Meeting SDK. This helps developers to quickly generate JWT token using the [SDK App Type](https://marketplace.zoom.us/docs/guides/build/sdk-app/) credentials. You can refer to [SDK Authorization](https://marketplace.zoom.us/docs/sdk/native-sdks/auth/) for SDK JWT details.

JWT is generated based on the following core parts as stated in the [documentation](https://marketplace.zoom.us/docs/sdk/native-sdks/auth#generate-the-sdk-jwt). Please create an environment file to store your SDK Key and Secret.

For JWT Token generation, [JWT](https://github.com/jpadilla/pyjwt/) library is used to encode and decode JSON Web Tokens (JWT) in PHP, conforming to RFC 7519. For more JWT libraries and examples, see [JWT.io](https://jwt.io/libraries).


-------
```
/**
 * Below are the fields required for the JWT payload
 * appKey: Your SDK Key. Required for Native, optional for Web.
 * iat: The current timestamp in epoch format. Required.
 * exp: JWT expiration date. Required. Values: Min = 1800 seconds greater than iat value, max = 48 hours greater than iat value. In epoch format.
 * tokenExp: JWT expiration date. Required. Values: Min = 1800 seconds greater than iat value, max = 48 hours greater than iat value. In epoch format.
 * 
 * Source: https://marketplace.zoom.us/docs/sdk/native-sdks/auth/
 */


iat = float(int(time.time()))
exp = float((datetime.datetime.today() + datetime.timedelta(days=2)).strftime("%s"))
tokenExp = float((datetime.datetime.today() + datetime.timedelta(hours=10)).strftime("%s"))

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
}
```