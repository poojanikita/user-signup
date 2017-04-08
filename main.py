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

userform = """
<form method="post">
<h1>Signup</h1>
<table>
    <tr>
      <td>
        <label> Username
        </label>
      </td>
      <td>
          <input type = "text" name="username" value="username">
      </td>
    </tr>

    <tr>
      <td>
        <label> Password
        </label>
      </td>
      <td>
        <input type = "password" name="password">
      </td>
    </tr>

    <tr>
      <td>
        <label> Verify Password
        </label>
      </td>
      <td>
        <input type = "password" name="verifypw">
      </td>
    </tr>

    <tr>
      <td>
        <label> Email (optional)
        </label>
      </td>
      <td>
        <input type = "text" name="email">
      </td>
    </tr>
</table>

  <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def user_form(self, username ="", password="",verifypw="",email=""):
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
