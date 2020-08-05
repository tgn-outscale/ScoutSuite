from ScoutSuite.providers.osc.resources.api.snapshots import Snapshots
#from ScoutSuite.providers.osc.resources.api.volumes import Volumes
#from ScoutSuite.providers.osc.resources.api.vpcs import Vpcs
#from ScoutSuite.providers.osc.resources.api.instances import Instances
from ScoutSuite.providers.osc.resources.regions import Regions


class Api(Regions):
    _children = [
        #(Vpcs, 'vpcs'),
        #(Instances, 'instances'),
        (Snapshots, 'snapshots'),
       # (Volumes, 'volumes')
    ]

    def __init__(self, facade):
        super(Api, self).__init__('api', facade)

    async def fetch_all(self, regions=None, excluded_regions=None, partition_name='aws', **kwargs):
        await super(Api, self).fetch_all(regions, excluded_regions, partition_name=partition_name)

