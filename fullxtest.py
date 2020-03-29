import os
import time
import sys

hostname=sys.argv[1]
run="-c run"

os.system("./recon-cli -w pentest -m recon/domains-hosts/hackertarget -c 'options set source {}' {}".format(hostname, run))
os.system("./recon-cli -w pentest -m recon/domains-hosts/brute_hosts -c 'options set source {}' {}".format(hostname, run))
os.system("./recon-cli -w pentest -m recon/domains-hosts/threatminer -c 'options set source {}' {}".format(hostname, run))
os.system("./recon-cli -w pentest -m recon/domains-hosts/certificate_transparency -c 'options set source {}' {}".format(hostname, run))
os.system("./recon-cli -w pentest -m recon/domains-contacts/whois_pocs -c 'options set source {}' {}".format(hostname, run))
os.system("./recon-cli -w pentest -m reporting/html -c 'options set customer fullXtest' -c 'options set creator 404TeamNotFound' {}".format(run))
os.system("./theHarvester.py -d {} -b ALL -f {}".format(hostname, hostname))
os.system("nmap -A --script vuln --reason {} -oX nmap.xml".format(hostname))
os.system("xsltproc nmap.xml -o nmap.html")
os.system("ls -la")

# fullXtest - passive/active recon + reporting
# created by 404TeamNotFound









