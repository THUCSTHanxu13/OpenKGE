f = open("home.html", "r")
ff = open("res.html", "w")
import re

def work(content, f1):
	if (content.find(f1)!=-1):
		if (content.find("href")!=-1):
			gg = re.findall('''href=".*?"''',content)[0]
			gg = gg.replace("href=","").replace('''"''',"")
		else:
			gg = re.findall('''src=".*?"''',content)[0]
			gg = gg.replace("src=","").replace('''"''',"")
		content = content.replace(gg, "{{url_for('static', filename='"+ gg + '''')}}''')
		return True, content
	return False, content

def work1(content, f1):
	if (content.find(f1)!=-1):
		if (content.find("src")!=-1):
			gg = re.findall('''src=".*?"''',content)[0]
			gg = gg.replace("src=","").replace('''"''',"")
		else:
			gg = re.findall('''href=".*?"''',content)[0]
			gg = gg.replace("href=","").replace('''"''',"")
		content = content.replace(gg, "{{url_for('static', filename='"+ gg + '''')}}''')
	return content

while (True):
	content =  f.readline()
	if content == "":
		break
	flag = False
	flag, content = work(content, "bootstrap/")
	if (flag):
		ff.write(content)
		continue
	flag, content = work(content, "css/")
	if (flag):
		ff.write(content)
		continue
	flag, content = work(content, "fonts/")
	if (flag):
		ff.write(content)
		continue
	flag, content = work(content, "js/")
	if (flag):
		ff.write(content)
		continue
	flag, content = work(content, "plugins/")
	if (flag):
		ff.write(content)
		continue
	flag, content = work(content, "images/")
	if (flag):
		ff.write(content)
		continue
	ff.write(content)



	

	# if (content.find("images/")!=-1):
	# 	print content

	# 	if (content.find("src")!=-1):
	# 		gg = re.findall('''src=".*?"''',content)[0]
	# 		print gg
	# 	else:	
	# 		gg = re.findall('''href=".*?"''',content)[0]
	# 		print gg
	
	
ff.close()
f.close()
