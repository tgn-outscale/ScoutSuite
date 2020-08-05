
class OSCFacadeUtils:
    @staticmethod
    async def get_all_security_groups(self, session):
        import logging
        logging.getLogger('scout').critical("Test OSCFacadeUtils::get_all_pages()")
        return session.ReadSecurityGroups()
    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
