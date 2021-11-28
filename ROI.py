# tpc = 200000
# ri = 2000
# l = 0
# s = 0
# m = 0
# TMI = (tpc+ri+l+s+m)

# tax = .011 * TPC
# ins = .0205 * TPC
# el = 0
# wa = 0
# sw = 0
# gar = 0
# gas = 0
# util = (el+wa+sw+gar+gas)
# hoa = 0
# lc = 0
# vaca = .05 * ri
# rep = 100
# capex = .05 * ri
# pm = .1 * ri
# mort = 860
# TME = (tax+ins+util+hoa+lc+vaca+rep+capex+pm+mort)

# CF = TMI - TME

# ACF = CF * 12
# dp = .2 * tpc
# cc = 3000
# rb = 7000
# mo = 0
# TI = (dp+cc+rb+mo)
# COCROI = ACF // TI

# class ROI:
#     def __init__(self)

class Income:
    def __init__(self, ri, l=0, s=0, m=0):
        self.ri = ri
        self.l = l
        self.s = s
        self.m = m
    def TMI(self):
        tmi = self.ri + self.l + self.s + self.m
        return tmi

class Expenses:
    def __init__(self, tpc, ri=2000, util=0, hoa=0, lc=0, rep=0, mort=0):
        self.tpc= tpc
        self.ri = ri
        self.tax = self.gettax()
        self.ins = self.getins()
        self.util = util
        self.hoa = hoa
        self.lc = lc
        self.vaca = self.getvaca()
        self.capex = self.getcapex()
        self.pm = self.getpm()
        self.rep = rep
        self.mort = mort
    def gettax(self):
        tax = self.tpc *.011
        return tax
    def getins(self):
        ins = self.tpc *.0205
        return ins
    def getvaca(self):
        vaca = self.ri *.05
        return vaca
    def getcapex(self):
        capex = self.ri *.05
        return capex
    def getpm(self):
        pm = self.ri *.1
        return pm
    def TME(self):
        tme = self.tax + self.ins + self.util + self.hoa + self.lc + self.vaca + self.rep + self.capex + self.pm + self.mort
        return tme

class Cashflow:
    def __init__(self, TMI, TME):
        self.TMI = TMI
        self.TME = TME
    def CF(self):
        CF = self.TMI - self.TME
        return CF

class Croi:
    def __init__(self, ACF, TI):
        self.ACF = ACF
        self.TI = TI
    def COCRIO(self):
        COCRIO = self.ACF / self.TI
        return COCRIO
    def ACF(CF):
        ACF = CF * 12
        return ACF
    def TI(tpc, cc, rb, mo):
        dp = .2 * tpc
        TI = dp + cc + rb + mo
        return TI

duplex = {
	'income': Income(2000),
	'expense': Expenses(200000)
}

cash = Croi(duplex['income'].TMI(), duplex['expense'].TME())
print(cash.COCRIO())
