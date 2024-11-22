#!/usr/bin/python

import subprocess
import socket
from datetime import datetime
import os
import re


def main():
    # Date
    uptime_formatted=get_command_output("uptime | cut -d ',' -f1  | cut -d ' ' -f4,5")
    date_formatted=datetime.today().strftime("%H:%M %d-%m-%Y")

    # Linux version
    # get the Linux version but remove the "-1-ARCH" part
    linux_version=get_command_output("uname -r | cut -d '-' -f1")

    # Battery info
    # returns the battery status: "Full", "Discharging", or "Charging".
    battery_status=get_command_output("cat /sys/class/power_supply/BAT0/status")
    battery_percentage=get_command_output("cat /sys/class/power_supply/BAT0/capacity")
    battery_icon = "🔋" if battery_status == "Discharging" else "🔌"

    # IP
    ip_addr = socket.gethostbyname(socket.gethostname())
    vpn_status = "🔐" if os.path.isdir("/proc/sys/net/ipv4/conf/ppp0") else "🔓"

    # Disk space
    disk_infos = parse_diskinfos(get_command_output('df -h /'))

    disk_freespace = disk_infos['size']
    disk_usedspace = disk_infos['used']
    disk_usedpercentage = disk_infos['use%']

    # Output
    print(f'{vpn_status} | {disk_usedspace}/{disk_freespace} ({disk_usedpercentage}) 💾 | {linux_version} 🐧 | {battery_percentage}% - {uptime_formatted} {battery_icon} | {ip_addr} 💻 | {date_formatted} ⏲ |')


def get_command_output(command:str) -> str:
    return subprocess.check_output(command, shell=True, text=True).strip()


def parse_diskinfos(diskinfo: str) -> dict:
    titles, values = diskinfo.split('\n')


    titles = re.sub(' +', ' ', titles.strip().lower())
    values = re.sub(' +', ' ', values.strip())

    keys, values = titles.split(' '), values.split(' ')
    keys = keys[: -1]  # last key: 'mounted on' generate 2 keys. Removing last one

    data = dict(zip(keys, values))
    return data


if __name__ == "__main__":
    main()

