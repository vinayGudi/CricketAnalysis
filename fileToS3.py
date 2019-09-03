from google.cloud import storage
import os

testfile="F:\\ds\\Project 001\\SectorData"

bucket_name="raw-bucket-rawdata"
destination_blob_name="testdata"

print(testfile)


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))




for file in os.walk(testfile):
    for csv in file[2]:
        upload_blob(bucket_name,os.path.join(testfile,csv),csv)




