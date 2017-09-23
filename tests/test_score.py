from tyto.score import simple_score
import yaml


with open('tests/data.yaml') as f:
    data = yaml.load(f)

passage = data.pop('passage').lower()


def batch_tests():
    for k, v in data.items():
        transcript = v['words'].lower().replace('  ', ' ')
        expected_score = v['score']  # eval(v['score'])
        expected_score = eval(expected_score)
        score = simple_score(transcript, passage)
        assert score == expected_score


def test_simple_score_perfect():
    transcript, expected_score = data['perfect']['words'], data['perfect']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_insert():
    transcript, expected_score = data['insert']['words'], data['insert']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_omit():
    transcript, expected_score = data['omit']['words'], data['omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_insert_omit():
    transcript, expected_score = data['insert_omit']['words'], data['insert_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_multi_insert():
    transcript, expected_score = data['multi_insert']['words'], data['multi_insert']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_multi_omit():
    transcript, expected_score = data['multi_omit']['words'], data['multi_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_multi_insert_omit():
    transcript, expected_score = data['multi_insert_omit']['words'], data['multi_insert_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_all_same():
    transcript, expected_score = data['all_same']['words'], data['all_same']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_all_different():
    transcript, expected_score = data['all_different']['words'], data['all_different']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_offset():
    transcript, expected_score = data['offset']['words'], data['offset']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_offset_insert():
    transcript, expected_score = data['offset_insert']['words'], data['offset_insert']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_offset_omit():
    transcript, expected_score = data['offset_omit']['words'], data['offset_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_offset_insert_omit():
    transcript, expected_score = data['offset_insert_omit']['words'], data['offset_insert_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score


def test_simple_score_offset_multi_insert_omit():
    transcript, expected_score = data['offset_multi_insert_omit']['words'], data['offset_multi_insert_omit']['score']
    expected_score = eval(expected_score)
    assert simple_score(transcript, passage) == expected_score
