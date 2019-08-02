import pickle

class Translator:
    def __init__(
        self, 
        embedding_location, 
        dictionary_location, 
        translated_embedding_location
        ):
        self.embedding = []
        print('loading embedding')
        with open(embedding_location, encoding='utf-8') as file:
            for line in file:
                line = line.rstrip()
                line = line.split(' ')
                self.embedding.append(line)
        print('loading dictionary')
        with open(dictionary_location,'rb') as infile:
            self.dictionary = pickle.load(infile)
        self.translated_embedding_location = translated_embedding_location
    def translate(self):
        print('translating embedding')
        for i,vec in enumerate(self.embedding):
            if (len(vec) == 301) & (vec[0] != '</s>'):
                try:
                    token_id = int(vec[0])
                    token_word = self.dictionary[token_id]
                    self.embedding[i][0] = token_word
                    print(str(token_id) + ' ' + token_word)
                except:
                    print('### error in id: ' + str(token_id))
                    pass
        print('saving embedding')
        with open(self.translated_embedding_location, 'w', encoding='utf-8') as file:
            for vec in self.embedding:
                line = " ".join(vec)
                file.write(line)
                file.write('\n')
        
