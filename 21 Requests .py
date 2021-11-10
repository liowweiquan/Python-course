>>> import requests
>>> r = requests.get("https://www.google.com")
>>> r.status_code
200
>>> r.headers
{'Date': 'Sun, 18 Jul 2021 17:18:13 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Type': 'text/html; charset=ISO-8859-1', 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-Encoding': 'gzip', 'Server': 'gws', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2021-07-18-17; expires=Tue, 17-Aug-2021 17:18:13 GMT; path=/; domain=.google.com; Secure, NID=219=WJ6Ou89-huefEbLmbvQwfxJ2Bq8T95fduYQTB9mJxV_N9qO_R9gdtqIsmjlWBurBPNtv3rBBm2NdR6ev5xi3TcHyr7wgwl2u8QxykYusU0LO5ZCn4FB_VEgr2-mNDwyWDWuP-HkPlNoC4qP6P3h0-KRcSn_wiFQRaDC1oj91eM4; expires=Mon, 17-Jan-2022 17:18:13 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
>>> r.headers["date"]
'Sun, 18 Jul 2021 17:18:13 GMT'
>>> r.text
