from wn_1 import similarity
import json

text = { 'Rawtext1': "there is a fire in vashi sector 9.", 'Rawtext2' :"there is a fire in andheri sector 9.",
 'Rawtext3' :"there is a fire in andheri sector 9.", 'Rawtext4' :"there is a fire in andheri sector 9." };

json_str = json.dumps(text)
resp = json.loads(json_str)
a = str(resp['Rawtext1'])
b = str(resp['Rawtext2'])
c = str(resp['Rawtext3'])
d = str(resp['Rawtext4'])

print((similarity(a,b)+similarity(a,c)+similarity(a,d))/3)
