from ScoutSuite.providers.osc.resources.base import OSCResources
from ScoutSuite.providers.osc.facade.base import OSCFacade
from ScoutSuite.utils import manage_dictionary
from ScoutSuite.core.fs import load_data

import logging

class SecurityGroups(OSCResources):
    def __init__(self, facade: OSCFacade, region: str, vpc: str):
        logging.getLogger("scout").critical("OSC Security Groups\n\n\n\n\n")
        super(SecurityGroups, self).__init__(facade)
        self.region = region
        self.vpc = vpc

    async def fetch_all(self):
        raw_security_groups = await self.facade.fcu.get_security_groups()
        for raw_security_group in raw_security_groups:
            name, resource = self._parse_security_group(raw_security_group)
            self[name] = resource

    def _parse_security_group(self, raw_security_group):
        security_group = {}
        security_group['name'] = "" # raw_security_group[""]
        security_group['id'] = 0 # raw_security_group[""]

        return security_group['id'], security_group