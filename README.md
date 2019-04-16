# Exploit dev
Show binary protections:  
```
$ rabin2 -I <binary>
$ checksec -f <binary>
```

List functions:  
```$ rabin2 -i <binary> ```

List functions written by the programmer (approx.):  
```$ rabin2 -qs <binary> | grep -ve imp -e ' 0 ' ```

Strings:  
```$ rabin2 -z <binary>```

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
