#-*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import os
import re
import sys



class requester:

    def __init__(self, url, cookie_url=None):

        # passman = urllib2.HTTPBasicAuthHandler()
        # passman.add_password(None, "", "protected", "password")
        # # use HTTPDigestAuthHandler instead here

        self.url=url
        self.cookie_url=cookie_url

        self.cookie = cookielib.MozillaCookieJar()
        self.opener = urllib2.build_opener()#urllib2.HTTPCookieProcessor(self.cookie))
        #self.opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        self.opener.addheaders = [("User-agent","gcchek"),('Cookie', ':)')]

        #self.getCookie()

    def getCookie(self):
        if self.cookie_url:
            self.opener.open(self.cookie_url)
        else:
            self.opener.open(self.url)


    def tryData(self,data):

        data_string= urllib.urlencode(data)

        req = self.opener.open(self.url, data_string)
        return req.read()