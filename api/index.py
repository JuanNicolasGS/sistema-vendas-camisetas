from flask import Flask
from app import app

# This is required for Vercel to work with Flask
def handler(environ, start_response):
    return app(environ, start_response)