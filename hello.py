import os
from flask import Flask, request, redirect, session
import json
from grooveshark import Client
from grooveshark.classes.song import Song

app = Flask(__name__)
app.config['DEBUG'] = True

gsClient = Client()
gsClient.init()
gsClient.init_token()
gsClient.init_queue()

@app.route('/')
def hello():
    return 'Hello World!'

'''
Only to be called from localhost verison of the app. NOTHING ELSE.
Downloads the song in ~/Music directory with name songId-phoneumber.mp3
'''
@app.route('/downloadSong', methods=['POST'])
def downloadSong():
    song = Song.from_export(json.loads(request.form['song']), gsClient.connection)
    song.download(song_name = song.id + "-" + request.form['phoneNumber'])
    return song.id
