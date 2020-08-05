# from ScoutSuite.providers.osc.resources.fcu.ami import OutscaleMachineImages
# from ScoutSuite.providers.osc.resources.fcu.snapshots import Snapshots
# from ScoutSuite.providers.osc.resources.fcu.volumes import Volumes
# from ScoutSuite.providers.osc.resources.fcu.vpcs import FcuVpcs
from ScoutSuite.providers.osc.resources.fcu.securitygroups import SecurityGroups
from ScoutSuite.providers.osc.resources.regions import Regions

class FCU(Regions):
    _children = [
        (SecurityGroups, 'security_groups')
        # (FcuVpcs, 'vpcs'),
        # (OutscaleMachineImages, 'omis'),
        # (Snapshots, 'snapshots'),
        # (Volumes, 'volumes')
    ]

    def __init__(self, facade):
        super(FCU, self).__init__('fcu', facade)
        import logging
        logging.getLogger("scout").critical("OSC ::: Ressource FCU\n\n\n\n\n")

    async def fetch_all(self, regions=None, excluded_regions=None, partition_name='osc', **kwargs):
        # await super(FCU, self).fetch_all(regions, excluded_regions, partition_name)
        import logging
        logging.getLogger("scout").critical("OSC ::: FCU.fetch_all()\n\n\n")
        await super(FCU, self).fetch_all(regions, excluded_regions)
        logging.getLogger("scout").critical("OSC ::: ! FCU.fetch_all()\n\n\n")

        logging.getLogger("scout").critical("Regions :::")
        logging.getLogger("scout").critical(self['regions'])
        for region in self['regions']:
            logging.getLogger("scout").critical(f"OSC ::: region :: {region}")
            logging.getLogger("scout").critical(f"OSC ::: {self['regions'][region]}")
            # logging.getLogger("scout").critical(self['regions'][region]['security_groups'].values())
            # self['regions'][region]['security_groups_count'] =\
            #     sum([len(sg) for sg in self['regions'][region]['security_groups'].values()])
            # self['regions'][region]['instances_count'] =\
            #     sum([len(vpc['instances']) for vpc in self['regions'][region]['vpcs'].values()])
            # self['regions'][region]['security_groups_count'] =\
            #     sum([len(vpc['security_groups']) for vpc in self['regions'][region]['vpcs'].values()])
            # self['regions'][region]['network_interfaces_count'] =\
            #     sum([len(vpc['network_interfaces']) for vpc in self['regions'][region]['vpcs'].values()])

        # self['instances_count'] = sum([region['instances_count'] for region in self['regions'].values()])
        # self['security_groups_count'] = sum([region['security_groups_count'] for region in self['regions'].values()])
        # self['network_interfaces_count'] = sum([region['network_interfaces_count'] for region in self['regions'].values()])
