class WordsFinder:
    def __init__(self, *files):
        file_names = []
        self.file_names = file_names
        for file_name in files:
            self.file_names.append(file_name)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                p = [',', '.', '=', '!', '?', ';', ':', ' - ']
                words = []
                for line in file:
                    for i in p:
                        line = line.replace(i, '')
                    words += line.lower().split()
                all_words[name] = words
        return all_words

    def find(self, word):
        word = word.casefold()
        find_dict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_dict[name] = words.index(word) + 1
                return find_dict
            else:
                return 'Искомое слово не найдено.'

    def count(self, word):
        word = word.casefold()
        count_dict = {}
        count = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i == word:
                    count += 1
                count_dict[name] = count
        return count_dict



d = WordsFinder('Rudyard Kipling - If.txt')
print(d.file_names)
print(d.get_all_words())
print(d.find('tHe'))
print(d.count('tHE'))