

def simple_score(transcript, passage):
    if is_perfect(transcript, passage):
        result = 1
    else:
        # create map of transcript words found in passage
        # index transcript against passage based on map density
        # normalize lists
        # score lists
        result = 0
    return result


def is_perfect(transcript, passage):
    if transcript in passage:
        return True
    else:
        return False
