import logging
#import os
#import sys
#import datetime

#from google.appengine.api import app_identity
from flask import Flask, request
#import cloudstorage as gcs
from google.cloud import bigquery

# Set up file attributes
app = Flask(__name__)
#app_bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())


@app.route('/_ah/start')
def instance_start():
    """ Called when the GAE app instance starts. Manual scaling invokes this
    when the instance is started, basic scaling will invoke this when the
    first request comes in
    """
    # Do nothing for this service on start
    logging.info("Service received start request")
    return ""


# noinspection PyPep8,PyBroadException
@app.route('/load/csv/')
def loadcsv():
    schema = [
    bigquery.SchemaField('location', 'STRING', 'NULLABLE',
     'LOCATION'),
    bigquery.SchemaField('name', 'STRING', 'NULLABLE',
     'NAME'),
    bigquery.SchemaField('age', 'STRING', 'NULLABLE',
     'AGE'),
    bigquery.SchemaField('color', 'STRING', 'NULLABLE',
     'COLOR'),
    bigquery.SchemaField('coffee', 'STRING', 'NULLABLE',
     'COFFEE')
    ]
    client = bigquery.Client('my-second-proj-205311')
    dataset = client.dataset('my_dataset')
    #obj = gcs.listbucket('my-awesomesach-bucketsach/incoming',page_size = 100)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    job_config.skip_leading_rows = 1
    job_config.schema = schema
    ob = client.load_table_from_uri(('gs://' + 'my-awesomesach-bucketsach/data/' + 'data.csv'), dataset.table('sachin1'),
                                                       job_config=job_config)

    return "Files moved to bigquery"


