# from ScoutSuite.providers.osc.resources.fcu.ami import OutscaleMachineImages
# from ScoutSuite.providers.osc.resources.fcu.snapshots import Snapshots
# from ScoutSuite.providers.osc.resources.fcu.volumes import Volumes
# from ScoutSuite.providers.osc.resources.fcu.vpcs import FcuVpcs
from ScoutSuite.providers.osc.resources.regions import Regions

class FCU(Regions):
    _children = [
        # (FcuVpcs, 'vpcs'),
        # (OutscaleMachineImages, 'omis'),
        # (Snapshots, 'snapshots'),
        # (Volumes, 'volumes')
    ]

    def __init__(self, facade):
        super(FCU, self).__init__('fcu', facade)

    async def fetch_all(self, regions=None, excluded_regions=None, partition_name='osc', **kwargs):
        # await super(FCU, self).fetch_all(regions, excluded_regions, partition_name)
        await super(FCU, self).fetch_all(regions, excluded_regions)

        for region in self['regions']:
            # self['regions'][region]['instances_count'] =\
            #     sum([len(vpc['instances']) for vpc in self['regions'][region]['vpcs'].values()])
            self['regions'][region]['security_groups_count'] =\
                sum([len(vpc['security_groups']) for vpc in self['regions'][region]['vpcs'].values()])
            # self['regions'][region]['network_interfaces_count'] =\
            #     sum([len(vpc['network_interfaces']) for vpc in self['regions'][region]['vpcs'].values()])

        # self['instances_count'] = sum([region['instances_count'] for region in self['regions'].values()])
        self['security_groups_count'] = sum([region['security_groups_count'] for region in self['regions'].values()])
        # self['network_interfaces_count'] = sum([region['network_interfaces_count'] for region in self['regions'].values()])
