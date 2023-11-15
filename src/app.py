"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

import os
import json
import requests
from flask import Flask

#


app = Flask(__name__)


@app.route('/')
def index():
  return json.dumps({})


@app.route('/release')
def release():
  
  url = "https://api.github.com"
  endpoint = "/repos/pyenv/pyenv/releases"

  res = requests.get(url + endpoint)

  if res.status_code == 200:

      data = res.json()
      releases = [
        {
          'created_at' : release['created_at'],
          'tag_name'   : release['tag_name'],
          'body'       : release['body'],
        }
        for release in data
      ]
      return releases
  else:
      return json.dumps({}), 404


@app.route('/most_3_recent/release')
def most_3_recent__release():
  
  url = "https://api.github.com"
  endpoint = "/repos/pyenv/pyenv/releases"

  params = {
      "per_page": 3,  # Get only the first three releases
      "sort": "created_at",  # Sort by the created_at field
      "direction": "desc"  # Sort in descending order
  }
  res = requests.get(url + endpoint , params=params)

  if res.status_code == 200:

      data = res.json()
      releases = [
        {
          'created_at' : release['created_at'],
          'tag_name'   : release['tag_name'],
          'body'       : release['body'],
        }
        for release in data
      ]
      return releases
  else:
      return json.dumps({}), 404
 
  


if __name__=='__main__':
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
