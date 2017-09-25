from tyto.score import map_and_score
from tyto.format import markup_results
from flask import Flask, render_template, request, session
import uuid


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        transcript, passage = request.form['transcript'], request.form['passage']
        if transcript and passage:
            score, maps = map_and_score(transcript, passage)
            score = str(score)[:6]
            session['transcript'], session['passage'] = transcript, passage
            print(transcript, passage, score)
            results = markup_results(transcript, passage, maps)
            return render_template('grade.html', results=results, score=score)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)  # for testing
