#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================================================================
# IMPORTS
# =============================================================================

from flask import Flask, render_template
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap

from . import sim

# =============================================================================
# CONF
# =============================================================================

app = Flask(__name__)
cli_manager = Manager(app)

Bootstrap(app)


# =============================================================================
# ROUTES
# =============================================================================

@app.route("/")
def index():
    return render_template('index.html', name="foo")



