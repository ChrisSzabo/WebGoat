import venariapi
import os
import click
import urllib3
import traceback
import sys
from venariapi.models import JobStatus,VerifyEndpointInfo
from venariapi import VenariAuth,VenariApi,VenariRequestor

client_id=os.environ['CLIENT_ID']
client_secret=os.environ['CLIENT_SECRET']
master_url=os.environ['VENARI_MASTER_URL']
venari_workspace="WebGoat"

def do_login():
    token_endpoint=VenariApi.get_token_endpoint(master_url)
    auth=VenariAuth.login(token_endpoint,client_secret,client_id)
    if auth is None:
        raise Exception("Invalid login information")
    return VenariApi(auth,master_url)

@click.group()
def cli():
    pass

@cli.command()
def login()->VenariApi:
    do_login()

@cli.command()
def upload_templates():
    api:VenariApi=do_login()
    api.import_template_from_file('scan-template.jobtemplate.json',venari_workspace,"http://webgoat:8080")
    api.import_workflow_from_file('register-user.workflow.yaml',venari_workspace)

@cli.command()
def start_scan():
    api:VenariApi=do_login()
    api.start_job_fromtemplate("CI-CD",venari_workspace,"Authenticated Exploit")

@cli.command()
def export_data():
    pass

if __name__ == '__main__':
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        cli()
    except Exception as e:
        #print(f"login failed: {repr(e)}")
        traceback.print_exc(file=sys.stdout)
        exit(1)
