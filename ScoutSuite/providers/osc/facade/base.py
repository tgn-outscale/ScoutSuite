from ScoutSuite.providers.osc.facade.basefacade import OSCBaseFacade
from ScoutSuite.providers.osc.facade.api import ApiFacade
import requests

class OSCFacade(OSCBaseFacade):
    def __init__(self, credentials=None):
        super(OSCFacade, self).__init__()
        self.session = credentials.session
        self._instantiate_facades()

    async def build_region_list(self, service: str, chosen_regions=None,
                        excluded_regions=None, partition_name='osc'):
        regions = requests.post(
            "https://api.eu-west-2.outscale.com/api/latest/ReadRegions").json()["Regions"]
        regions_list = []
        for region in regions:
            regions_list.append(region["RegionName"])
        return regions

    def _instantiate_facades(self):
        self.api = ApiFacade(self.session)