# Tools and Methodologies
## Unified Kill Chain
### IN
#### Reconnaissance - [TA0043](https://attack.mitre.org/tactics/TA0043/)
##### Web app
1. Access web app and browse through as a normal user
2.  Check page source code for potential file exploits and web app insights
3. Gobuster to search for directory structure
   - dir option for directory search
   - -u for URL
   - -w for wordlist
4. Nmap application - Active
   - Start by stealth searches -sS
   - -sT and -sU : TCP  / UDP

#### Weaponization
#### Delivery
#### Social Engineering
#### Exploitation
#### Persistence
#### Defense Evasion
#### Command & Control
#### Pivoting
