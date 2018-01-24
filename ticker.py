class Ticker:
    def __init__(self, aprice, awlot, alvol, bprice, bwlot, blvol, closedp, closedv, volumet, volume24,
                 vwapt, vwap24, tradest, trades24, lowt, low24, hight, high24, oprice):
        self.AskPrice = aprice
        self.AskWholeLot = awlot
        self.AskLotVol = alvol
        self.BidPrice = bprice
        self.BidWholeLot = bwlot
        self.BidLotVol = blvol
        self.ClosedPrice = closedp
        self.ClosedVolume = closedv
        self.VolumeToday = volumet
        self.Volume24h = volume24
        self.VWAPToday = vwapt
        self.VWAP24h = vwap24
        self.TradesToday = tradest
        self.Trades24h = trades24
        self.LowToday = lowt
        self.Low24h = low24
        self.HighToday = hight
        self.High24h = high24
        self.OpenPrice = oprice
