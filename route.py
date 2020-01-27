from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return u"""
    <html>
       <head><title>tableau</title></head>
       <body>
          <h1><a href="/panel" target="_blank">Customer Analysis</a></h1>
       </body>
    </html>
    """
#https://hom.tableau.verde.rj.def.br/views/Superstore/Customers?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link
@app.route("/panel")
def getPanel():
    r = requests.post('https://hom.tableau.verde.rj.def.br/trusted', data={"username": "tableau"}, verify=False)
    # print(r.status_code, r.reason)r.text
    return u"""
    <html>
       <head><title>tableau</title></head>
       <body>
              <iframe src="https://hom.tableau.verde.rj.def.br/trusted/%s/views/Superstore/Customers?iframeSizedToWindow=true&:embed=y&:showAppBanner=false&:display_count=no&:showVizHome=no&:origin=viz_share_link" frameborder="0" marginheight="0" marginwidth="0" style="width: 100%%;height: 100%%;"></iframe>
       </body>
    </html>
    """% r.text

app.run()
