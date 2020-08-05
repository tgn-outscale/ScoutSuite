
class OSCFacadeUtils:
    @staticmethod
    def get_all_security_groups(session):
        return session.ReadSecurityGroups()
    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
