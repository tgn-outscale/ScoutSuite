from ScoutSuite.providers.osc.resources.base import OSCResources
from ScoutSuite.providers.osc.facade.base import OSCFacade


class Snapshots(OSCResources):

    def __init__(self, facade: OSCFacade, region: str):
        super(Snapshots, self).__init__(facade)
        self.region = region

    async def fetch_all(self):
        raw_snapshots = await self.facade.api.list_snapshots()
        for raw_snapshot in raw_snapshots:
            name, resource = self._parse_snapshot(raw_snapshot)
            self[name] = resource