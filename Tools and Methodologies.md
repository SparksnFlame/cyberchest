# Tools and Methodologies
## [Unified Kill Chain - IN](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf)
### Reconnaissance - [TA0043](https://attack.mitre.org/tactics/TA0043/)
#### Web app
1. Access web app and browse through as a normal user
2.  Check page source code for potential file exploits and web app insights
3. Gobuster to search for directory structure
   - dir option for directory search
   - -u for URL
   - -w for wordlist
4. Nmap application - [Link](https://nmap.org/book/toc.html)
   - Start by stealth searches and move to more noisy
   - -sn: Shows hosts that are online WITHOUT port scanning
   - -sL: List IPs in block and Reverse-DNS
   - -sS: SYN scan it was more stealhy but it can be detected with good security
   - -sT and -sU : TCP  / UDP
   - -sV: Provides versions of the services
   - -A: Advanced and Aggressive = -sV -sC --traceroute
   - -p: Ports to be scanned. Usage -p 1,10 (1 and 10) 1-10 (1 to 10) -p- (all ports)
   - -T(1-5) 1 slow less detectable 5 faster more detectable
5. Nikto
   - -h: host option (works with IP, domaim, file) - e.g: ``` nikto -h 10.10.10.10 ```

6. Dirbuster
   - ``` dirb http://10.10.10.10 ```

7. Arpscan
   - arpscan -l: searches network throgh ARP protocol L2

8. Netdiscover
   - netdiscover -r Network IP



### Weaponization
1. Create shell / reverse shell in backend language
   - Eg: [PHP shell](Shells\shell.php)
   - Eg: [PHP reverse shell](Reverse shells\reverse.php)
2. Hashes
   - Unix known format
   - Windows LTNM format
   - [Typical hash types](https://hashcat.net/wiki/doku.php?id=example_hashes)
   - [Rainbow tables](https://crackstation.net/)
### Delivery
### Social Engineering
### Exploitation
1. Check permissions: sudo -l
### Persistence
### Defense Evasion
### Command & Control
### Pivoting
