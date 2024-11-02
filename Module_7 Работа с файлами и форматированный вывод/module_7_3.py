class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        files_dict = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                file_text = file.read()
                for symb in [',', '.', '=', '!', '?', ';', ':', '-', '\n']:
                    file_text = file_text.replace(symb, ' ')
                files_dict[name] = [word.lower() for word in file_text.split()]
        return files_dict

    def find(self, word):
        find_dict = {}
        for name, list in self.get_all_words().items():
            if word.lower() in list:
                find_dict[name] = list.index(word.lower())
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, list in self.get_all_words().items():
            if word.lower() in list:
                count_dict[name] = list.count(word.lower())
        return count_dict
finder = WordsFinder("test_file.txt")
print(finder.get_all_words())
print(finder.find("Влад"))
print(finder.count("Влад"))