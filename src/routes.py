from flask import (
    render_template,
    request,
    redirect,
    flash
)

from app import app

@app.route("/ping")
def ping():
    return "Pong"
