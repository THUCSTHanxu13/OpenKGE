import pymongo
import ctypes
import json

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory


#Get the database
mongo = pymongo.MongoClient("127.0.0.1", 27017)
db = mongo["KG"]
db = db.database
# db.create_index([("uid", pymongo.ASCENDING)])
# db.create_index([("labels.en.value", pymongo.ASCENDING)])
# db.create_index([("labels.zh.value", pymongo.ASCENDING)])

#Get the list of the papers
paperList = []

def PaperListInit():
	print "Loading the papers list..."
	global paperList
	f = open("static/paper/list.txt")
	while (True):
		content = f.readline()
		if (content == ""):
			break
		nid = content.replace("\n", "").replace("\r", "")
		label = f.readline().replace("\n", "").replace("\r", "")
		year = f.readline().replace("\n", "").replace("\r", "")
		writer = f.readline().replace("\n", "").replace("\r", "")
		model = f.readline().replace("\n", "").replace("\r", "")
		title = f.readline().replace("\n", "").replace("\r", "")
		abstract = f.readline().replace("\n", "").replace("\r", "")
		abstract = abstract[0:400]+"..."
		filesrc = f.readline().replace("\n", "").replace("\r", "")
		img = f.readline().replace("\n", "").replace("\r", "")
		img = img.encode("utf-8")
		filesrc = filesrc.encode("utf-8")
		paperList.append({"year":year, "writer":writer, "model":model, "id":nid, "label":label, "title":title, "abstract":abstract, "filesrc":filesrc, "img":img})
	f.close()


# def insert(lists, num, value, Limit):
# 	for i in lists:
# 		if i[0] == num:
# 			return
# 	if (len(lists) < Limit):
# 		lists.append((num, value))
# 	else:
# 		if (lists[Limit - 1][1] > value):
# 			lists[Limit - 1] = (num, value)
# 	i = len(lists) - 1
# 	while (i >= 1):
# 		if (lists[i][1] < lists[i - 1][1]):
# 			j = lists[i]
# 			lists[i] = lists[i-1]
# 			lists[i-1]=j
# 			i = i - 1
# 		else:
# 			break


# # id = "Q33"
# # entity = db.find_one({'id':id})
# # nid = flag[id]
# # hash = []
# # for i in entity['claims']:
# # 	i = i.encode("utf-8")
# # 	if (not i in flagrelation):
# # 		continue
# # 	rel = flagrelation[i]
# # 	idlist = (ctypes.c_int * (Limit + 1))()
# # 	reslist = (ctypes.c_float * (Limit + 1))()
# # 	test.search(nid, rel, idlist, reslist, Limit)
# # 	tot = 0
# # 	for i in idlist:
# # 		if (i == -1):
# # 			break
# # 		if (i in flag1relation):
# # 			continue
# # 		insert(hash, i, reslist[tot], Limit)
# # 		tot = tot + 1
# # print hash
# # a = [(7427, 3.080303907394409), (5700, 3.5079503059387207), (13565, 3.7147023677825928), (322360, 3.855585813522339), (186273, 3.855585813522339), (143187, 3.8603665828704834), (5332733, 3.988929510116577), (3234, 4.023291110992432), (94226, 4.033496856689453), (332438, 4.033496856689453), (10447, 4.054015159606934), (15041, 4.0976643562316895), (159233, 4.0976643562316895), (583337, 4.0976643562316895), (2341290, 4.0976643562316895), (7672, 4.116037368774414), (32998, 4.116037368774414), (5262584, 4.116037368774414), (578939, 4.116037368774414), (3224, 4.116612911224365), (5287729, 4.116612911224365), (979, 4.116612911224365), (37796, 4.116612911224365), (3207, 4.116612911224365), (45654, 4.140870571136475), (374512, 4.140870571136475), (2696448, 4.140870571136475), (14440539, 4.157783031463623), (41579, 4.194014549255371), (50082, 4.194014549255371)]
# # for i in a:
# # 	print flag1[i[0]]

app = Flask(__name__)

@app.route('/')
def root_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)

@app.route('/home')
def home_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)


@app.route('/index')
def index_home():
	global paperList
	info = {"paper":paperList}
	return render_template('home.html', info = info)

@app.route('/index/explore')
def index_explore():
	return render_template('explore.html')

@app.route('/index/researchers')
def index_researchers():
	return render_template('researchers.html')

@app.route('/index/students')
def index_students():
	return render_template('students.html')

@app.route('/index/download')
def index_download():
	return render_template('download.html')

@app.route('/index/contact')
def index_contact():
	return render_template('contact.html')

@app.route('/index/api')
def index_api():
	return render_template('api.html')

@app.route('/index/publications')
def index_publications():
	global paperList
	info = {"paper":paperList}
	return render_template('publications.html', info = info)

# @app.route('/download/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
# 	print filename
# 	return send_from_directory(directory='out', filename=filename)

