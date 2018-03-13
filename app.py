import requests
from readability import Document


# https://github.com/buriy/python-readability
# response = requests.get('http://example.com')
# response = requests.get('http://usosdelasticsenlaadministracion.blogspot.com/')
# https://williamjturkel.net/2013/06/15/basic-text-analysis-with-command-line-tools-in-linux/
response = requests.get('http://www.eumed.net/ce/2015/1/tecnologia.html')
doc = Document(response.text)
# print(doc.title())
content = doc.summary()
# print(doc.summary())
file = open('tecnologia.html', 'w')
file.write(content)
file.close()
