#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import cgi

userform = """<!DOCTYPE html><html>
<head>
<form method="post">
<h1>Signup</h1>
<table>
    <tr>
      <td>
        <label> Username
        </label>
      </td>
      <td>
          <input type = "text" name="username" value = %(username)s>
      </td>
      <td> %(errorUsername)s</td>
    </tr>

    <tr>
      <td>
        <label> Password
        </label>
      </td>
      <td>
        <input type = "password" name="password" value = %(password)s>
      </td>
      <td> %(errorPassword)s</td>
    </tr>

    <tr>
      <td>
        <label> Verify Password
        </label>
      </td>
      <td>
        <input type = "password" name="verify" value = %(verify)s>
      </td>
      <td> %(errorVerify)s</td>
    </tr>

    <tr>
      <td>
        <label> Email (optional)
        </label>
      </td>
      <td>
        <input type = "text" name="email" value =%(email)s>
      </td>
      <td> %(errorEmail)s</td>
    </tr>
</table>

  <input type="submit">
</form>
</head>
</html>
"""

WelcomeUser = """
<!DOCTYPE html><html>
<head>
<title>Welcome</title>
</head>
<body>
<h2>Welcome %(username)s!</h2>
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASSWORD_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

def escape_html(s):
   return cgi.escape(s,quote = True)

class MainHandler(webapp2.RequestHandler):
#main user-sign up page and renders back here if errors
    def writeForm(self,username="",password="",verify="",email="",errorUsername="",errorPassword="",errorVerify="",errorEmail=""):
        self.response.write(userform%{
                                        "username":escape_html(username),
                                        "password":escape_html(password),
                                        "verify":escape_html(verify),
                                        "email":escape_html(email),
                                        "errorUsername":escape_html(errorUsername),
                                        "errorPassword":escape_html(errorPassword),
                                        "errorVerify":escape_html(errorVerify),
                                        "errorEmail":escape_html(errorEmail)})

    def get(self):
        self.writeForm()

    def post(self):
        errorUsername =""
        errorPassword = ""
        errorVerify =  ""
        errorEmail = ""

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        usernameChk = valid_username(username)
        passwordChk = valid_password(password)
        emailChk = valid_email(email)

        if not (usernameChk and passwordChk and emailChk and password == verify):
            if not usernameChk:
                errorUsername = "Try again, invalid username"
            if not passwordChk:
                errorPassword = "You need a better password that\'s too easy to hack"
            if not emailChk:
                errorEmail = "That\'s not a real email, you can\'t trick me!"
            if not password == verify:
                errorVerify = "Your passwords don\'t match...come on, you just typed it 2 seconds ago..."
            self.writeForm(username,"","",email,errorUsername,errorPassword,errorVerify,errorEmail)

        else:
            self.redirect("/welcome")


class WelcomeUserHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.write(WelcomeUser%{'username':username})


app = webapp2.WSGIApplication([
    ('/', MainHandler),('/welcome',WelcomeUserHandler)], debug=True)
