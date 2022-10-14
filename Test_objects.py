import config

# headers = {
#     "x-token-id": config.UAT_TOKEN4
# }

wrong_headers = {
    "x-token-id": config.WRONG_TOKEN
}

order_channel_subscription = {
    "type": "subscribe",
    "channelname": "orders"
}

my_volume_order = {
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 1.5,
    }
}

my_amount_order = {
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTCEUR",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 30000,
        "currency": "EUR",
    }
}

my_wrong_volume_order = {
    "type": "CREATE_ORDER",
    "order": {
        "instrument": "BTC",
        "order_type": "MARKET",
        "side": "BUY",
        "amount": 1.5,
        "unique_client_order_id": "",
        "client_order_id_2": ""
    }
}


bulk_order = {
    "client_bulk_order_id": "my-first-client-bulk-order-id",
    "order_type": "BULK_MARKET",
    "orders": [
        {
            "instrument": "BTCEUR",
            "side": "BUY",
            "amount": 500000,

        },
        {
            "instrument": "BTCEUR",
            "side": "BUY",
            "amount": 0.07,

        },
        {
            "instrument": "BTCEUR",
            "side": "SELL",
            "amount": 1.23,

        },
        {
            "instrument": "LTCEUR",
            "side": "BUY",
            "amount": 102.304,

        },
        {
            "instrument": "LTCEUR",
            "side": "BUY",
            "amount": 105.302
        }
    ]
}

wrong_bulk_order = {
    "client_bulk_order_id": "my-first-client-bulk-order-id",
    "order_type": "BULK_MARKET",
    "orders": [
        {
            "instrument": "BTCEUR",
            "amount": 0.5,

        },
        {
            "instrument": "BTCEUR",
            "side": "BUY",
            "amount": 0.07,

        },
        {
            "instrument": "BTCEUR",
            "side": "SELL",

        },
        {
            "instrument": "LTCEUR",
            "side": "BUY",
            "amount": 102.304,
            "currency": "EUR"
        },
        {}
    ]
}