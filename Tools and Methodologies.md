# Tools and Methodologies
## [Unified Kill Chain - IN](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf)
### Reconnaissance - [TA0043](https://attack.mitre.org/tactics/TA0043/)
#### Network Scanning
1. Arpscan
   - arp-scan -l: searches network throgh ARP protocol L2

2. Netdiscover
   - netdiscover -r Network IP

3. Nmap application - [Link](https://nmap.org/book/toc.html)
   - Start by stealth searches and move to more noisy
   - -sn: Shows hosts that are online WITHOUT port scanning
   - -sL: List IPs in block and Reverse-DNS
   - -sS: SYN scan it was more stealhy but it can be detected with good security
   - -sT and -sU : TCP  / UDP
   - -sV: Provides versions of the services
   - -A: Advanced and Aggressive = -sV -sC --traceroute
   - -p: Ports to be scanned. Usage -p 1,10 (1 and 10) 1-10 (1 to 10) -p- (all ports)
   - -T(1-5) 1 slow less detectable 5 faster more detectable
   
#### Web app scanning
1. Access web app and browse through as a normal user
2. Check page source code for potential file exploits and web app insights
3. Gobuster to search for directory structure
   - dir option for directory search
   - -u for URL
   - -w for wordlist

4. Nikto - may be blocked by good web security
   - -h: host option (works with IP, domaim, file) - e.g: ``` nikto -h 10.10.10.10 ```

6. Dirb
   - ``` dirb http://10.10.10.10 ```

7. Dirbuster
   Check this tool https://www.hackingarticles.in/comprehensive-guide-on-dirbuster-tool/

8. Gobuster
   Check this tool https://hackertarget.com/gobuster-tutorial/

#### Enumerating SMB (samba fileshare)
1. Use Metasploit to scan version -> useful to find potential exploits
2. Use smbclient to try to access (list SMB)
   ```smbclient -L \\\\IP\\```

#### Enumerating Processes in Linux
https://github.com/DominicBreuker/pspy

#### Identifying vulnerabilities
CVE information
https://www.cvedetails.com/
### Weaponization
1. Create shell / reverse shell in backend language
   - Eg: [PHP shell](Shells\shell.php)
   - Eg: [PHP reverse shell](Reverse shells\reverse.php)
2. Hashes
   - Unix known format
   - Windows LTNM format
   - [Typical hash types](https://hashcat.net/wiki/doku.php?id=example_hashes)
   - [Rainbow tables](https://crackstation.net/)
3. Shell cheat sheets
   https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
   https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
### Delivery
PHP reverse shells can be deployed via vulnerable upload buttons in web applications
### Social Engineering
### Exploitation
1. Check permissions: sudo -l
### Persistence
Obtain more users
### Defense Evasion
### Command & Control
### Pivoting
Privilege escalation
https://delinea.com/blog/linux-privilege-escalation
https://shauryasharma05.medium.com/privilege-escalation-through-insecure-configuration-db8ac03b324c
https://systemweakness.com/how-to-escalate-privileges-in-linux-privilege-escalation-techniques-70c92499ae45