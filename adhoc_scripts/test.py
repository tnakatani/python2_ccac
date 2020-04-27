import re


def extract_jp_chars(text):
    """Extract all Japanese characters from a text
    """
    all_kanji = '一-熙'
    all_hiragana = 'ぁ-ん'
    all_katakana = 'ァ-ヶ'
    jp_special_chars = '、-〿'  #'ー！：／'
    regex_pattern = '[' + \
        all_kanji + \
        all_hiragana + \
        all_katakana + \
        jp_special_chars + \
        ']'
    # clean = re.compile(regex_pattern)
    # split = re.split(regex_pattern, utterance)
    jp = '([一-熙ぁ-んァ-ヶー！：／])'  #|([a-zA-Z])'
    utt = text.replace(' ', '')
    sub = re.sub(jp, r' \1', utt)
    # findall = re.findall(regex_pattern, utterance)
    # print(split)
    # print(findall)
    print(sub)


if __name__ == '__main__':
    test = ['all 漢字 は not クリエイテッド equal でしょう ！!', '皆さん、こんにちは、Python、パイソン']
    for text in test:
        extract_jp_chars(text)
