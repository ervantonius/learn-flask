import os
from flask import (
	Flask,
	render_template,
	request,
	make_response,
	session,
	url_for,
	redirect,
	flash,
	abort,
)

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret_key_session'

@app.route('/')
def index():
	# return 'Halo'
	search = request.args.get('search')
	return render_template('index.html', search = search)
	
	# if not search:
	# 	return render_template('index.html')

	# return 'hasil search adalah ' + search

@app.route('/setting')
def show_setting():
	return 'Halo di setting'

@app.route('/profile/<username>')
def show_profile(username):
	# return 'Halo ' + username
	# return 'Halo %s' % username
	return render_template('profile.html', name=username)

@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
	# return 'Halo angka %d' % blog_id
	return 'Halo angka %d' % blog_id


@app.route('/login', methods=['GET', 'POST'])
def show_login():
	if request.method == 'POST':
		if request.form['password'] == '':
			abort(401)

		# return 'Email : ' + request.form['email']
		resp = make_response('Email : ' + request.form['email'])
		resp.set_cookie('email_user', request.form['email'])
		session['username'] = request.form['email']
		flash('Berhasil login!', 'info')
		# return resp
		return redirect(url_for('show_profile', username = request.form['email']))

	if 'username' in session:
		username = session['username']
		return redirect(url_for('show_profile', username = username))

	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('show_login'))

@app.route('/getcookie')
def getcookie():
	email = request.cookies.get('email_user')
	return 'Email yang tersimpan di cookie adalah : ' + email

ALLOWED_EXTENSION = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = 'uploads'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile():
	if request.method == 'POST':
		file = request.files['file']
		if 'file' not in request.files:
			return redirect(request.url)
		
		if file.filename == '':
			return redirect(request.url)

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return 'file berhasil di save di ' + filename

	return render_template('upload.html')

@app.errorhandler(401)
def page_unauthorized(e):
	return render_template('401.html'), 401