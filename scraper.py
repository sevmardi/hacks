import re
import sys
import errno
import socket
import requests
import argparse
import subprocess
from socket import error as socket_error
# Python tool to check for expired domains still allowed in
# crossdomain.xml files


parser = argparse.ArgumentParser()
parser.add_argument(
    "domain", help="Search the crossdomain.xml file on <domain> must fully-qualified")
parser.add_argument(
    "-v", "--verbose", help="Print information to the console during runtime", action="store_true")
parser.add_argument("-o", "--output", type=str, help="Write output to file")

args = parser.parse_args()

input_domain = args.domain
verbose = args.verbose

if args.output:
    f = open(args.output, "w")
    sys.stdout = f


if verbose:
    print("Searching crossdomain.xml on " +
          inputDomain + " for unregistered domains\n")
    print("=============================================================\n")


#Request the crossdomain file 
