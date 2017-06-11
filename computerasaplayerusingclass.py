class ComputerPlayer(Player):
    """
    A computer player class.
    Does everything a Player does, but can also pick a word using the
    PickBestWord method.
    """
    def pickBestWord(self, wordlist):
        """
        Pick the best word available to the computer player.

        returns: The best word (a string), given the computer player's hand and
        the wordlist
        """
        wordlength = sum(self.hand.handDict.values())
        dicc = pointdict()
        word = bestchoice(dicc, self.hand.handict, wordlength)
        return word
        # TODO
    def playHand(self, callback, wordlist):
        """
        Play a hand completely by passing chosen words to the callback
        function.
        """
        while callback(self.pickBestWord(wordlist)): pass
        

def getwordmaxscore(word):
    valid = get_frequency_dict(word)
    temp = 0
    for i in word:
        temp = temp+valid[i]*SCRABBLE_LETTER_VALUES[i]
    return temp

def pointdict():
    dicc = {}
    for i in range(len(word_list)):
        lenword = len(word_list[i])
        word = word_list[i]
        wordmaxscore = getwordmaxscore(word)
        if lenword not in dicc.keys():
            dicc[lenword] = {wordmaxscore: [word]}
        else:
            if wordmaxscore not in dicc[lenword].keys():
                dicc[lenword][wordmaxscore] = [word]
            else:
                dicc[lenword][wordmaxscore].append(word)
    return dicc


def is_validword(word, hand):
    word_freq = get_frequency_dict(word)
    if all(key in hand.keys() and word_freq[key] <= hand[key]
            for key in word_freq) and word in word_list:
        print("it is present in the hand and it is a validword")
        return True
    return False


def bestchoice(dicc, hand, wordlen):
    print "wordlen = ", wordlen
    while wordlen > 1:
        # print ("hi")
        print "len(dicc[wordlen].keys()) = ", len(dicc[wordlen].keys())
        while len(dicc[wordlen].keys()) != 0:
            # print("hello")
            maxscore = max(dicc[wordlen].keys())
            for word in dicc[wordlen][maxscore]:
                # print("is it working")
                if is_validword(word, hand):
                    print(word)
                    return word
                else:
                    dicc[wordlen][maxscore].remove(word)
            del dicc[wordlen][maxscore]
        del dicc[wordlen]
        wordlen -= 1
        print "word length ", wordlen
    defaultword = "."
    print("ok I stop here")
    return defaultword
