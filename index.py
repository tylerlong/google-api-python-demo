from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/androidpublisher']

credentials = ServiceAccountCredentials.from_json_keyfile_name('./key.json', scopes=scopes)

from httplib2 import Http

http = Http()

http_auth = credentials.authorize(http)

resp, content = http.request('https://www.googleapis.com/androidpublisher/v2/applications/com.glip.mobile/reviews', method='GET')
print resp
print content

print '================'

resp, content = http.request('https://www.googleapis.com/androidpublisher/v2/applications/com.ringcentral.android/reviews', method='GET')
print resp
print content

print '================'

resp, content = http.request('https://www.googleapis.com/androidpublisher/v2/applications/com.ringcentral.meetings/reviews', method='GET')
print resp
print content
