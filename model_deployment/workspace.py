from azureml.core import Workspace

ws = Workspace.create(name='model_deployment', # provide a name for your workspace
                      subscription_id='bc0eb6ac-086a-4656-89dd-deb91b94d1b0', # provide your subscription ID
                      resource_group='my_resource_group1', # provide a resource group name
                      create_resource_group=True,
                      location='westeurope') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')