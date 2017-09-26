from concurrent.futures import ThreadPoolExecutor


def strike(string):
    return f'<strike style="color: red;">{string}</strike>'


def bold(string):
    return f'<strong style="color: red;">{string}</strong>'


def format_transcript(transcript, map_):
    transcript = transcript.lower().replace('  ', ' ').split()
    word_map = dict(zip(map_, transcript))
    strings = [word if i >= 0 else strike(word) for i, word in word_map.items()]
    string = ' '.join(strings).replace('</strike> <strike style="color: red;">', ' ')
    return string


def format_passage(passage, map_):
    passage = passage.lower().replace('  ', ' ').split()
    strings = [word if i in map_ else bold(word) for i, word in enumerate(passage)]
    string = ' '.join(strings).replace('</strong> <strong style="color: red;">', ' ')
    return string


def markup_results(transcript, passage, maps):
    results = []
    with ThreadPoolExecutor() as executor:
        for map_ in maps:
            results += [{'transcript': format_transcript(transcript, map_),
                         'passage': format_passage(passage, map_)}]
    return results


# TODO format blocks of like formatted words instead of individual words
