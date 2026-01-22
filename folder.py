import urllib.request, BeautifulSoup
#connect to a site
r = urllib.request.urlopen("https://goal.com")
text = r.read()
#parse into beautifulsoup
soup = BeautifulSoup.BeautifulSoup(text)
soup.contents[0].name