from app.dashboards import dashboards_bp
from flask import Blueprint, render_template


@dashboards_bp.route('/')
def index():
    return render_template('dashboards.html', title='Dashboard')


@dashboards_bp.route('/setup')
def setup():
    return render_template('setup.html', title='Dashboard')


@dashboards_bp.route('/setup/school-identity')
def school_identity():
    return render_template('school_identity.html', title='Dashboard')
