import json
import codecs

# f = open("entgam.txt","r")
# print f.read() 
# print f.readlines()
file = open("final.json", "w")

# line = f.readline()
i = 1
with open('entgam.txt', encoding='utf-8') as f:
	for line in f:
		l = line.split("\t")
		# print(l)
		encoded0 = str.encode(l[0], 'utf-8').decode()
		encoded1 = str.encode(l[1], 'utf-8').decode()
		encoded2 = str.encode(l[2], 'utf-8').decode()
		encoded3 = str.encode(l[3], 'utf-8').decode()
		# print (l[3])
		file.write('{"id":"V1-'+str(i)+'","english":"'+encoded0+'","type":"'+encoded1+'","amharic":"'+encoded3+'","tigrigna":"'+encoded2+'" },')
		# print (json.dumps({"id": "V1-"+str(i),"english": line[0],"type":line[1],"amharic":line[2] }))
		i+=1
		line = f.readline()
		# print line, 

file.close()




# 	{
# "id": "v1-A1",
# "sidamic": "aa ",
# "english": "to give ",
# "amharic": "",
# "seealso": [],
# "synonym": [],
# "antonym": [],
# "example": [],
# "type":"",
# "image": 0
# }