from flask import Flask
# from dotenv import load_dotenv 
import os 

#from app.config import Config  # if you're using a config class

#load_dotenv()  # Load environment variables from .env file

app = Flask(__name__, static_folder='static', static_url_path='/static') 

#app.config.from_object(Config) # Load configuration from Config class or .env file

from app import routes  # Import routes to register them with the app
