from Flask import app, request, url_for


@app.route('/handle_data', methods=['POST'])
def handle_data():
    transcript = request.form['transcript']
    passage = request.form['passage']
    #your code
