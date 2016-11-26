'''
Module for handling worker requests with REST API
'''

import falcon


class Resource(object):
    '''
    Class to contain worker resource object
    '''
    def on_get(self, req, resp):
        resp.body = '{"body": "Hello World!"}'
        resp.status = falcon.API()
