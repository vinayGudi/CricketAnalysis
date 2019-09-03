from google.cloud import automl_v1beta1 as automl
from google.oauth2 import service_account


project_id = 'testproject-250605'
compute_region = 'us-central1'
dataset_id = 'TBL8278535306827792384'
path =  'bq://testproject-250605.testset.testtable'
dataset_name = 'testsetfinal'













"""
client = automl.TablesClient(
credentials=service_account.Credentials.from_service_account_file('./account.json'),project='testproject-250605',
region='us-central1')




d = client.get_dataset(dataset_display_name='testset')

m = client.create_model('my_model', train_budget_milli_node_hours=1000,dataset_display_name=d)  #to create a ml  model 



""""""client.batch_predict(
    gcs_input_uris="https://storage.cloud.google.com/raw-bucket-rawdata/Auto%20Data.csv",
    gcs_output_uri_prefix="https://storage.cloud.google.com/raw-bucket-rawdata/",
    model_display_name="my_model").result()


project_id = 'testproject-250605'
compute_region = 'us-central1'"""




client = automl.AutoMlClient(credentials=service_account.Credentials.from_service_account_file('./account.json'))

# A resource that represents Google Cloud Platform location.
project_location = client.location_path(project_id, compute_region)

##############################################################################################
def dataset_creation():
    # Set dataset name and metadata of the dataset.
    my_dataset = {
    "display_name": dataset_name,
    "tables_dataset_metadata": {}
}

    # Create a dataset with the dataset metadata in the region.
    dataset = client.create_dataset(project_location, my_dataset)

    # Display the dataset information.
    print("Dataset name: {}".format(dataset.name))
    print("Dataset id: {}".format(dataset.name.split("/")[-1]))
    print("Dataset display name: {}".format(dataset.display_name))
    print("Dataset metadata:")
    print("\t{}".format(dataset.tables_dataset_metadata))
    print("Dataset example count: {}".format(dataset.example_count))
    print("Dataset create time:")
    print("\tseconds: {}".format(dataset.create_time.seconds))
    print("\tnanos: {}".format(dataset.create_time.nanos))
#####################################################################################################
def import_data_to_dataset():
    dataset_full_id = client.dataset_path(project_id, compute_region, dataset_id)

    if path.startswith('bq'):
        input_config = {"bigquery_source": {"input_uri": path}}
    else:
        # Get the multiple Google Cloud Storage URIs.
        input_uris = path.split(",")
        input_config = {"gcs_source": {"input_uris": input_uris}}

    # Import data from the input URI.
    response = client.import_data(dataset_full_id, input_config)

    print("Processing import...")
    # synchronous check of operation status.
    print("Data imported. {}".format(response.result()))

##################################################################################################
import_data_to_dataset()


