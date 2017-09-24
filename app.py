from tyto.score import score
from flask import Flask, render_template, request, session
import uuid


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = session.get('transcript', '')
    passage = session.get('passage', '')
    result = session.get('result', '')
    if request.method == 'POST':
    # if request.form:
        transcript = request.form['transcript']
        passage = request.form['passage']
        result = score(transcript, passage)
        result = str(result)[:6]
        session['transcript'], session['passage'] = transcript, passage
        session['result'] = result
        return render_template('boom.html', transcript=transcript,
                               passage=passage, result=result)
    print(transcript, passage, result)
    return render_template('index.html', transcript=transcript,
                           passage=passage, result=result)


if __name__ == '__main__':
    app.run(debug=True)  # for testing
