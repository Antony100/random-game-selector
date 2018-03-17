import json
import os
import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html', consoles=get_consoles())


@app.route('/<console>', methods=['POST'])
def select_game_endpoint(console):
    return select_game(console)


def select_game(console):
    with open(f'consoles/{console}.json') as data_file:
        game_list = json.load(data_file)
    return random.choice(game_list)


def get_consoles():
    console_files = os.listdir('consoles')
    consoles = []
    for console in console_files:
        console_endpoint = console.replace('.json', '')
        name = console_endpoint.replace('_', ' ').title()
        console_dict = dict(console_endpoint=console_endpoint, name=name)
        consoles.append(console_dict)
    app.logger.info(console_dict)
    return consoles
