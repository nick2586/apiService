from flask import Flask
app = Flask(__name__)

import apiService.hello
import apiService.healthAPI