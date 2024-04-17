URL = 'https://www.scrapethissite.com/pages/simple/'
s = requests.Session()
r=s.get(URL)
r=s.post(url + suburl, params=payload, headers=headers) 