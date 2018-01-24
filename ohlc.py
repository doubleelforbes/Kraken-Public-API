class OHLC:
    def __init__(self, mtime, mopen, high, low, close, vwap, volume, count):
        self.Time = mtime
        self.Open = mopen
        self.High = high
        self.Low = low
        self.Close = close
        self.VWAP = vwap
        self.Volume = volume
        self.Count = count
