import params as p
import unicodedata
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter

class SentenceAnalysis:
    def __init__(self):
        self.t = Tokenizer()

    # def analysis(self, content):
    #     items = []
    #     token_filters = [POSKeepFilter(['名詞'])]
    #     analyzer = Analyzer([], self.t, token_filters)
    #     for  in analyzer.analyze():
    #         for idx in range(len(p.TARGET_POS)):
    #             print(token.part_of_speech.split(',')[0])
    #             if str(token.part_of_speech.split(',')[0]) == "名詞":
    #                 items.append(token.surface)
    #     return items

    def remove_template(self, surface):
        #日本語だったら
        if self.is_japanese(surface):
            if not surface == "バッド" or surface == "グッド" or surface == "ニュース" or surface == "その他":
                return surface
        #英語だったら
        else:
            low_surface = surface.lower()
            if not low_surface == "bad" or low_surface == "good" or low_surface == "others":
                return surface

        return False
    @classmethod
    def is_japanese(self, string):
        for ch in string:
            name = unicodedata.name(ch)
            if "CJK UNIFIED" in name \
            or "HIRAGANA" in name \
            or "KATAKANA" in name:
                return True
            return False