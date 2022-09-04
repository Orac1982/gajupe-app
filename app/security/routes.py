from flask import Blueprint, render_template, request
# from app.models import user_datastore, db

security_bp = Blueprint(
    'security_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@security_bp.route("/login")
def login():
    pass


@security_bp.route("/callback")
def callback():
    pass


@security_bp.route("/logout")
def logout():
    pass


@security_bp.route("/")
def index():
    pass


@security_bp.route("/protected_area")
def protected_area():
    pass


# @security_bp.route('/register', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         user_datastore.create_user(
#             email=request.form.get('email'),
#             password=request.form.get('password')
#         )
#         db.session.commit()
#     return render_template('register.html')