# # @app.route("/network/<id>")
# # def network(id):
# # 	global flag
# # 	global flag1
# # 	global flagrelation
# # 	global flag1relation
# # 	global Limit
# # 	global test
# # 	entity = db.find_one({'id':id})
# # 	nid = flag[id]
# # 	hash = []
# # 	Limit = 30
# # 	for i in entity['claims']:
# # 		i = i.encode("utf-8")
# # 		if (not i in flagrelation):
# # 			continue
# # 		rel = flagrelation[i]
# # 		idlist = (ctypes.c_int * (Limit + 1))()
# # 		reslist = (ctypes.c_float * (Limit + 1))()
# # 		test.search(nid, rel, idlist, reslist, Limit)
# # 		tot = 0
# # 		for i in idlist:
# # 			if (i == -1):
# # 				break
# # 			if (i in flag1relation):
# # 				continue
# # 			insert(hash, i, reslist[tot], Limit)
# # 			tot = tot + 1
# # 	info['nodes'] = [{'name':'0', 'id':nid, 'amount':10}]
# # 	info['edges'] = []
# # 	tot = 0
# # 	for i in hash:
# # 		tot = tot + 1
# # 		info['nodes'].append({'name':str(tot), 'id':flag1[i[0]], 'amount':i[1]})
# # 		info['edges'].append({'source':0,'target':tot})
# # 	return render_template('network.html', info = info)

# def findname(id):
# 	entity = db.find_one({'id':id})
# 	if entity == None:
# 		return "not found"
# 	if (not 'en' in entity['labels']):
# 		return "not found"
# 	return entity['labels']['en']['value']

# def work(entity):
# 	if entity == None:
# 		return "not found"
# 	info = {}
# 	info['title'] = entity['labels']['en']['value']
# 	if 'en' in entity['descriptions']:
# 		info['description'] = entity['descriptions']['en']['value']
# 	else:
# 		info['description'] = ""
# 	info['table2_name'] = ""
# 	info['table2'] = {}
# 	info['table1_name'] = "Statement"
# 	info['table1'] = {}
# 	# print id
# 	if 'claims' in entity:
# 		for i in entity['claims']:
# 			for j in entity['claims'][i]:
# 				if ('type' in j) and (j['type'] == 'statement') and ('mainsnak' in j):
# 					con = j['mainsnak']
# 					if ('datavalue' in con) and (con['datatype'] == u'wikibase-item'):
# 						rel = i
# 						ent = 'Q' + (str)(con['datavalue']['value']['numeric-id'])
# 						rellink = "/relation/id/%s"%(rel)
# 						entlink = "/entity/id/%s"%(ent)
# 						if not findname(rel) in info['table1']:
# 							info['table1'][findname(rel)] = []
# 						info['table1'][findname(rel)].append({"relation":findname(rel), "tail":findname(ent), "relationlink":rellink, "taillink":entlink})

# 					if ('datavalue' in con) and (con['datatype'] == u'wikibase-property'):
# 						rel = i
# 						ent = 'P' + (str)(con['datavalue']['value']['numeric-id'])
# 						rellink = "/relation/id/%s"%(rel)
# 						entlink = "/entity/id/%s"%(ent)
# 						if not findname(rel) in info['table1']:
# 							info['table1'][findname(rel)] = []
# 						info['table1'][findname(rel)].append({"relation":findname(rel), "tail":findname(ent), "relationlink":rellink, "taillink":entlink})
# 	res = []
# 	for i in info['table1']:
# 		res.append({'relation':i, 'data':info['table1'][i]})
# 	info['table1'] = res
# 	return render_template('entity.html', info = info)

# @app.route("/search")
# def search():
# 	error = None
# 	if request.method == 'POST':
# 		pass
# 	else:
# 		labels = request.args.get('word')
# 		entity = db.find({'labels.en.value':labels})
# 		res = []
# 		for i in entity:
# 			page = {}
# 			page['url'] = '/entity/id/'+i['id']
# 			try:
# 				page['des'] = i['descriptions']['en']['value']
# 			except Exception, err:
# 				page['des'] = ""
# 			page['label'] = i['labels']['en']['value']
# 			res.append(page)
# 		info = {}
# 		info['res'] = res
# 		return render_template('search.html', info = info)
# 		# return work(entity)

# @app.route('/entity/id/<id>')
# def getEntityById(id):
# 	entity = db.find_one({'id':id})
# 	return work(entity)

# @app.route('/entity/uid/<uid>')
# def getEntityByUid(uid):
# 	entity = db.find_one({'uid':uid})
# 	return work(entity)

# #==========================================
# #Load the C
# #==========================================
# print "Wait...Loading the transE model..."
# test = ctypes.CDLL("./VecBase.so")
# test.init()
# print "Ready!!!"

# transEModel = test
# DIMENSION = 50

