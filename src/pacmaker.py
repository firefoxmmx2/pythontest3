#!/usr/bin/env python
#Filename: pacmaker.py

'''
用于生成一个自动代理的脚本,使用autoproxy规则
'''

import os
from optparse import OptionParser
from urllib.request import urlopen
import urllib.parse as urlparse
import base64


port = 80
protol = 'HTTP'
host = 'localhost'

avail_protol = ('HTTP','SOCK4','SOCK5',)
output = os.path.realpath('.') + os.path.sep + 'pacmaked.pac'
autoproxy_gfwlist = "http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt"
online_proxy = (
        (
            'http://www.8qi8.com/proxy.php',
            {
                'server':'http://co.xinyali.info',
                'url':autoproxy_gfwlist
            }
        ),
        )
gfwlist_file = None


def make_pac():
   # data = urlparse.urlencode(online_proxy[0][1]).encode('utf8')
    #res = urlopen(online_proxy[0][0],data)
    #gfwlist = res.read().decode('utf-8')
    #print({'gfwlist':gfwlist})
    #gfwlist = base64.decodestring(gfwlist)
    #print(gfwlist)
    
    gfwlist=None
    if gfwlist_file:
        with open(gfwlist_file,'r') as gfwfile:
            gfwlist = gfwfile.read()
            gfwlist = base64.b64decode(gfwlist).decode()

    pac_content = '''
    function regExpMatch(url, pattern) {
	    try { return new RegExp(pattern).test(url); } catch(ex) { return false; }
    }

    function FindProxyForURL(url, host) {
        %s
        return "DIRECT";
    }
    '''
    pac_part = []

    
    for line in (i for i in gfwlist.split('\n') if i.find("!-") != 0):
        return_str = 'return "{protol} {host}:{port}; DIRECT"; \n'.format(
                protol=protol,
                host=host,
                port=port
                )
        print(line)
        if line.find('@@') == 0:
            return_str = 'return "DIRECT"; \n'
            line = line[2:]
        if line.find('||') == 0:
            line = line[2:]
            match_str = line.replace('.',r'\\.')
            match_str = match_str.replace('/',r'\\/')

            if_str = r'     if(regExpMatch(url,"^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?{match}"))'.format(match=match_str)
        else:
            if_str = r'     if(shExpMatch(url, "http://*' + line + '*"))'

        pac_part.append(if_str+' '+return_str)

    #print(''.join(pac_part))
    print(pac_content % (''.join(pac_part)))
    pac_content = pac_content % (''.join(pac_part))

if __name__ == '__main__':
    usage = 'usage: %prog [option]'
    parser = OptionParser(usage=usage)
    
    parser.add_option('-o','--output',help='output file',dest='output',default=output)
    parser.add_option('-H','--host',help='hostname or ip of proxy',dest='host',default=host)
    parser.add_option('-p','--port',help='port of proxy',dest='port',default=port)
    parser.add_option('-t','--type',help='type of proxy',dest='protol',default=protol)
    parser.add_option('-i','--input',help="autoproxy input file",dest='input')
    (options,args) = parser.parse_args()
    
    print(options)
    
    if options.protol.upper() not in avail_protol:
        raise Exception('it\'s not support proxy protol.')
    
    protol = options.protol.upper()
    port = options.port
    host = options.host
    output = options.output
    gfwlist_file = options.input

    make_pac()
