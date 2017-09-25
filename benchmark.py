from timeit import timeit

setup ="""
from tests.test_score import data, passage

def timed_run():
    transcript = data['repeated_phrase']['words']
    score, maps = get_score(transcript, passage)
    results = markup_results(transcript, passage, maps)
    pass
"""


elapsed = timeit('timed_run', setup=setup,number=100000)
print(elapsed)


# 0.0001352769322693348
# 0.0001354909036308527
# 0.0002626110799610615
# 0.00013476982712745667
