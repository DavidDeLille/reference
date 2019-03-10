# PDF files
## Tools
https://blog.didierstevens.com/programs/pdf-tools/

## crack
Download Bleeding John (https://github.com/magnumripper/JohnTheRipper). Use pdf2john.pl.
```Kali
perl pdf2john.pl file.pdf > pdf-hash.txt
john --wordlist=/w/rockyou.txt pdf-hash.txt
```

# ZIP files
## crack
```Kali
fcrackzip -u -D -p '/w/rockyou.txt' -v file.zip
```
