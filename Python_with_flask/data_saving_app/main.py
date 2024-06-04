from flask import Flask,render_template,request,redirect,url_for
from json_person import read_data,write_data



app = Flask(__name__)


@app.route ('/')

def index():
	persons = read_data()
	return render_template('index.html', persons=persons)

@app.route ('/add_person', methods = ['post'])
def add_person():
	new_person = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'phone': request.form['phone'],
		'email': request.form['email']
	}

	persons = read_data()
	persons.append(new_person)
	write_data(persons)
	return redirect(url_for('index'))

@app.route('/delete_person/<int:person_index>', methods=['POST'])
def delete_person(person_index):
    persons = read_data()
    if 0 <= person_index < len(persons):
        del persons[person_index]
    write_data(persons)
    return redirect(url_for('index'))








if __name__ == '__main__':
	app.run (debug=True)
