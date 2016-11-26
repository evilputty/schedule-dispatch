'''
Entry point for gunicorn to serve REST API
'''
import falcon

import worker


api = application = falcon.API()

worker = worker.Resource()
api.add_route('/worker', worker)
