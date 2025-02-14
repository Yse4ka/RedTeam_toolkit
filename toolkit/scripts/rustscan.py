import subprocess
from .ctpdf import convert_to_pdf
from .checksum import check
import multiprocessing
#import re


def rustscan_script(ip, user_name, function_name):
    #"--range", "1-10000"
    #p = subprocess.run(["rustscan", "-a", f"{ip}", "--accessible", "--ulimit", "15000"],
    #                   capture_output=True, encoding="utf-8")
    p = subprocess.run(["nmap", "-PS", f"{ip}"],
                       capture_output=True, encoding="utf-8")
    output = p.stdout.split('\n')[1:]

    #pre_output = ' , '.join(str(pre_output))
    #ansi_escape = re.compile(r'(?:\[\d?\;?\d+\w+)')
    #result = ansi_escape.sub('', pre_output)

    #pre_output = pre_output[0:-3]
    #delete_list = [
    #               "increasing ulimit",
    #               "lowering it",
    #               "the timeout",
    #               "Starting Nmap",
    #               "nmap","Nmap",
    #               "file","be run"
    #               ]
#
    #output = pre_output
    #for line in pre_output:
    #    for word in delete_list:
    #        if word in line:
    #            output.remove(line)
    #            break

    if check():
        ip = str(ip).split(',')[0]
        convert_to_pdf(output, user_name, ip, function_name)

    else:
        exit(1)


#user_name = "sarayloo"
#ip = "192.168.1.0/28"
#function_name = "livehost"
#rustscan_script(ip, user_name, function_name)