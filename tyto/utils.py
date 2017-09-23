from score import simple_score
import yaml


def load_data():
    with open('tests/data.yml') as f:
        data = yaml.load(f)
    return data


data = load_data()
passage = data.pop('passage').lower()


if __name__ == '__main__':
    print()
    print(passage)
    print('-' * 60)
    print()

    for k, v in data.items():
        words = v['words'].lower().replace('  ', ' ')
        score = eval(v['score'])
        result = simple_score(words, passage)
        print(k)
        print(words)
        print(score)
        print(result)
        print()

    print()
