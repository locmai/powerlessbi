import click
import yaml
from simple_chalk import yellow, red, greenBright

import sys
import subprocess

report_base_path = "G:\\.shortcut-targets-by-id\\target+_id\\Power BI report"

def psrun(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode != 0:
        print(red(f"An error occured: {completed.stderr}"))

@click.command()
def main():
    """A powerless tool to help publishing to PowerBI service\n
    The configuration file should be at C:\\Users\\lmai\\Desktop\\config
    """
   
    data = {}
    with open('C:\\Users\\ngoctrinh\\Desktop\\config.yaml') as config:
        data = yaml.safe_load(config)

    global report_base_path  

    report_data = data['reports']

    print_reports(report_data)

    proceed_answer = click.prompt(yellow("Proceed? (y/N)"), default='y')

    if proceed_answer == 'y':
        upload_reports(data['reports'])
    else:
        print(red('Aborted!'))


def print_reports(reports: dict) -> None:
    for key, value in reports.items():
        msg= f"""------------------
{key} report(s) that will be uploaded by {value["username"]} to their workspace:
{value["files"]}
"""
        print(msg)
       

def upload_reports(reports: dict) -> None:
    for key, value in reports.items():
        report_files = value["files"]    
        login_and_upload(value["username"],value["password"], report_files)  
       
    print(greenBright("Reports uploaded!"))

def login_and_upload(username: str, password: str, report_files: list):
    print(f"Login with {username} to upload the reports: {report_files}")
    pscmds = [
        f"$username = \"{username}\"",
        f"$password = ConvertTo-SecureString \"{password}\" -AsPlainText -Force",
        "$psCred = New-Object System.Management.Automation.PSCredential -ArgumentList ($username, $password)",
        "Connect-PowerBIServiceAccount -Credential $psCred",
    ]
   
    uploadcmds = [f"New-PowerBIReport -Path \"{report_base_path}\\{report_file}.pbix\" -Name \"{report_file}\" -ConflictAction CreateOrOverwrite" for report_file in report_files]
    logincmd = ";".join(pscmds)
    uploadcmd = ";".join(uploadcmds)
    fullcmd = f"{logincmd};{uploadcmd}"
    print(uploadcmd)
    psrun(fullcmd)
   
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)