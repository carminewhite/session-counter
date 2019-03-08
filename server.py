from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super secret'

@app.route('/')
def index():
    if "num_visits" and "incremented_by_x" in session:
        pass
    else:
        session['num_visits'] = 0
        session['incremented_by_x'] = 0
    session['num_visits'] += 1
    print (f"Session has {session['num_visits']} of visits.  {session['incremented_by_x']} increment count")
    return render_template('index.html')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment_counter', methods=['POST'])
def increment_counter():
    session['incremented_by_x'] += 1
    session['num_visits'] += int(request.form['increment'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)