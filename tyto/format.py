# Word by word styling for the results


def strike(string):
    return f'<strike style="color: red;">{string}</strike>'


def bold(string):
    return f'<strong style="color: red;">{string}</strong>'


def format_transcript(transcript, map_):
    print(transcript, map_)
    transcript = transcript.lower().replace('  ', ' ').split()
    word_map = dict(zip(map_, transcript))
    strings = [word if i >= 0 else strike(word) for i, word in word_map.items()]
    print(strings)
    return ' '.join(strings)


def format_passage(passage, map_):
    print(passage, map_)
    passage = passage.lower().replace('  ', ' ').split()
    strings = [word if i in map_ else bold(word) for i, word in enumerate(passage)]
    print(strings)
    return ' '.join(strings)


def markup_results(transcript, passage, maps):
    results = []
    for map_ in maps:
        results.append({'transcript': format_transcript(transcript, map_),
                        'passage': format_passage(passage, map_)})
    return results