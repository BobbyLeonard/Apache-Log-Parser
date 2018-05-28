# Apache-Log-Parser
Script to help with server security management. This script returns a list of CIDR blocks relating to Ip's which have made some connection with Apache server over the last 2 days. 99% of this traffic is unwanted (port scans, sqlmap attempts etc.)
Because only 3, maybe 4 different networks ever have a legitimate reason to have a connection with my server,
my solution is to ban anyone else who attempts to connect.
I do this by running PSAD (https://github.com/mrash/psad) and passing the output of this script to PSAD's blocking file (auto_dl)
