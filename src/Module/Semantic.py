class Semantic:
    def __init__(self):
        self.pos = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
                    'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'nd': 14, 'nh': 15, 'ni': 16,
                    'nl': 17, 'ns': 18, 'nt': 19, 'nz': 20, 'o': 21, 'p': 22, 'q': 23, 'r': 24,
                    'u': 25, 'v': 26, 'wp': 27, 'ws': 28, 'x': 29}
        self.relate = self.reverseList([
            'SBV', 'VOB', 'IOB', 'FOB', 'DBL', 'ATT', 'ADV', 'CMP', 'COO', 'POB', 'LAD', 'RAD', 'IS', 'WP', 'HED'
        ])
        self.sem_relate = self.reverseList([
            'Agt', 'Exp', 'Aft', 'Poss', 'Pat', 'Cont', 'Prod', 'Orig', 'Datv', 'Comp',
            'Belg', 'Clas', 'Accd', 'Reas', 'Int', 'Cons', 'Mann', 'Tool', 'Malt', 'Time',
            'Loc', 'Proc', 'Dir', 'Sco', 'Quan', 'Qp', 'Freq', 'Seq', 'Desc', 'Feat', 'Host',
            'Nmod', 'Tmod', 'eCoo', 'r + main role', 'd + main role', 'eSelt', 'eEqu', 'ePrec',
            'eSucc', 'eProg', 'eAdvt', 'eCau', 'eResu', 'eInf', 'eCond', 'eSupp', 'eConc',
            'eMetd', 'ePurp', 'eAban', 'ePref', 'eSum', 'eRect', 'mConj', 'mAux', 'mPrep',
            'mTone', 'mTime', 'mRang', 'mDegr', 'mFreq', 'mDir', 'mPars', 'mNeg', 'mMod',
            'mPunc', 'mPept', 'mMaj', 'mVain', 'mSepa', 'Root'
        ])

    def reverseList(self, l):
        d = {}
        for i in range(0, len(l)):
            d[i] = l[i]
        return d

