from ScoutSuite.providers.osc.resources.fcu.securitygroups import SecurityGroups
from ScoutSuite.providers.osc.resources.regions import Regions
from ScoutSuite.providers.osc.resources.fcu.volumes import Volumes


class FCU(Regions):
    _children = [
        (SecurityGroups, 'security_groups')
        # (Volumes, 'volumes')
    ]

    def __init__(self, facade):
        super(FCU, self).__init__('fcu', facade)

    async def fetch_all(self, regions=None, excluded_regions=None, partition_name='osc', **kwargs):
        await super(FCU, self).fetch_all(regions, excluded_regions)
        for region in self['regions']:
            self['regions'][region]['security_groups_count'] =\
                sum([len(sg) for sg in self['regions'][region]['security_groups'].values()])
            self['regions'][region]['volumes_count'] =\
                sum([len(volumes['volumes']) for volumes in self['regions'][region]['volumes'].values()])
        self['security_groups_count'] = sum([region['security_groups_count'] for region in self['regions'].values()])
