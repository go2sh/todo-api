import os
import sys
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

import api.v1.endpoints.todos

from api.v1 import api
app.register_blueprint(api)
