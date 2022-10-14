from joseph.APIs.market_orders import make_orders
from joseph.tests.variables import *
import asyncio
from joseph.APIs.risk_figures import *
class TestMarketOrders:

    # def test_sanity_checks(self):
    #     buy_side=asyncio.run(make_orders([my_buy_order]))
    #     sell_side=asyncio.run(make_orders([my_sell_order]))
    #     print("BUY",buy_side)
    #     print(sell_side)
    #     assert buy_side['total_amount']> sell_side['total_amount']

    def test_wrong_body_params(self):
        for wrong_buy_order in wrong_buy_orders:
            response=asyncio.run(make_orders([wrong_buy_order]))
            index = wrong_buy_orders.index(wrong_buy_order)
            if index == 0: # Wrong Side
                assert response['message'] == 'Invalid Side'
            elif index == 1: # Wrong Channel Name
                assert response['message']=="Invalid Create Order Request"
            elif index==2: # Low requested amount
                assert response['message'].split(":")[0]=="The amount is too low"
            elif index==3: # High requested amount
                assert response['message'].split(".")[2]==" Consider decreasing your order size"
            elif index==4 and response['order_status']=="rejected": # Order price higher than collateral
                assert response['message'] == "Your collateral does not allow for this trade to be executed. Consider increasing your collateral."
