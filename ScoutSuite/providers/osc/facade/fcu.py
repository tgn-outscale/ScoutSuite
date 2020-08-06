import asyncio
import base64
from osc_sdk_python import Gateway
import zlib

from ScoutSuite.core.console import print_exception
from ScoutSuite.providers.osc.facade.basefacade import OSCBaseFacade
from ScoutSuite.providers.osc.facade.utils import OSCFacadeUtils
from ScoutSuite.providers.utils import get_and_set_concurrently
from ScoutSuite.providers.utils import run_concurrently


class FCUFacade(OSCBaseFacade):
    def __init__(self, session: Gateway):
    # def __init__(self, session: Gateway, owner_id: str):
        # self.owner_id = owner_id
        self.session = session
        super(FCUFacade, self).__init__(session)

    async def get_security_groups(self, region: str, vpc: str = None):
        import logging
        logging.getLogger('scout').critical("OSC ::: FCUFacade::get_security_groups()")
        try:
            # return await OSCFacadeUtils.get_all_pages(
            #     'fcu', region, self.session, 'describe_security_groups', 'SecurityGroups', Filters=filters
            # )
            security_groups = await OSCFacadeUtils.get_all_security_groups(self.session)
            return security_groups
        except Exception as e:
            print_exception('Failed to describe FCU security groups: {}'.format(e))
            return []
