import json
from urllib.parse import quote_plus
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import time

class kAPI:
    def __init__(self):
        self.BaseURL = "https://api.kraken.com"

    def getServerTime(self):
        command = "/0/public/Time"
        return self.makeUrlQuery(command)

    def getAssets(self, asset="all", info="all info", aclass="currency"):
        command = "/0/public/Assets"
        if asset != "all":
            command += "?asset=" + asset
        if info != "all info":
            command += "?info=" + info
        if aclass != "currency":
            command += "?aclass=" + aclass
        return self.makeUrlQuery(command)

    def getAssetPairs(self, pair="all", info="all info"):
        # info values
        #   leverage = leverage info
        #   fees = fees schedule
        #   margin = margin info
        # pair = comma delimited list of asset pairs default = all
        command = "/0/public/AssetPairs"
        if pair != "all":
            command += "?pair=" + pair
        if info != "all info":
            command += "?info=" + info
        return self.makeUrlQuery(command)

    def getTicker(self, pair):
        command = "/0/public/Ticker?pair=" + pair
        return self.makeUrlQuery(command)

    def getOHLC(self, pair, interval=1, since=None):
        command = "/0/public/OHLC?pair=" + pair
        if interval > 1:
            command += "?interval=" + str(interval)
        if since != None:
            command += "?since=" + since
        return self.makeUrlQuery(command)

    def getOrderBook(self, pair, count=None):
        command = "/0/public/Depth?pair=" + pair
        if count != None:
            command += "?count=" + str(count)
        return self.makeUrlQuery(command)

    def getRecentTrades(self, pair, since=None):
        command = "/0/public/Trades?pair=" + pair
        if since != None:
            command += "?since=" + str(since)
        return self.makeUrlQuery(command)

    def getRecentSpread(self, pair, since=None):
        command = "/0/public/Spread?pair=" + pair
        if since != None:
            command += "?since=" + since
        return self.makeUrlQuery(command)

    def makeUrlQuery(self, commandparams):
        uri = self.BaseURL + commandparams
        response = urllib.request.urlopen(uri).read()
        data = response.decode('utf-8')
        jsondata = json.loads(data)
        if len(jsondata.get("error")) == 0:
            return jsondata.get("result")
        else:
            return "API ERROR! : " + str(jsondata.get("error"))

    def makeJsonQuery(self, command, params):
        # Append the command to the URL
        uri = self.BaseURL + command
        # Pack into HTTP request and try to open the URL.
        rapi = Request(uri, data=str(params).encode("UTF-8-SIG"), method="POST")
        try:
            response = urlopen(rapi).read().decode("UTF-8-SIG")
        except HTTPError as e:
            return "HTTP ERROR! : " + e.reason
        # If we got a response it's a json object
        jsondata = json.loads(response)
        if len(jsondata.get("error")) == 0:
            return jsondata.get("result")
        else:
            return "API ERROR! : " + str(jsondata.get("error"))
