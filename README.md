[![Python Versions](https://img.shields.io/badge/Python-3.6-blue.svg)](https://travis-ci.org/brennv/tyto)
[![Build Status](https://travis-ci.org/brennv/tyto.svg?branch=master)](https://travis-ci.org/brennv/tyto)
[![codecov](https://codecov.io/gh/brennv/tyto/branch/master/graph/badge.svg)](https://codecov.io/gh/brennv/tyto)

# tyto

🦉 Text comparison analytics and scoring

Score and map actual text versus expected text.

Demo: [https://tyto.vonapp.co](https://tyto.vonapp.co)


## Usage

Use it to compare actual text versus expected:

```python
from tyto.score import get_score

actual_text = 'hello word'
expected_text = 'hello world'

score, maps = get_score(actual_text, expected_text)

score  # 0.5
maps  # [[0, -1]]
```

The `score` indicates the ratio of words appearing in the correct order that are
found in expected text over the expected text word count.

The `maps` is all possible index mappings of the actual words to expected words.
Actual words that are not found in expected words are a negative number.


## Demo app

Install requirements and start the server:

```
pip install -r requirements.txt
python app.py
```


## Development

Install package and dev requirements:

```
pip install -r requirements.txt
pip install pytest pytest-cov pylama
```

Run and benchmark tests:

```
pytest -v --duration=10 tests/
```
