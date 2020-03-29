### fullXtest - python code to run passive/active reconnaisance on a single target and compile results into reports ###
### by 404TeamNotFound ###

import os
import time
import sys
hostname=sys.argv[0] #set variable from cli argument
run="'-c run'" #set variable to run the recon-ng exploit
os.system("./recon-cli -w pentest -m recon/domains-hosts/hackertarget -c 'options set source "
            "{} {}'".format(hostname, run))
time.sleep(15)
os.system("./recon-cli -w pentest -m recon/domains-hosts/brute_hosts -c 'options set source "
            "{} {}'".format(hostname, run))
time.sleep(15)
os.system("./recon-cli -w pentest -m recon/domains-hosts/threatminer -c 'options set source "
            "{} {}'".format(hostname, run))
time.sleep(15)
os.system("./recon-cli -w pentest -m recon/domains-hosts/certificate_transparency -c 'options set source "
            "{} {}'".format(hostname, run))
time.sleep(15)
os.system("./recon-cli -w pentest -m recon/domains-contacts/whois_pocs -c 'options set source "
            "{} {}'".format(hostname, run))
time.sleep(15)
os.system("./recon-cli -w pentest -m reporting/html -c 'options set customer fullXtest' -c 'options set creator "
          "404TeamNotFound' {}'".format(run))
time.sleep(15)
os.system("'./theHarvester.py -d $hostname -b ALL -f {}'".format(hostname))
time.sleep(15)
os.system("'nmap -A --script vuln --reason $hostname -oX nmap.xml'")
time.sleep(90)
os.system("'xsltproc nmap.xml -o nmap.html'")
os.system(15)
os.system('ls -la')
