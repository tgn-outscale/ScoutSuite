from ScoutSuite.core.console import print_exception
from ScoutSuite.providers.aws.facade.basefacade import AWSBaseFacade
from ScoutSuite.providers.aws.facade.utils import AWSFacadeUtils


class DynamoDBFacade(AWSBaseFacade):

    async def get_backups(self, region: str):
        try:
            return await AWSFacadeUtils.get_all_pages('dynamodb', region, self.session, 'list_backups',
                                                      'BackupSummaries')
        except Exception as e:
            print_exception('Failed to get DynamoDB Backups: {}'.format(e))
            return []

    async def get_tables(self, region: str):
        try:
            return await AWSFacadeUtils.get_all_pages('dynamodb', region, self.session, 'list_tables', 'TableNames')
        except Exception as e:
            print_exception('Failed to get DynamoDB Tables: {}'.format(e))
            return []

    async def get_tags_of_resource(self, region: str, resource_arn: str):
        try:
            return await AWSFacadeUtils.get_all_pages('dynamodb', region, self.session, 'list_tags_of_resources', 'Tags', ResourceArn=resource_arn)
        except Exception as e:
            print_exception('Failed to get DynamoDB Tags on Resource: {}'.format(e))
            return []
