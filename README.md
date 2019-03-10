# PDF files
## Tools
https://blog.didierstevens.com/programs/pdf-tools/

## Crack
Download Bleeding John (https://github.com/magnumripper/JohnTheRipper). Use pdf2john.pl.
```Kali
perl pdf2john.pl file.pdf > pdf-hash.txt
john --wordlist=/w/rockyou.txt pdf-hash.txt
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
fcrackzip -u -D -p '/w/rockyou.txt' -v file.zip
```
