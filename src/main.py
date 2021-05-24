import click
import yaml
from simple_chalk import green, yellow, red

report_base_path = ''

@click.command()
@click.option('--target','-t', default=None, help='Targeting the team to publish report')
def main(target):
    """A powerless tool to help publishing to PowerBI service"""
    
    data = {}
    with open('./src/config.yaml') as config:
        data = yaml.safe_load(config)

    global report_base_path
    report_base_path = data['report_folder_path']
    print(f"Processing for folder {data['report_folder_path']} ...\n")

    
    report_date = None

    report_data = data['reports']

    if target is not None:
        pass
    else:
        print_reports(report_data)

    proceed_answer = click.prompt(yellow("Proceed? (y/N)"), default='y')

    if proceed_answer == 'y':
        if target is not None:
            pass
        else:
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
        login(value["username"],value["password"])   
        report_files = value["files"]
        for report_file in report_files:
            upload(report_file)
    print(green("Reports uploaded!"))


def login(username: str, password: str):
    print(f"Login with {username} and {password}")


def upload(report_file: str):
    print(f"Uploading {report_base_path}\\{report_file} ... ")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)