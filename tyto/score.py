# Example transcript and passage
# transcript = 'jumped over the lazy'
# passage = ('the quick brown FOX jumped over the lazy dog '
#            'then the quick brown DOG jumped over the lazy fox')


def listify(string):
    # TODO regex to remove non-alpanumerics, strip
    return string.lower().replace('  ', ' ').split()


def inspect_slice(transcript, passage, i, step):
    """ Inspect a passage slice and generate a mapping of transcript words
    found in the slice as well as a negative index for words not found. """
    hits, map_ = [], []
    reverse_index = 0
    previous_hit_word = ''
    chunk = passage[i:i + step]
    for word in transcript:
        if word == previous_hit_word:
            rechunk = chunk[len(hits) - 1:]
        else:
            rechunk = chunk[len(hits):]
        if word in rechunk:  # Re-sliced chunk used accomadate words already matched
            index = rechunk.index(word) + i + len(hits)
            if not hits or index > max(hits):  # Only match words presented in the right order
                hits.append(index)
                map_.append(index)
                previous_hit_word = word
        else:
            reverse_index -= 1
            map_.append(reverse_index)  # Track extra words in transcript with a negative index
        hit_count = len(hits)
        fit = hit_count * (hit_count/len(chunk))  # Ratio of matches over chunk size, times number of matches
        print(fit)
    return map_, hits, fit


def get_score(transcript, passage):
    """ Given two strings, transcript and passage, split them into lists and
    interate over the passage while inspecting a slice of increasing size.
    Return the score and associated mappings. """
    maps = []
    fit_max, hit_count_max = 0, 0
    transcript, passage = listify(transcript), listify(passage)
    passage_length = len(passage)
    if not passage:
        return -1, []  # TODO raise BookPassageValueError
    if transcript == passage:
        return 1, [list(range(passage_length))]
    for i in range(passage_length):
        step = 0
        # Only inspect chunks while chunks are the appropriate size
        while i + step < passage_length and hit_count_max < passage_length - i:
            step += 1
            if step >= hit_count_max:  # Skip slices smaller than max observed
                map_, hits, fit = inspect_slice(transcript, passage, i, step)
                if fit == fit_max:
                    maps.append(map_)
                if fit > fit_max:
                    fit_max = fit
                    hit_count_max = len(hits)
                    maps = [map_]
                if len(hits) == len(transcript):
                    break
            # Stop searching when there's no common elements
            if i == 0 and max(maps[0]) < 0 and len(maps[0]) == passage_length:
                return 0, maps
    score = hit_count_max/passage_length
    return score, maps
