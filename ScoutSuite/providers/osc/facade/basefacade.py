from osc_sdk_python import Gateway
import logging

class OSCBaseFacade(object):
    def __init__(self, session: Gateway = None):
        logging.getLogger('scout').critical(f"Gateway :: {Gateway}")
        self.session = session
