import kapi
import ticker
import ohlc
import order
import trade
import spread

class AssetPair:
    def __init__(self, label, altname, aclassbase, base, aclassquote, quote, lot, pairdecimals,
                 lotdecimals, lotmultiplier, leveragebuy, leveragesell, fees, feevolumecurrency,
                 margincall, marginstop):
        self.Label = label
        self.AltName = altname
        self.AClassBase = aclassbase
        self.Base = base
        self.AClassQuote = aclassquote
        self.Quote = quote
        self.Lot = lot
        self.PairDecimals = pairdecimals
        self.LotDecimals = lotdecimals
        self.LotMultiplier = lotmultiplier
        self.LeverageBuy = leveragebuy
        self.LeverageSell = leveragesell
        self.Fees = fees
        self.FeesMaker = ""
        self.FeeVolumeCurrency = feevolumecurrency
        self.MarginCall = margincall
        self.MarginStop = marginstop
        self.AskOrders = []
        self.BidOrders = []
        self.OHLC = []
        self.RecentTrades = []
        self.RecentSpread = []
        self.Ticker = ""

    def setFeesMaker(self, feesmaker):
        self.FeesMaker = feesmaker

    def fillTicker(self):
        kApi = kapi.kAPI()
        tickerdata = kApi.getTicker(self.Label)
        tickerdata = tickerdata[self.Label]
        aprice = tickerdata["a"][0]
        awlvol = tickerdata["a"][1]
        alvol = tickerdata["a"][2]
        bprice = tickerdata["b"][0]
        bwlvol = tickerdata["b"][1]
        blvol = tickerdata["b"][2]
        cprice = tickerdata["c"][0]
        cvolume = tickerdata["c"][1]
        volumet = tickerdata["v"][0]
        volume24 = tickerdata["v"][1]
        vwapt = tickerdata["p"][0]
        vwap24 = tickerdata["p"][1]
        tradest = tickerdata["t"][0]
        trades24 = tickerdata["t"][1]
        lowt = tickerdata["l"][0]
        low24 = tickerdata["l"][1]
        hight = tickerdata["h"][0]
        high24 = tickerdata["h"][1]
        oprice = tickerdata["o"]
        self.Ticker = ticker.Ticker(aprice, awlvol, alvol, bprice, bwlvol, blvol, cprice, cvolume, volumet, volume24,
                                    vwapt, vwap24, tradest, trades24, lowt, low24, hight, high24, oprice)

    def fillOHLC(self):
        kApi = kapi.kAPI()
        ohlcdata = kApi.getOHLC(self.Label)
        ohlcdata = ohlcdata[self.Label]
        tmpohlclist = []
        for ohlclist in ohlcdata:
            mtime = ohlclist[0]
            mopen = ohlclist[1]
            high = ohlclist[2]
            low = ohlclist[3]
            close = ohlclist[4]
            vwap = ohlclist[5]
            volume = ohlclist[6]
            count = ohlclist[7]
            tmpOHLC = ohlc.OHLC(mtime, mopen, high, low, close, vwap, volume, count)
            tmpohlclist.append(tmpOHLC)
        self.OHLC = tmpohlclist

    def fillOrderBook(self):
        kApi = kapi.kAPI()
        # Even though I ask for "LABEL" it still returns a single element dict under "LABEL"
        book = kApi.getOrderBook(self.Label)
        # 2 Element Dict, Lists of Lists.
        asklist = book[self.Label]["asks"]
        bidlist = book[self.Label]["bids"]
        # Temp Order List
        askorders = []
        for ask in asklist:
            # Set up an order object and add to list
            tmpOrder = order.Order(ask[0], ask[1], ask[2])
            askorders.append(tmpOrder)
        # Set the object with the final list
        self.AskOrders = askorders
            
        # Temp Order List
        bidorders = []
        for bid in bidlist:
            # Set up an order object and add to list
            tmpOrder = order.Order(ask[0], ask[1], ask[2])
            bidorders.append(tmpOrder)
        # Set the object with the final list
        self.BidOrders = bidorders

    def fillRecentTrades(self):
        kApi = kapi.kAPI()
        history = kApi.getRecentTrades(self.Label)
        # Same again, the API likes Dicts, even when they're useless.
        histlist = history[self.Label]
        trades = []
        for hist in histlist:
            price = hist[0]
            volume = hist[1]
            ttime = hist[2]
            if hist[3] == "b":
                ttype = "Buy"
            elif hist[3] == "s":
                ttype = "Sell"
            if hist[4] == "l":
                otype = "Limit"
            elif hist[4] == "m":
                otype = "Market"
            misc = hist[5]
            tmpTrade = trade.Trade(price, volume, ttime, ttype, otype, misc)
            trades.append(tmpTrade)
        self.RecentTrades = trades

    def fillRecentSpread(self):
        kApi = kapi.kAPI()
        spreaddata = kApi.getRecentSpread(self.Label)
        spreaddata = spreaddata[self.Label]
        tmpSpreads = []
        for gap in spreaddata:
            gtime = gap[0]
            bid = gap[1]
            ask = gap[2]
            tmpSpread = spread.Spread(gtime, bid, ask)
            tmpSpreads.append(tmpSpread)
        self.RecentSpread = tmpSpreads
