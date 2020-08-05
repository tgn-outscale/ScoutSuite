import asyncio

from osc_sdk_python import Gateway

from ScoutSuite.core.console import print_exception
from ScoutSuite.providers.osc.facade.basefacade import OSCBaseFacade
from ScoutSuite.providers.osc.facade.utils import OSCFacadeUtils


class FCUFacade(OSCBaseFacade):
    def __init__(self, session: Gateway, owner_id: str):
        self.owner_id = owner_id

        super(FCUFacade, self).__init__(session)

    async def get_security_groups(self, region: str, vpc: str):
        import logging
        logging.getLogger('scout').critical("Test get_security_groups")
        try:
            return await OSCFacadeUtils.get_all_pages(
                'fcu', region, self.session, 'describe_security_groups', 'SecurityGroups', Filters=filters
            )
        except Exception as e:
            print_exception('Failed to describe FCU security groups: {}'.format(e))
            return []
