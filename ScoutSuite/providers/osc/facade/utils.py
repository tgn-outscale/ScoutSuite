from osc_sdk_python import Gateway


class OSCFacadeUtils:
    @staticmethod
    async def get_all_security_groups(session: Gateway):
        response = session.ReadSecurityGroups()
        security_groups = []
        if 'SecurityGroups' in response:
            for security_group in response['SecurityGroups']:
                security_groups.append(security_group)
        return security_groups


    @staticmethod
    def _get_outscale_endpoint(region, version, action):
        return "https://api.{}.outscale.com/api/{}/{}".format(
            region,
            version,
            action
        )
