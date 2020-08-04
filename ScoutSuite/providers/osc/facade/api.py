from ScoutSuite.providers.osc.facade.basefacade import OSCBaseFacade
from osc_sdk_python import Gateway
from ScoutSuite.providers.osc.facade.utils import OSCFacadeUtils
from ScoutSuite.core.console import print_exception


class ApiFacade(OSCBaseFacade):

    def __init__(self, session: Gateway):
        super(ApiFacade, self).__init__(session)

    async def get_instances(self, region: str):
        try:
            instances = OSCFacadeUtils.get_all_instances(self.session)
        except Exception as e:
            print_exception('Failed to describe instances: {}'.format(e))
            return []

