from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id ': 1,
  'title': 'Data Analyste',
  'location': 'Vancouver',
  'salary': '$ 10.000'
}, {
  'id ': 2,
  'title': 'Data Scientist',
  'location': 'Montreal',
  'salary': '$ 20.000'
}, {
  'id ': 3,
  'title': 'Frontend Engineer',
  'location': 'Toronto',
  'salary': '$ 15.000'
}, {
  'id ': 4,
  'title': 'Backend Engineer',
  'location': 'Ottawa',
  'salary': '$ 22.000'
}]


@app.route("/")
def hello_word():
  return render_template('Home.html', jobs=JOBS)
  
@app.route("/api/jobs")
def list_jobs() :
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
