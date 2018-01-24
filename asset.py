class Asset:
    def __init__(self, aclass, altname, decimals, display_decimals):
        self.AClass = aclass
        self.AltName = altname
        self.Decimals = decimals
        self.DisplayDecimals = display_decimals

    def tostring(self):
        retstr = str(self.AltName) + " Asset Class: " + str(self.AClass) + "Display: "
        retstr += str(self.DisplayDecimals) + " out of " + str(self.Decimals) + " decimal places."
        return retstr
