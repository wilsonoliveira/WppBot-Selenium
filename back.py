from flask import Flask, render_template, request, jsonify
import service_locator

app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/index/')
def index():
   return render_template('index.html')

@app.route('/groups', methods=['GET'])
def get_groups():
   group_service = service_locator.GroupService()
   print(group_service)
   
   groups = group_service.getAllGroups()
   print(groups)
   return render_template('groups.html', groups = groups)

@app.route('/groups', methods=['POST'])
def post_groups():
   requent_form = request.form;
   print(requent_form)
   return render_template('groups.html', groups = requent_form)

@app.route('/startbot/', methods=['POST'])
def startbot():
   from wppbot import WppApi
   wpp = WppApi(60)
   chats = wpp.get_chat_names()

   data = {'message': chats}

if __name__ == '__main__':
   app.run(debug=True)
