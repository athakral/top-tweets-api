import urllib2, json, base64
import urllib


def login():
    CONSUMER_KEY = "LYEmPkX6eAHlyUaahTYCM15ba" # (API key)
    CONSUMER_SECRET = "MGUEzKDdYavWWMBMArQb5G2bzO6IkRAIC0oqg28wwdAfOnBIE8" #(API secret key)
    # Set the variable to Twitter OAuth 2 endpoint
    oauth_url = 'https://api.twitter.com/oauth2/token'

    # Set the HTTP request headers, including consumer key and secret
    http_headers={'Authorization': "Basic %s" % base64.b64encode("%s:%s" % (CONSUMER_KEY,CONSUMER_SECRET)), 'Content-Type': 'application/x-www-form-urlencoded'} 

    # Set the payload to the required OAuth grant type, in this case client credentials
    request_body=urllib.urlencode({"grant_type":"client_credentials"}) 

    # Send the request
    request = urllib2.Request(url=oauth_url, data=request_body, headers=http_headers)
    response = urllib2.urlopen(request).read()


    # Read the response as JSON
    app_token = json.loads(response)
    return app_token

def search(query,app_token):
    # Use the query for searching the tweets
    url='https://api.twitter.com/1.1/search/tweets.json?%s' % urllib.urlencode({'q':query,'type':'popular'}) 

    # Set the Authorization header using the value of the access_token key from the app_token dictionary created above
    http_headers={'Authorization': 'Bearer %s' % app_token ['access_token']} 

    # Send the request
    request = urllib2.Request(url=url, data=None, headers=http_headers)
    response = urllib2.urlopen(request).read() 
    return response


