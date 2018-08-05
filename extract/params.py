#################
#パラメータ群です
#################



#読み込むファイルのパスとファイル名です
CONTENTS_PATH = '../src_for_py/'
CONTENTS_FILE = 'sample_diary.txt'

#取得する品詞群です。
TARGET_POS = [
    '名詞',
    '動詞',
    '形容詞'
              ]

#順位何番目まで取得するか決めます。
TARGET_COUNT = 3

#吐き出すjsonのパスとファイル名です
JSON_PATH = '../src_for_py/'
JSON_FILE = 'hot_words.json'

#jsonの日本語エスケープ有無です（Falseで日本語化）
JP_ESCAPE = False