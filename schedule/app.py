'''
Entry point for gunicorn to serve REST API
'''
import falcon

import worker


application = falcon.API()
api = application

worker = worker.Resource()
api.add_route('/worker', worker)
