from flask import Flask, request, render_template, redirect

app = Flask(__name__)

past_accounts = ['3dollarchickensoup', 'oysterher']

@app.route('/', methods=['GET','POST'])
def main():
	latest_account = past_accounts[-1]
	if request.method == "POST":
		username = request.form.get("username")
		if (username.isspace()) | (username ==''):
			feedback = 'Username cannot be blank or space'
			return render_template('main_page.html', latest_account = latest_account, feedback = feedback)
		past_accounts.append(username)
		return redirect('/tao_usernames')
	return render_template('main_page.html', latest_account = latest_account)

@app.route('/tao_usernames', methods=['GET','POST'])
def list_of_users():
	return render_template('list_of_users.html', past_accounts=past_accounts)

@app.route('/latest_user', methods=['GET','POST'])
def latest_user():
	if request.method == "POST":
		option = request.form['options']
		past_accounts.append(past_accounts.pop(past_accounts.index(option)))
		return redirect('/')
	return render_template('latest_user.html', past_accounts=past_accounts)

@app.route('/delete_user', methods=['GET','POST'])
def delete_user():
	if request.method == "POST":
		username = request.form.get("options_delete")
		past_accounts.remove(username)
		return redirect('/tao_usernames')
	return render_template('delete_user.html', past_accounts=past_accounts)
