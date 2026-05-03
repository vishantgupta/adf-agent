from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

# your details
subscription_id = "4fc3407d-e164-4150-b5bd-00694b941cb5"
resource_group = "vishantRG"
factory_name = "TestAEVishant"

# auth
credential = DefaultAzureCredential()

# client
client = DataFactoryManagementClient(credential, subscription_id)

# list pipelines
pipelines = client.pipelines.list_by_factory(resource_group, factory_name)

for p in pipelines:
    print("Pipeline:", p.name)

    # get full pipeline JSON
    pipeline_detail = client.pipelines.get(resource_group, factory_name, p.name)
    print(pipeline_detail.as_dict())