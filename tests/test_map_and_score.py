from tyto.score import map_and_score
import yaml


with open('tests/data.yml') as f:
    data = yaml.load(f)

passage = data.pop('passage')


def test_map_and_score_partial():
    transcript = data['partial']['words']
    expected_score = data['partial']['score']
    expected_map = data['partial']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_insert():
    transcript = data['insert']['words']
    expected_score = data['insert']['score']
    expected_map = data['insert']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_omit():
    transcript = data['omit']['words']
    expected_score = data['omit']['score']
    expected_map = data['omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_insert_omit():
    transcript = data['insert_omit']['words']
    expected_score = data['insert_omit']['score']
    expected_map = data['insert_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_multi_insert():
    transcript = data['multi_insert']['words']
    expected_score = data['multi_insert']['score']
    expected_map = data['multi_insert']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_multi_omit():
    transcript = data['multi_omit']['words']
    expected_score = data['multi_omit']['score']
    expected_map = data['multi_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_multi_insert_omit():
    transcript = data['multi_insert_omit']['words']
    expected_score = data['multi_insert_omit']['score']
    expected_map = data['multi_insert_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_all_same():
    transcript = data['all_same']['words']
    expected_score = data['all_same']['score']
    expected_map = data['all_same']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_all_different():
    transcript = data['all_different']['words']
    expected_score = data['all_different']['score']
    expected_map = data['all_different']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_offset():
    transcript = data['offset']['words']
    expected_score = data['offset']['score']
    expected_map = data['offset']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_offset_insert():
    transcript = data['offset_insert']['words']
    expected_score = data['offset_insert']['score']
    expected_map = data['offset_insert']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_offset_omit():
    transcript = data['offset_omit']['words']
    expected_score = data['offset_omit']['score']
    expected_map = data['offset_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_offset_insert_omit():
    transcript = data['offset_insert_omit']['words']
    expected_score = data['offset_insert_omit']['score']
    expected_map = data['offset_insert_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score


def test_map_and_score_offset_multi_insert_omit():
    transcript = data['offset_multi_insert_omit']['words']
    expected_score = data['offset_multi_insert_omit']['score']
    expected_map = data['offset_multi_insert_omit']['map']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert str(actual_maps[0])[1:-1] == expected_map
    assert actual_score == expected_score
