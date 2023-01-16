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
   - -sL: List IPs in block and Reverse-DNS
   - -sS: SYN scan
   - -sT and -sU : TCP  / UDP
   - -sV: Provides versions of the services
   - -A: Advanced and Aggressive = -sV -sC --traceroute
5. Nikto
   - -h: host option (works with IP, domaim, file) - e.g: ``` nikto -h 10.10.10.10 ```

6. Dirbuster
   - ``` dirb http://10.10.10.10 ```



### Weaponization
1. Create shell / reverse shell in backend language
   - Eg: [PHP shell](Shells\shell.php)
   - Eg: [PHP reverse shell](Reverse shells\reverse.php)
### Delivery
### Social Engineering
### Exploitation
1. Check permissions: sudo -l
### Persistence
### Defense Evasion
### Command & Control
### Pivoting
