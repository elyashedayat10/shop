from decouple import config
from kavenegar import *


def send_otp(phone_number, code):
    try:
        api = KavenegarAPI(config("KAVENEGAR_API_KEY"))
        params = {"sender": "", "receptor": phone_number, "message": f"{code}"}
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
