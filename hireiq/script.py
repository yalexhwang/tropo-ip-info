import sys
import subprocess 
import csv
import re


# Function to extract IP addresses and print to STDOUT
def extract_addresses(data):
    # Regex pattern for IPv4
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}\b'
    # Find all matching IP addresses
    addresses = re.findall(pattern, data)
    # Print all matching IP addresses if availalbe
    if addresses:
        writer = csv.writer(sys.stdout, delimiter=' ', 
                            quoting=csv.QUOTE_NONE)
        for item in addresses:
            writer.writerow(['tropo,' + item])
    else:
        print 'No match found for IP address'

try:
    # Run a query to retrieve Tropo Server IP ranges
    result = subprocess.check_output(
        'nslookup -q=TXT _netblocks.tropo.com 8.8.8.8', shell=True)
    # Run the function to extract and print IP addresses
    extract_addresses(result)
except subprocess.CalledProcessError as e:
    # Get error detail
    output = e.output
    return_code = e.returncode
    print 'CalledProcessError output: \n' + output
    print 'CalledProcessError return_code: \n' + return_code

