
"""from json2xml import json2xml,readfromjson

data = readfromjson("358448 k.kavya 20180323 15-30-00.json")
xml=json2xml.Json2xml(data).to_xml()
print(xml)"""

import os
from json2xml import json2xml,readfromjson
cdir=os.getcwd()
outdir='xml/'

if not os.path.exists(os.path.join(cdir,outdir)):
    os.mkdir(outdir)
for files in os.listdir(os.path.join(cdir,'annotations')):
    if files.endswith('.json'):
        data=readfromjson(os.path.join(cdir,'annotations',files))
        xml=json2xml.Json2xml(data).to_xml()
        name=files.replace('.json','.xml')
        txt_file= open('xml/{}'.format(name),'w')
        txt_file.write(xml)
        txt_file.close()
