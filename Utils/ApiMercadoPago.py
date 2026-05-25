import mercadopago

def GeneratePaymentLink():
    sdk = mercadopago.SDK("APP_USR-3568605179053688-042920-a78349479673b7005a5053242e04d4c4-281165992")

    paymentData = {
        "items": [
            {"id": "1", "title": "NumerologiaDoNome", "quantity": 1, "currency_id": "BRL", "unit_price": 7.99}
        ],
        "back_urls": {
            "success": "http://localhost:8501/",
            "failure": "http://localhost:8501/Numerologia_do_Nome",
            "pending": "http://localhost:8501/Numerologia_do_Nome",
        },
        # "auto_return": "all",
    }
    result = sdk.preference().create(paymentData)
    # print(result)
    payment = result["response"]
    linkStartPayment = payment["init_point"]
    # print(linkStartPayment)
    return linkStartPayment

# GeneratePaymentLink()