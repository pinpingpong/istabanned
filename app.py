from flask import Flask, request, render_template, redirect

app = Flask(__name__)

past_accounts = ['oysterher','3dollarchickensoup']

@app.route('/', methods=['GET','POST'])
def hello_world():
	latest_account = past_accounts[0]
	if request.method == "POST":
		username = request.form.get("username")
		past_accounts.append(username)
		return tmp()
	return render_template('main_page.html', latest_account = latest_account)


@app.route('/tao_usernames')
def tmp():
	account_title = "List of past usernames"
	return render_template('list_of_users.html', account_title=account_title, past_accounts=past_accounts)


