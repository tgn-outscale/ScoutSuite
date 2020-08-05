import json
import requests


class OSCFacadeUtils:
    @staticmethod
    def get_all_pages(self, session):
        return session.ReadVms
    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
