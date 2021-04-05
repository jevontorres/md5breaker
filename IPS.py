import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
file1 = open('hashes.txt', 'r')

for line in file1:
	testhash = line.strip()
	testurl = f"https://md5.gromweb.com/?md5={testhash}"
	browser.open(testurl)
	test = browser.page.find(class_="long-content string")
	print(test.string)