#!/usr/bin/env python3
"""This script prints the details of all the
archives in the borg repo as well as some of
the details of the borg repo

This script doesn't have any error checking...yet.
"""

import subprocess
import json
from prettytable import PrettyTable as PT
import humanize

""" Change these two to suit your environment """
borg_repo = "/Volumes/BackupDrive/borg/"
borg_cmd = "/usr/local/bin/borg"

archives = []

def get_archives():
    """
    This function gathers the archives in the borg repo
    and assigns it to the 'archives' list
    """
    print("Working on your report...", end='', flush=True)
    arch = subprocess.run([borg_cmd, "list",
        "--format", "{archive}{SPACE}", borg_repo],
        stdout=subprocess.PIPE, text=True)
    archives = arch.stdout.split()
    archive_details(archives)

def repo_details():
    """
    This function gets the repo details and prints them
    """
    details = subprocess.run([borg_cmd, "info", 
        "--json",
        f"{borg_repo}"],
        stdout=subprocess.PIPE, text=True)
    output = details.stdout
    data = json.loads(output)
    print(f"{'Repo: ' : >19} {borg_repo}")
    print(f"{'Encryption: ' : >19} {data['encryption']['mode']}")
    print(f"{'Total size: ' : >19} {humanize.naturalsize(data['cache']['stats']['total_size'])}")
    print(f"{'Compressed size: ' : >19} {humanize.naturalsize(data['cache']['stats']['total_csize'])}")
    print(f"{'Deduplicated size: ' : >19} {humanize.naturalsize(data['cache']['stats']['unique_csize'])}")

def archive_details(archives):
    """
    This function gets all the archive details
    and prints them in table format.
    """
    num_archives = len(archives)
    table = PT()
    table.title = "Borg Backup Report"
    table.field_names = ["Hostname", "Archive", "Date", "Original", "Compressed", "Deduplicated"]
    for x in archives:
        backup = []
        details = subprocess.run([borg_cmd, "info", 
            "--json",
            f"{borg_repo}::{x}"],
            stdout=subprocess.PIPE, text=True)
        output = details.stdout
        data = json.loads(output)
        table.add_row([data['archives'][0]['hostname'],
            data['archives'][0]['name'],
            data['archives'][0]['start'].split("T")[0],
            humanize.naturalsize(data['archives'][0]['stats']['original_size']),
            humanize.naturalsize(data['archives'][0]['stats']['compressed_size']),
            humanize.naturalsize(data['archives'][0]['stats']['deduplicated_size'])])
    table.align["Hostname"] = "l"
    table.align["Archive"] = "l"
    table.align["Original"] = "r"
    table.align["Compressed"] = "r"
    table.align["Deduplicated"] = "r"
    table.sortby = "Date"
    table.reversesort = True
    print("Done!")
    print(table)

def main():
    get_archives()
    repo_details()

if __name__ == "__main__":
    main()
