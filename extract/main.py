import params as p
from sentence_analysis import SentenceAnalysis
import json

def read_contents(file):
    data = open(file, "r")
    contents = []
    for row in data:
        contents.append(row.replace('\n',''))
    data.close()
    return contents


def flatten(items):
    return [item for sublist in items for item in sublist]


def make_dict(items):
    dict = {}
    for item in items:
        if not item in dict.keys():
            dict[item] = 1
        else:
            dict[item] += 1

    sorted_dict = {}
    for kwd, count in sorted(dict.items(), key=lambda x: -x[1]):
        sorted_dict[kwd] = int(count)
    shaped_dict = shape_dict_for_json(sorted_dict)
    return shaped_dict


def shape_dict_for_json(sorted_dict):
    word_counts = list(sorted_dict.values())
    maximum = list(set(word_counts))
    maximum.sort(reverse=True)
    limited_max = maximum[:p.TARGET_COUNT]

    json_dict_beta = {}
    for idx ,included in enumerate(limited_max):
        group = []
        if included in word_counts:
            words = [w for w, c in sorted_dict.items() if c == included]
            count = [included] * len(words)
            group.append(dict((zip(words, count))))
        json_dict_beta[idx+1] = group

    json_dict = {}
    for i in range(p.TARGET_COUNT):
        sub_dict = {}
        if len(json_dict_beta[i+1][0]) != 1:
            overlap_word = []
            for idx, (word, count) in enumerate(json_dict_beta[i+1][0].items()):
                sub_dict = {}
                sub_dict["word"] = word
                sub_dict["count"] = count
                overlap_word.append(sub_dict)
                json_dict[i+1] = overlap_word
        else:
            sub_dict["word"] = list(json_dict_beta[i+1][0].keys())[0]
            sub_dict["count"] = list(json_dict_beta[i+1][0].values())[0]
            json_dict[i+1] = sub_dict

    return json_dict

def make_json(dict):
    json_file_path = p.JSON_PATH + p.JSON_FILE
    fw = open(json_file_path, 'w')
    try:
        json.dump(dict, fw, indent=2, ensure_ascii=p.JP_ESCAPE)
        fw.close()
        return True
    except:
        fw.close()
        return False



def main():
    file_path = p.CONTENTS_PATH + p.CONTENTS_FILE
    an = SentenceAnalysis()
    contents = read_contents(file_path)
    items = []
    for content in contents:
        items.append(an.analysis(content))
    flat_items = flatten(items)
    dict = make_dict(flat_items)
    if make_json(dict) == True:
        print('success')
    else:
        print('faild')

if __name__ == '__main__':
    main()