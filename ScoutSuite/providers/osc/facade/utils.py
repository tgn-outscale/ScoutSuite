import json
import requests


class OSCFacadeUtils:
    @staticmethod
    async def get_all_pages(self, session):
        import logging
        logging.getLogger('scout').critical("Test OSCFacadeUtils::get_all_pages()")
        return session.ReadVms()
    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
