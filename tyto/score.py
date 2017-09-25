# Example transcript and passage
# transcript = 'jumped over the lazy'
# passage = ('the quick brown FOX jumped over the lazy dog '
#            'then the quick brown DOG jumped over the lazy fox')


def map_and_score(transcript, passage):
    """ Given two strings, transcript and passage, split them into a list and
    interate over the passage while inspecting a slice of increasing size.
    Determine the score using best fit and record the mappings for testing. """
    maps = []
    fit_max, hit_count_max = 0, 0
    transcript = transcript.lower().replace('  ', ' ').split()
    passage = passage.lower().replace('  ', ' ').split()
    passage_length = len(passage)
    if not passage:
        return -1, []  # TODO raise BookPassageValueError
    # if not list(set(transcript) & set(passage)):  # Stop searching when there's no common words
    #     return 0, [list(range(-1, -1 * passage_length - 1, -1))]
    if transcript == passage:
        return 1, [list(range(passage_length))]
    for i in range(passage_length):
        step = 0
        # commance inspecting chunks while chunks are the appropriate size
        while i + step < passage_length and hit_count_max < passage_length - i:
            step += 1
            if step >= hit_count_max:  # ensure we're only inpecting chunks >= max observed
                chunk = passage[i:i + step]
                hits, map_ = [], []
                insert_index = 0
                for word in transcript:
                    if word in chunk[len(hits):]:  # re-slice to fix issue repeated words
                        index = chunk[len(hits):].index(word) + i + len(hits)
                        if not hits or index > max(hits):  # ensures expected word order
                            hits.append(index)
                            map_.append(index)
                    else:
                        insert_index -= 1
                        map_.append(insert_index)  # placeholder for unexpected insertions
                hit_count = len(hits)
                fit = hit_count * (hit_count/len(chunk))  # best fit ratio times number of matches
                if fit == fit_max:  # sometimes we'll find mappings with identical fit
                    maps.append(map_)
                if fit > fit_max:  # keep track of the best observation
                    fit_max = fit
                    hit_count_max = hit_count
                    maps = [map_]
                if len(hits) == len(transcript):  # max score reached, skip to the next sliding chunk
                    break
            # Stop searching when there's no common words
            if i == 0 and maps and max(maps[0]) < 0 and len(maps[0]) == passage_length:
                return 0, maps
    score = hit_count_max/passage_length
    return score, maps
