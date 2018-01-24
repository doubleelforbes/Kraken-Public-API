import asset
import assetpair
import order

import json
import kapi

#API Instance
kApi = kapi.kAPI()

# Asset and AssetPair Dicts
Assets = {}
AssetPairs = {}


# Simple trick to begin, return the time.  This can be used to detect Offset/Lag
# Between client and server
rTime = kApi.getServerTime()
print(rTime)

#  Grab Asset, copy data to object and store objects in a dict.
rAssets = kApi.getAssets()
for label, rasset in rAssets.items():
    tmpAsset = asset.Asset(rasset["aclass"], rasset["altname"], rasset["decimals"], rasset["display_decimals"])
    Assets[label] = tmpAsset
print("Assets stored in dictionary of classes!")

# Grab Asset Pairs, copy data to object and store in a dict.
rAssetPairs = kApi.getAssetPairs()
for label, rassetpair in rAssetPairs.items():
    if ".d" in label:
        pass # Why is the API passing duplicate / dud markets?!?!
    else:
        tmpAssetPair = assetpair.AssetPair(label, rassetpair["altname"], rassetpair["aclass_base"], rassetpair["base"],
                                           rassetpair["aclass_quote"], rassetpair["quote"], rassetpair["lot"],
                                           rassetpair["pair_decimals"], rassetpair["lot_decimals"], rassetpair["lot_multiplier"],
                                           rassetpair["leverage_buy"], rassetpair["leverage_sell"], rassetpair["fees"],
                                           rassetpair["fee_volume_currency"], rassetpair["margin_call"], rassetpair["margin_stop"])
        try:
            feesmaker = rassetpair["fees_maker"]
            if feesmaker != None:
                tmpAssetPair.setFeesMaker(feesmaker)
        except:
            pass
        AssetPairs[label] = tmpAssetPair
print("AssetPairs stored in dictionary of classes!")
print("Requesting Test market Data ...")
AssetPairs["BCHEUR"].fillTicker()
AssetPairs["BCHEUR"].fillOHLC()
AssetPairs["BCHEUR"].fillOrderBook()
AssetPairs["BCHEUR"].fillRecentTrades()
AssetPairs["BCHEUR"].fillRecentSpread()
print("\rTicker")
print(AssetPairs["BCHEUR"].Ticker)
print("\rOHLC")
print(AssetPairs["BCHEUR"].OHLC)
print("\rAsk Orders")
print(AssetPairs["BCHEUR"].AskOrders)
print("\rBid Orders")
print(AssetPairs["BCHEUR"].BidOrders)
print("\rHistory")
print(AssetPairs["BCHEUR"].RecentTrades)
print("\rRecent Spread")
print(AssetPairs["BCHEUR"].RecentSpread)
