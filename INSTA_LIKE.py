import requests
print("DEV: SH4MUL | @N_C_P")
user=input("INSGRAM USER:")
link=input("YOUR POST URL:")
url = "https://api.likesjet.com/freeboost/7"
json_data = {
    'instagram_username': user,
    'link': link,
    'email': 'MRSH4MUL404@gmail.com'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'accept': 'application/json, text/plain, */*',
    'Connection': 'keep-alive',
    'Host': 'api.likesjet.com',
    'content-length': '137',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://likesjet.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://likesjet.com/',
    'accept-language': 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5'
}
response = requests.post(url, json=json_data, headers=headers).json()
message = response.get('message', '')
if "Success! You will receive likes within next few minutes." in message:print("تم الرشق بنجاح")
elif "You can only receive likes once per day." in message:print("انتظر 24 ساعة لإعادة المحاولة")
elif "The Instagram Video Link must be a valid Instagram video link. Here are some example links" in response:print("خطا في الرابط المنشور او الفيديو")
else:
    link_errors = response.get('errors', {}).get('link', [])
    if link_errors:print("الرابط فيه خطا")
    else:print("السيرفر مشغول")