from flask import Flask, render_template, url_for, request, redirect, session, abort
from website import create_app



app = create_app()
application = app


if __name__ ==  "__main__":
    app.run(debug=True, port=80)

