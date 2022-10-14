from joseph.APIs.ticker_subscription import get_prices
import asyncio
import json
class TestTicker:
    # def check_quantity_prices(self,side):
    #     for i in range(len(side)):
    #         for j in range(i+1,len(side)):
    #             assert

    def test_sanity_check(self):
        response=asyncio.run(get_prices("BTCEUR"))
        for i in response['levels']['buy']:
            assert i['price']!=0
        for i in response['levels']['sell']:
            assert i['price'] != 0
        for i in range(len(response['levels']['buy'])):
            assert response['levels']['buy'][i]['price']>response['levels']['sell'][i]['price']
