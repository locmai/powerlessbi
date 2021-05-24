import click
import yaml
from simple_chalk import green, yellow

def upload():
    data = {}
    with open('./src/config.yaml') as config:
        data = yaml.safe_load(config)

    print(f"Processing for folder {data['report_folder_path']} ...\n")

    print_reports(data['reports'])

    print(yellow("Proceed? (y/N)"))    
def print_reports(reports: dict) -> None:
    for key, value in reports.items():
        msg= f"""------------------
{key} report(s) that will be uploaded by {value["username"]} to their workspace:
{value["files"]}
"""
        print(msg)
        
def main():
    upload()

if __name__ == "__main__":
    main()