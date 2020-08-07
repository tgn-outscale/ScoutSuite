from ScoutSuite.providers.osc.resources.base import OSCResources
from ScoutSuite.providers.osc.facade.base import OSCFacade
from ScoutSuite.utils import manage_dictionary

import logging


class Volumes(OSCResources):
    def __init__(self, facade: OSCFacade, region: str, vpc: str = None):
        super(Volumes, self).__init__(facade)
        self.region = region
        self.vpc = vpc

    async def fetch_all(self, regions=None, excluded_regions=None, partition_name='osc', **kwargs):
        try:
            raw_volumes = await self.facade.fcu.get_volumes(self.region)
            for raw_volume in raw_volumes:
                name, resource = self._parse_volumes(raw_volume)
                self[name] = resource
        except Exception as e:
            logging.warning(e)

    def _parse_volume(self, raw_volume):
        volume = {}
        volume['size'] = raw_volume['Size']
        volume['id'] = raw_volume['VolumeId']
        volume['type'] = raw_volume['VolumeType']
        volume['snapshot_id'] = raw_volume['SnapshotId']
        volume['state'] = raw_volume['State']
        volume["rules"] = []
        return volume['id'], volume

    def _parse_volume_rules(self, rules):
        protocols = {}
        rules_count = 0
        for rule in rules:
            # @TODO find ome rule to put here
            rules_count += 1

        return protocols, rules_count
