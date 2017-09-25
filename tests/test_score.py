from tyto.score import map_and_score
import yaml


# Positive transcript map indexes correspond with the passage index
# Negative trancript map indexes track extra insertions in the transcript

# TODO add tests for expected markup result data


def test_map_and_score_with_flip_flopping():
    transcript = 'the quick bird the quick ballon'
    passage =    'the quick cat the quick chat'
    expected_score = 4/6
    expected_maps = [[0, 1, -1, 3, 4, -2]]
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_repeated_words():
    transcript = 'hello bob hello galvin'
    passage =    'hello tom hello sue'
    expected_score = 2/4
    expected_maps = [[0, -1, 2, -2]]
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_flip_flopping_and_repeated_words():
    transcript = 'hello bob hello sue'
    passage =    'hello sue hello bob'
    expected_score = 2/4
    expected_maps = [[0, -1, -2, 1]]  # TODO look into argument for [[0, -1, 2, -2]]
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_flip_flopping_and_repeated_words():
    transcript = 'By default capturing is DONE by intercepting writes to low level file descriptors'
    passage =    'By default capturing is by intercepting writes DONE to low level file descriptors'
    expected_score = 10/13  # BUG: Working as designed but seems like it should be 12/13
                            # Note: this is the down-side of successive/order based matching
    expected_maps = [[0, 1, 2, 3, 7, -1, 8, 9, 10, 11, 12]]  # TODO research other best-fit/distance algos
                                                             # Levenstein distance check might catch this
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


with open('tests/data.yml') as f:
    data = yaml.load(f)

passage = data.pop('passage')


def test_map_and_score_with_incomplete_transcript():
    transcript = data['partial']['words']
    expected_score = data['partial']['score']
    expected_maps = data['partial']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_one_extra_word():
    transcript = data['insert']['words']
    expected_score = data['insert']['score']
    expected_maps = data['insert']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_one_word_ommitted():
    transcript = data['omit']['words']
    expected_score = data['omit']['score']
    expected_maps = data['omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_one_extra_word_and_one_missing_word():
    transcript = data['insert_omit']['words']
    expected_score = data['insert_omit']['score']
    expected_maps = data['insert_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_multiple_extra_words():
    transcript = data['multi_insert']['words']
    expected_score = data['multi_insert']['score']
    expected_maps = data['multi_insert']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_multiple_words_omitted():
    transcript = data['multi_omit']['words']
    expected_score = data['multi_omit']['score']
    expected_maps = data['multi_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_multiple_words_inserted_and_omitted():
    transcript = data['multi_insert_omit']['words']
    expected_score = data['multi_insert_omit']['score']
    expected_maps = data['multi_insert_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_all_the_same_words():
    transcript = data['all_same']['words']
    expected_score = data['all_same']['score']
    expected_maps = data['all_same']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_all_different_words():
    transcript = data['all_different']['words']
    expected_score = data['all_different']['score']
    expected_maps = data['all_different']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_offset_start():
    transcript = data['offset']['words']
    expected_score = data['offset']['score']
    expected_maps = data['offset']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_offset_start_and_an_inserted_word():
    transcript = data['offset_insert']['words']
    expected_score = data['offset_insert']['score']
    expected_maps = data['offset_insert']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_offset_start_and_an_omitted_word():
    transcript = data['offset_omit']['words']
    expected_score = data['offset_omit']['score']
    expected_maps = data['offset_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_offset_start_and_one_extra_word_and_one_missing_word():
    transcript = data['offset_insert_omit']['words']
    expected_score = data['offset_insert_omit']['score']
    expected_maps = data['offset_insert_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_offset_start_with_multiple_words_inserted_or_omitted():
    transcript = data['offset_multi_insert_omit']['words']
    expected_score = data['offset_multi_insert_omit']['score']
    expected_maps = data['offset_multi_insert_omit']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score


def test_map_and_score_with_repeated_phrase():
    transcript = data['repeated_phrase']['words']
    expected_score = data['repeated_phrase']['score']
    expected_maps = data['repeated_phrase']['maps']
    expected_score = eval(expected_score)
    actual_score, actual_maps = map_and_score(transcript, passage)
    assert actual_maps == expected_maps
    assert actual_score == expected_score
