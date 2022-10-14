import uuid
import io
import json
import csv


wrong_buy_orders = [{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUYY",
        "amount": 1.5,
        "unique_client_order_id": str(uuid.uuid4()),
        "client_order_id_2": str("Hello World!")
    }
},{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEU",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 1.5,
        "unique_client_order_id": str(uuid.uuid4()),
        "client_order_id_2": str("Hello World!")
    }
},{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 0.0000000000000000000000000000000000000000001,
        "unique_client_order_id": str(uuid.uuid4()),
        "client_order_id_2": str("Hello World!")
    }
},{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 15000000000000000000000000000000000000000000,
        "unique_client_order_id": str(uuid.uuid4()),
        "client_order_id_2": str("Hello World!")
    }
},{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 1.5,
        "unique_client_order_id": "1aaa525b-8434-4e79-9032-8e5d44462f83",
        "client_order_id_2": str("Hello World!")
    }
},{
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 25,
        "unique_client_order_id": str(uuid.uuid4()),
        "client_order_id_2": str("Hello World!")
    }
},]
class GetBulkOrder:
    @staticmethod
    def get_default_bulk_order():
        return {
            "client_bulk_order_id": "my-first-client-bulk-order-id",
            "order_type": "BULK_MARKET",
            "orders": [
                {
                    "instrument": "XRPEUR",
                    "side": "BUY",
                    "amount": 0.05,
                    "unique_client_order_id": "In a bulk order, this is not unique.",
                    "client_order_id": "my client order id 1",
                    "client_order_id_1": "my second client order id 1"
                },
                {
                    "instrument": "BTCEUR",
                    "side": "BUY",
                    "amount": 0.05,
                    "unique_client_order_id": "In a bulk order, this is not unique.",
                    "client_order_id_1": "my second client order id 2"
                },
                {
                    "instrument": "BTCEUR",
                    "side": "SELL",
                    "amount": 0.05,
                    "unique_client_order_id": "In a bulk order, this is not unique.",
                    "client_order_id": "my client order id 2",
                    "client_order_id_1": "my second client order id 3",
                    "client_order_id_2": "my third client order id 3"
                },
                {
                    "instrument": "LTCEUR",
                    "side": "BUY",
                    "amount": 0.05,
                    "unique_client_order_id": "In a bulk order, this is not unique.",
                    "client_order_id": "my client order id 3",
                    "client_order_id_1": "my second client order id 4"
                },
                {
                    "instrument": "LTCEUR",
                    "side": "BUY",
                    "amount": 0.05
                }
            ]
        }
    @staticmethod
    def get_bulk_order_with_wrong_order_id():
        default_bulk_order=GetBulkOrder.get_default_bulk_order()
        default_bulk_order['client_bulk_order_id']=""
        return default_bulk_order
    @staticmethod
    def get_bulk_order_with_wrong_instrument():
        default_bulk_order = GetBulkOrder.get_default_bulk_order()
        print(default_bulk_order['orders'][0]['instrument'])
        default_bulk_order['orders'][0]['instrument'] = ""
        return default_bulk_order

    @staticmethod
    def get_bulk_order_with_wrong_side():
        default_bulk_order = GetBulkOrder.get_default_bulk_order()
        default_bulk_order['orders'][0]['side'] = ""
        return default_bulk_order


    @staticmethod
    def get_bulk_order_with_large_amount():
        default_bulk_order = GetBulkOrder.get_default_bulk_order()
        default_bulk_order['orders'][0]['amount'] = 10**50
        return default_bulk_order

    @staticmethod
    def get_bulk_order_with_small_amount():
        default_bulk_order = GetBulkOrder.get_default_bulk_order()
        default_bulk_order['orders'][0]['amount'] = 10**-50
        return default_bulk_order

    @staticmethod
    def get_bulk_order_with_no_orders_key():
        return {"client_bulk_order_id": "my-first-client-bulk-order-id",
            "order_type": "BULK_MARKET"}
    @staticmethod
    def get_bulk_orders_with_empty_orders():
        return {"client_bulk_order_id": "my-first-client-bulk-order-id",
            "order_type": "BULK_MARKET","orders":[]}

    @staticmethod
    def get_bulk_order_with_wrong_order_type():
        default_bulk_order = GetBulkOrder.get_default_bulk_order()
        default_bulk_order['order_type'] = ""
        return default_bulk_order
my_bulk_order_in_memory_file = io.StringIO(
    json.dumps(GetBulkOrder.get_default_bulk_order())
)

currencyMaster=open("C:/Users/jtannoury/Desktop/otc-app-tests/joseph/tests/currencyMaster.csv")
currencyMaster=csv.DictReader(currencyMaster)
csv_data={}
for row in currencyMaster:
    csv_data[row['Currency Code']]=row
currencyMaster=csv_data