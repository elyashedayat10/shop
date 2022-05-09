from decouple import config
from kavenegar import *


def send_otp(phone_number, code):
    try:
        api = KavenegarAPI(config("KAVENEGAR_API_KEY"), timeout=20)
        params = {
            "receptor": phone_number,
            "template": "",
            "token": code,
            "type": "sms",
        }
        response = api.verify_lookup(params)
        print(response)

    except APIException as e:
        print(e)

    except HTTPException as e:
        print(e)
