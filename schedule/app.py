'''
Entry point for gunicorn to serve REST API
'''
import falcon

import worker


api = falcon.API()

worker = worker.Resource()
api.add_route('/worker', worker)
