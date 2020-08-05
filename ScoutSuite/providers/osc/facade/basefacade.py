from osc_sdk_python import Gateway
import logging

class OSCBaseFacade(object):
    def __init__(self, session: Gateway = None):
        self.session = session
