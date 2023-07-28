from flask import Flask
import git

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./CB_Sample')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

@app.route("/")
def hello():
    return "Hello there. I am Clever Brain Updated 5."
