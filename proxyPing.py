import requests

siteList = [
	"https://google.com",
	"http://store.nike.com/us/en_us/",
	"http://www.adidas.com/us/yeezy",
	"http://www.adidas.com/us",
	"http://www.supremenewyork.com/shop/all"
]

proxies = [
	"123.123.123.123:1234"
	]

userAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
for site in siteList:
	for proxy in proxies:
		try:
			r = requests.get(site,proxies={"http":proxy,"https":proxy},timeout=5,headers=userAgent)
			print(site + " - Status Code: " + str(r.status_code))
		except:
			print(site + " - " + "Banned!")
