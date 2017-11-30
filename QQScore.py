#import

HighScore = 650
MidHScore = 550
MidLScore = 500

LowMHScore = 400
LowMLScore = 350
LowScor = 300

HighDecision = 1.348264008
MidHDecision = 1.103126188
MidLDecision = 0.465767857

LowMHDecision = -0.17189149
LowMLDecision = -0.751731643
LowDecision = -1.116816184
NDecision = -1.288620673

class QQScore:
    def __init__(self):
        self.DEBUG = 1
        
    def score(self, deci):
        scr = 0
        highstep = (HighScore - MidHScore)/(HighDecision - MidHDecision)
        midstep = (MidHScore - MidLScore)/(MidHDecision - MidLDecision)
        lowHstep = (MidLScore - LowMHScore)/(MidLDecision - LowMHDecision)
        lowLstep = (LowMHScore - LowMLScore)/(LowMHDecision - LowMLDecision)
        lowstep = (LowMLScore - LowScor)/(LowMLDecision - LowDecision)
        Nstep = LowScor/(LowDecision - NDecision)

        if ( deci > HighDecision ): #>650
            scr = HighScore
        elif ( deci > MidHDecision ): #550~650
            scr = MidHScore + (deci - MidHDecision )*highstep
        elif ( deci > MidLDecision ):#500~550
            scr = MidLScore + (deci - MidLDecision )*midstep
        elif ( deci > LowMHDecision ):#400~500
            scr = LowMHScore + (deci - LowMHDecision )*lowHstep
        elif ( deci > LowMLDecision ):#350~400
            scr = LowMLScore + (deci - LowMLDecision )*lowLstep
        elif ( deci > LowDecision ):#300~350
            scr = LowScor + (deci - LowDecision )*lowstep
        elif ( deci > NDecision ):#0~300
            scr = (deci - NDecision)*Nstep
        else:
            scr = 0
        
        return scr
        #return deci