# #==========================================
# #Get the embedding for each entity or relation
# #==========================================
# @app.route('/entity/embedding/id/<id>')
# def getEntityEmbeddingById(id):
# 	global transEModel
# 	entity = db.find_one({'id':id})
# 	uid = (int)(entity['uid'][1:])
# 	emb = (ctypes.c_float * (DIMENSION + 1))()

# 	print DIMENSION
# 	print uid
#  	transEModel.getEntityVec(uid, emb)
#  	res = []
#  	for i in range(0, DIMENSION):
#  		res.append(emb[i])
#  	return json.dumps(res)

# @app.route('/entity/embedding/uid/<uid>')
# def getEntityEmbeddingByUid(uid):
# 	global transEModel
# 	entity = db.find_one({'uid':uid})
# 	uid = (int)(entity['uid'][1:])
# 	emb = (ctypes.c_float * (DIMENSION + 1))()
#  	transEModel.getEntityVec(uid, emb)
#  	res = []
#  	for i in range(0, DIMENSION):
#  		res.append(emb[i])
#  	return json.dumps(res)

# @app.route('/relation/embedding/id/<id>')
# def getRelationEmbeddingById(id):
# 	global transEModel
# 	entity = db.find_one({'id':id})
# 	uid = (int)(entity['uid'][1:])
# 	emb = (ctypes.c_float * (DIMENSION + 1))()
#  	transEModel.getRelationVec(uid, emb)
#  	res = []
#  	for i in range(0, DIMENSION):
#  		res.append(emb[i])
#  	return json.dumps(res)

# @app.route('/relation/embedding/uid/<uid>')
# def getRelationEmbeddingByUid(uid):
# 	global transEModel
# 	entity = db.find_one({'uid':uid})
# 	uid = (int)(entity['uid'][1:])
# 	emb = (ctypes.c_float * (DIMENSION + 1))()
#  	transEModel.getRelationVec(uid, emb)
#  	res = []
#  	for i in range(0, DIMENSION):
#  		res.append(emb[i])
#  	return json.dumps(res)

# #==========================================
# #Get the database for each entity or relation
# #==========================================
# @app.route('/entity/wikidata/id/<id>')
# def getEntityWikidataById(id):
# 	entity = db.find_one({'id':id})
# 	res = {}
# 	for i in entity:
# 		if (i != '_id' and i!='uid'):
# 			res[i] = entity[i]
# 	return json.dumps(res)

# @app.route('/entity/wikidata/uid/<uid>')
# def getEntityWikidataByUid(uid):
# 	entity = db.find_one({'uid':uid})
# 	res = {}
# 	for i in entity:
# 		if (i != '_id' and i!='uid'):
# 			res[i] = entity[i]
# 	return json.dumps(res)

# @app.route('/relation/wikidata/id/<id>')
# def getRelationWikidataById(id):
# 	entity = db.find_one({'id':id})
# 	res = {}
# 	for i in entity:
# 		if (i != '_id' and i!='uid'):
# 			res[i] = entity[i]
# 	return json.dumps(res)

# @app.route('/relation/wikidata/uid/<uid>')
# def getRelationWikidataByUid(uid):
# 	entity = db.find_one({'uid':uid})
# 	res = {}
# 	for i in entity:
# 		if (i != '_id' and i!='uid'):
# 			res[i] = entity[i]
# 	return json.dumps(res)

# #==========================================
# #Get the embedding for each entity or relation
# #==========================================

# Limit = 30

# @app.route('/entity/nearest/id/<id>')
# def getEntityNearest(id):
# 	entity = db.find_one({'id':id})
# 	uid = (int)(entity['uid'][1:])
# 	rellist = []
# 	for i in entity['claims']:
# 		i = i.encode("utf-8")
# 		rel = db.find_one({'id':i})
# 		rellist.append((int)(rel['uid'][1:]))

# 	relidlist = (ctypes.c_int * (len(rellist) + 1))()
# 	for i in range(0, len(rellist)):
# 		relidlist[i] = rellist[i]
	
# 	print "sdaf"
# 	print uid
# 	idlist = (ctypes.c_int * (Limit + 1))()
# 	reslist = (ctypes.c_float * (Limit + 1))()
# 	test.search(uid, relidlist, len(rellist), idlist, reslist, Limit)
# 	print "gg"
	
# 	res = []
# 	for i in range(0, Limit):
# 		if (reslist[i] >= 0):
# 			print 'E'+(str)(idlist[i])
# 			entity = db.find_one({'uid':'E'+(str)(idlist[i])})
# 			if (entity!=None and ('en' in entity['labels'])):
# 				res.append((idlist[i], entity['id'], entity['labels']['en']['value']))
# 	return json.dumps(res)

if __name__ == '__main__':
	# id = "Q16597"
	# getEntityNearest(id)
	app.debug = True
	app.jinja_env.variable_start_string = '{{{{'
	app.jinja_env.variable_end_string = '}}}}'
	PaperListInit()
	app.run(host='0.0.0.0', port=8000)
