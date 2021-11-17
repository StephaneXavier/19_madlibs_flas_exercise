from flask import Flask,request, render_template
from stories import *
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
debug = DebugToolbarExtension(app)

@app.route('/')
def main_page():
    story_prompts = story.prompts
    return render_template('home.html', story_prompts = story_prompts )

@app.route('/story')
def story_page():
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    plural_noun = request.args.get('plural_noun')
    answers_dic = {'place':place,'noun':noun,'verb':verb,'adjective':adjective,
    'plural_noun':plural_noun}
     

    complete_story = story.generate(answers_dic)

    return render_template('story.html', complete_story = complete_story    )


