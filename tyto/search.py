# Approach: search parsed substrings for possible mappings and compose transcript mappings


def listify(string):
    return string.lower().replace('  ', ' ').split()


def parse_passage(passage):
    """ Find all possible slices of a word list where words appear in the
    expected order. Return a dict of substrings matching substring location to
    possible indexes in the word list. """
    slice_combinations = []
    substring_map = {}
    for n in range(len(passage)):
        for m in range(n, 0, -1):
            offset, split = passage[:m], passage[m:]
            slices = [offset] + [split[i:i + n] for i in range(0, len(split), n)]
            # print(n, len(slices), slices, '\n')
            if slices not in slice_combinations:  # len 2
                slice_combinations.append(slices)
                for j, s in enumerate(slices):
                    string = ' '.join(s)
                    if string in substring_map and j not in substring_map[string]:
                        substring_map[string] += [j]
                    else:
                        substring_map[string] = [j]
    return substring_map


def get_maps(string, substring_map):
    """ in progress """
    maps = []
    # string = ' '.join(transcript)
    for i in range(1, len(transcript)):
        key = ' '.join(transcript[:-i])

        maps = get_maps(key)
        print(i, key, maps)
        if maps:
            break
    if string in substring_map:
        print('substring_map', substring_map[string])
        for i in substring_map[string]:
            map_ = [x + i for x in range(len(transcript))]
            print(map_)
            maps.append(map_)
    return maps


transcript, passage = listify(transcript), listify(passage)
substring_map = parse_passage(passage)
maps = get_maps(string, substring_map)  #
