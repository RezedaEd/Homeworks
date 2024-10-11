import string
class WordsFinder:
    def __init__(self, *files_names):
        self.files_names = files_names


    def get_all_words(self):
        all_words = {}
        for name in self.files_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words += line.lower().split()
                all_words[name] = words
        return all_words

    def find(self, word):
        word = word.casefold()
        result_dict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result_dict[name] = words.index(word) + 1
            else:
                result_dict[name] = 'Искомое слово не найдено.'
        return result_dict

    def count(self, word):
        word = word.casefold()
        result_dict = {}
        count = 0
        for name, words in self.get_all_words().items():
            result_dict[name] = words.count(word)
        return result_dict



d = WordsFinder('Rudyard Kipling - If.txt', 'Walt Whitman - O Captain! My Captain!.txt')
print(d.files_names)
print(d.get_all_words())
print(d.find('tHat'))
print(d.count('tHE'))