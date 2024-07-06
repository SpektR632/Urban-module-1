class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        words_in_file = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                words_in_file[f] = [''.join([i for i in word if i.isalpha()]) for word in file.read().split()]
        return words_in_file

    def find(self, word):
        find_word = {}
        for key, value in self.get_all_words().items():
            if word.lower() in [i.lower() for i in value]:
                find_word[key] = [i.lower() for i in value].index(word.lower()) + 1
        return find_word

    def count(self, word):
        count_word = {}
        for key, value in self.get_all_words().items():
            if word.lower() in [i.lower() for i in value]:
                count_word[key] = len(list(filter(lambda x: x.lower() == word.lower(), value)))
        return count_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего