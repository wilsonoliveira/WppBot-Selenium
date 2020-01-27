from flask import Flask, render_template, request, jsonify

class Group:
   def __init__(self, group_name, is_on):
      self.group_name = group_name
      self.is_on = is_on
   

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
   g1 = Group("Group1", True);
   g2 = Group("Group2", False);
   g3 = Group("Group3", True);
   g4 = Group("Group4", True);
   groups = [g1,g2,g3,g4]
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
