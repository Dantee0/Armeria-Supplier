from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_migrate import Migrate

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))


db = SQLAlchemy() #libreria que usa postgres
migrate = Migrate()

USER_DB = os.environ.get('USER_DB') 
PASS_DB = os.environ.get('PASS_DB')
URL_DB = os.environ.get('URL_DB')
NAME_DB = os.environ.get('NAME_DB')
PORT_DB = os.environ.get('PORT_DB')

#FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'

FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}:{PORT_DB}/{NAME_DB}'