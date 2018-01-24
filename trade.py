class Trade:
    def __init__(self, price, volume, time, ttype, otype, misc):
        self.Price = price
        self.Volume = volume
        self.Time = time
        self.Type = ttype
        self.OrderType = otype
        self.Misc = misc
