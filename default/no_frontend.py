
import logging

from flask import Flask, request
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def ignore(path):
    """Ignores all frontend web requests"""
    logging.info('Default app ignoring:' + path)
    return "OK"