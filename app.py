from flask import Flask,request, render_template
from stories import *
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
debug = DebugToolbarExtension(app)

@app.route('/')
def main_page():
    story_template = story.template
    story2_template = story2.template
    return render_template('home.html', story_template = story_template, story2_template = story2_template )

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


@app.route('/story2')
def story2_page():
    adverb = request.args.get('adverb')
    noun = request.args.get('noun')
    verb_past_tense = request.args.get('verb_past_tense')
    adjective = request.args.get('adjective')
    
   

    answers_dic = {'adverb':adverb,'noun':noun,'verb_past_tense':verb_past_tense,'adjective':adjective}
     

    complete_story = story2.generate(answers_dic)

    return render_template('story2.html', complete_story = complete_story    )

@app.route('/form')
def form_page():
    template = request.args.get('choice')
    story_prompts = story.prompts
    story2_prompts = story2.prompts
   
    
    return render_template('form.html', template = template, story_prompts = story_prompts,
    story2_prompts = story2_prompts )

