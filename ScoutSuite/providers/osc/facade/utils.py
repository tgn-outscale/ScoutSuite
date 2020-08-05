from osc_sdk_python import Gateway


class OSCFacadeUtils:
    @staticmethod
    async def get_all_security_groups(session: Gateway):
        import logging
        logging.getLogger('scout').critical("OSC ::: OSCFacadeUtils::get_security_groups()")
        logging.getLogger('scout').critical(f"session ::: {session}")
        return session.ReadSecurityGroups()

    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
