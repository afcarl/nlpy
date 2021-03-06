class Ngram:
    def __init__(self, sentence):
        self.sentence = sentence.split(' ')
        self.unigram = self.uni_gram()
        self.bigram = self.bi_gram()
        self.trigram = self.tri_gram()

    def ngrams(self,n):
        n_gram = []
        for ind,word in enumerate(self.sentence):
            n_gram.append(self.sentence[ind:ind+n])
        return n_gram

    def uni_gram(self):
        return self.ngrams(1)
    
    def bi_gram(self):
        return self.ngrams(2)

    def tri_gram(self):
        return self.ngrams(3)

    #assumes other is also an Ngram object
    def comparison(self,other):
        unigram_count = len([gram for gram in self.unigram if gram in other.unigram])
        bigram_count = len([gram for gram in self.bigram if gram in other.bigram])
        trigram_count = len([gram for gram in self.trigram if gram in other.trigram])

        word_choice_sim = float(unigram_count) / len(self.unigram) 
        word_choice_sim *= 100 
        ave_choice_sim = ((float(bigram_count) / len(self.bigram)) + (float(trigram_count) / len(self.trigram))) / 2
        ave_choice_sim *= 100
        report = ["This writing sample is about %s%% the same in terms of word choice" % (str(word_choice_sim)),
                  "This writing sample uses about %s%% of the same phrasing as the provided second sample" % (str(ave_choice_sim))
                  ]
        return report
