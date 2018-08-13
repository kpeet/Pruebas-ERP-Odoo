import xmlrpclib
print "Iniciando proceso"
db="cumplo"
username = "kenneth.peet@cumplo.com"
password="papapleto"
url="http://192.168.130.156:8069"

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print "iniciando autenticacion"
uid = common.authenticate(db, username, password, {})

models= xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

print "Enviando nuevo usuario"
id = models.execute_kw(db, uid, password, 'res.partner','create',
[{
'name': 'Cliente desde Python'

}])

print id
