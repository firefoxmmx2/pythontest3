#!/usr/bin/env python
#coding:utf8

'''异步服务器和模板的测试'''

import tornado.web
import tornado.ioloop

from tornado.web import RequestHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('HelloWorld')

class ProfileHandler(RequestHandler):
    def initialize(self,database=None):
        self.database = database

    def get(self,username):
        self.write('第二个HelloWorld {0}'.format(username))

if __name__ == '__main__':
    settings = {
            'debug':True,
            }
    application = tornado.web.Application([
        (r'/',MainHandler),
        (r'/profile/(.*)',ProfileHandler, dict(database='database')),
        ],**settings)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

