#!/usr/bin/python
# x3.py 
# generates an apache conf file for x3 framework

import sys, re, os

conf = '../misc/example.org'
output_conf = 'x3-output.conf'
apache_dir = '/etc/apache2/sites-available/'

document_root = raw_input('DocumentRoot? (ex: sitename_com/trunk/): ')

if not document_root: document_root = 'sitename_com/trunk/'
if not document_root.endswith('/'): document_root = document_root + '/'
if not document_root.startswith('/www/'): document_root = '/www/' + document_root

if ( document_root.find('/') is not -1 ):
        document_root_temp = document_root.split('/')
        document_base_root = filter( None, document_root_temp )
        document_base_root = '/'.join( document_base_root[0:-1] )
        document_base_root = '/' + document_base_root

# vm = raw_input('Which VM? (default=1-2; ex: 1, 2, 1-2, 3-4, 11-12, 15-16 ): ')
# if not vm: vm = '1-2'

server_name = raw_input('ServerName? (ex: www.google.com): ')

if not server_name: server_name = 'www.sitename.com'

#redirect_www = raw_input('Redirect non-www to www? (default=no; ex:y/n): ')
#if not redirect_www: redirect_www = False

redirect_www = False

filename = raw_input('Conf file name? (ex: trumphotel.conf): ')

if not filename: filename=server_name

#logs = raw_input('Logs? (default=no) ')
#if not logs: logs = False else True

#rewrites = raw_input('Include default rewrites? (default=yes; options: y/n): ')
log_files = document_base_root + '/logs/'
server_alias = ''

conf = open(conf, 'rw')
text = conf.read()
                              
regex = re.compile("({%\s*block\s*([a-zA-Z_]+)\s*%})(.*)({%\s*endblock\s*%})",re.IGNORECASE|re.MULTILINE|re.DOTALL)

finds = regex.findall( text )

if ( server_name.startswith('www.') ):
        server_alias = server_name.replace('www.', '')

yes = ['yes', 'y']
no = ['no', 'n']

if redirect_www in yes:
        first = finds[0]
        last = finds[-1]
        text = text.replace( first, '' )
        text = text.replace( last, '' )
else:
        text = re.sub( regex, '', text )


dict = {
        'SERVER_NAME': server_name,
        'DOC_ROOT':document_root,
        'DOC_BASE_ROOT':document_base_root,
        'SERVER_ALIAS':server_alias
}

for x in dict:
        text = text.replace( '${' + x + '}', dict[x] )

try:
    confFile = os.open( apache_dir + filename, os.O_WRONLY | os.O_CREAT | os.O_EXCL )
    os.write( confFile, text )
    os.close ( confFile )
    print 'Virtualhost created at ' + apache_dir + filename

    create = raw_input('Directory to create correct? ' + document_base_root + ' '  )
    if create in yes:
        if not os.path.exists( document_base_root ):
            try:
                os.makedirs( document_root )
                os.makedirs( document_base_root + '/logs/' )
                os.makedirs( document_base_root + '/private/' )
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
