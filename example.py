#!/usr/bin/python
import API1brokerlib

api = API1brokerlib.Connection("your_api_key")
print api.market_get_bars("GOLD", "60")
