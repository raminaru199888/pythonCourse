from translate import Translator


def translates_sentences(words):
    words = Translator(from_lang='en', to_lang='ru')
    words = words.translate(input())
    return words
words = translates_sentences(0)
print(words)

