from flask import Flask
from flask_dropzone import Dropzone
from flask_session import Session
import os


app=Flask(__name__)
app.config['SECRET_KEY']='7c7690bf4cc9f9973f23abe21085680aeeb053dd4f919c36d3a47e699b1e'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

dir_path=os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH= os.path.join(dir_path,'static/uploaded_files/'),
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    AUDIO_FILE_UPLOAD=os.path.join(dir_path, 'static/audio_files/')
    
)

app.config['DROPZONE_REDIRECT_VIEW']='decoded'

dropzone=Dropzone(app)

from application import routes

