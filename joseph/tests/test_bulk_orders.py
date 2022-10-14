from joseph.APIs.bulk_orders import *
from joseph.tests.variables import *
import io
from decimal import *
getcontext().prec=1
class TestBulkOrders:

    def test_bulk_orders_with_wrong_id(self):
        assert get_bulk_order(GetBulkOrder.get_bulk_order_with_wrong_order_id()['client_bulk_order_id'])['error_description']== 'Cannot convert access token to JSON'

    def test_bulk_orders_with_wrong_instrument(self):
        assert send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_wrong_instrument())),custom_order_state=True)['order_rejections'][0]["error_description"]== 'Invalid instrument'

    def test_bulk_orders_with_wrong_side(self):
        assert send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_wrong_side())),custom_order_state=True)['order_rejections'][0]["error_description"]== 'Invalid side'

    def test_bulk_orders_with_large_amount(self):
        response=send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_large_amount())),
                               custom_order_state=True)['error_description']
        assert 'The maximum amount for' in response or  response=='Your collateral does not allow for this trade to be executed. Consider increasing your collateral.'

    def test_bulk_orders_with_small_amount(self):
        assert 'The amount is too low: The smallest acceptable unit of' in send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_small_amount())),
                               custom_order_state=True)['order_rejections'][0]['error_description']

    def test_bulk_orders_with_no_orders_key(self):
        assert send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_no_orders_key())),
                               custom_order_state=True)[
                   'error_description'] ==  'Invalid Format'

    def test_bulk_orders_with_empty_orders_key(self):
        assert send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_orders_with_empty_orders())),
                               custom_order_state=True)['bulk_order_status'] == 'rejected'
    def test_bulk_orders_with_wrong_order_type(self):
        assert send_bulk_order(io.StringIO(json.dumps(GetBulkOrder.get_bulk_order_with_wrong_order_type())),
                               custom_order_state=True)['order_rejections'][0]['error_description']==  'Invalid Order Type'

    def test_happy_case(self):
        response=send_bulk_order()['order_confirmations']
        # for i in response:
        print(response)