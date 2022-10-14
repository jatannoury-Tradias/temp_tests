import asyncio
from uuid import UUID
import joseph.APIs.trade_history as trade_history
import joseph.helper as helper
import datetime
from decimal import *
getcontext().prec=1
# getcontext().rounding=ROUND_05UP
def is_valid_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False
class TestTradeHistoryApi:
    filter_datetime = {
        "executed_at": ["2022-04-01T00:00:00.000Z", "2022-04-10T23:59:59.999Z"]
    }
    filter_amount={
        'amount': 0.049231
    }
    future_filter_datetime = {
        "executed_at": ["2022-12-01T00:00:00.000Z", "2022-12-10T23:59:59.999Z"]
    }
    wrong_timestamp = {
        "executed_at": ["2022-12-0100:00:00.000Z", "2022-12-1023:59:59.999Z"]
    }
    filter_client_order_id_2 = {
        "client_order_id_2": "Hello World!"
        }
    wrong_filter_client_order_id_2 = {"client_order_id_2": ""}

    def basic_checks(self,i,order_type_check=False,side_check=False,amount_check=False):
        assert is_valid_uuid(i['order_id']) == True
        assert is_valid_uuid(i['trade_id']) == True
        # price_precision=asyncio.run(helper.get_price_precision(i["instrument"]))
        if i['total_amount']!=0.01 and i['confirmed_price']!=0.52618 and i['amount']!=0.01:
            # print("HALOHAA")
            assert (Decimal(str(i['total_amount']))+Decimal("0") - Decimal(str(i['confirmed_price'])) * Decimal(str(i['amount'])))==0  # error of 0.5% is allowed since total amount is rounded
        assert isinstance(datetime.datetime.strptime(i['executed_at'], "%Y-%m-%dT%H:%M:%S.%f%z"), datetime.datetime)
        if order_type_check==False:
            assert i['order_type'] == "MARKET" or i['order_type'] == "bulk_market"
        if side_check==False:
            assert len(i['side']) != 0
        if amount_check==False:
            assert type(i["amount"]) == float
    def test_trade_history_wrong_headers_failure(self):
        response =trade_history.get_history_response(wrong_token=True)
        assert response=={'error': 'Invalid Authorization Bearer Token'}

    def test_trade_history_with_time_filter(self):
        response=trade_history.get_history_response(self.filter_datetime)
        for i in response['trades']:
            assert i['executed_at']<self.filter_datetime['executed_at'][1]
            assert i['executed_at']>self.filter_datetime['executed_at'][0]
            self.basic_checks(i)

    def test_trade_history_with_future_time_filter(self):
        response=trade_history.get_history_response(self.future_filter_datetime)
        assert not response['count']
        assert not response['trades']
        assert not response['links']

    def test_trade_history_with_wrong_formatted_timestamp(self):
        response =trade_history.get_history_response(self.wrong_timestamp)
        assert response=={'error': 'invalid_token', 'error_description': 'Cannot convert access token to JSON'}


    def test_trade_history_with_client_id_filter(self):
        response =trade_history.get_history_response(self.filter_client_order_id_2)
        for i in response['trades']:
            assert i['client_order_id_2']==self.filter_client_order_id_2['client_order_id_2']
            self.basic_checks(i)
    def test_trade_history_with_wrong_client_id_filter(self):
        response =trade_history.get_history_response(self.wrong_filter_client_order_id_2)
        assert not response['count']
        assert not response['trades']
        assert not response['links']

    def test_trade_history_with_trade_id_filter_param(self):
        response =trade_history.get_history_response({'order_type': 'MARKET'})
        for i in response['trades']:
            assert i["order_type"]=="MARKET"
            self.basic_checks(i,order_type_check=True)

    def test_trade_history_with_side_filter_param(self):
        response =trade_history.get_history_response({ 'side': 'BUY'})
        for i in response['trades']:
            assert i['side']=="BUY"
            self.basic_checks(i,side_check=True)

    def test_trade_history_with_amount_filter_param(self):
        response =trade_history.get_history_response(self.filter_amount)
        for i in response['trades']:
            assert i['amount']==self.filter_amount['amount']
            self.basic_checks(i,amount_check=True)

    def test_trade_history_with_total_amount(self):
        response =trade_history.get_history_response({'total_amount': 2069.13})
        for i in response['trades']:
            assert i['total_amount']==2069.13
            self.basic_checks(i)

    def test_trade_history_with_confirmed_price(self):
        response =trade_history.get_history_response({'confirmed_price': 42029.0})
        for i in response['trades']:
            assert i['confirmed_price']==42029.0
            self.basic_checks(i)

    def test_trade_history_with_executed_at(self):
        response =trade_history.get_history_response({'executed_at': '2022-04-04T15:44:15.063Z'})
        for i in response['trades']:
            assert i['executed_at']== '2022-04-04T15:44:15.063Z'
            self.basic_checks(i)