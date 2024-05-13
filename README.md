# tailwindcss-deobfuscater

<img src="https://github.com/reedjones/tailwindcss-deobfuscater/assets/4346136/6b2740df-33d9-4ab6-9ae8-10badd383dac" data-canonical-src="https://github.com/reedjones/tailwindcss-deobfuscater/assets/4346136/6b2740df-33d9-4ab6-9ae8-10badd383dac" width="250" height="250" />

Reverse engineer obfuscated TailwindCSS to get the original class names.


```plaintext
                                                                                 FailWind LOL v0.1                                           
                          xxxxxx                                 x                                                                          
                  xx x   xxxxxxxxx                  xx           xx                   x                                                     
                         xxxx  xxx                   xx            xx                 xx                                                    
            xx x x x  xxx xxx          xx  xx         xx        xx  xx                 xx                                                   
         xx x xxxx      xxxxxxxxxx     xx   xx         xx        xx       x              x                                                  
                            xx              xxx         xx   xxx  xx  xx  xxxxxxxx    xxxxxx                                                
                             xx  xxxxx  xxx  xxx  xxxx   xx  xxx   xx  xx  xxxx xxx  xxxxxxxx     xxxxxx                                    
                 x         xx xx x  xx   xx   xxx         xx  xxx   xx  xx  xx    xx  xx xxxxx xxxx  xxx xxx x    x      x                  
x                xxx      xxxxxx xx xxxx xxx   xxxxxxxxxx xxx xxxx  xxx  xx  xx   xxx xx  xx xx xxx      xxxx xxxxxx     x                  
xxx              x  xxxxxxxx xx  xxxx  xx xxx  xxxxxxxxxxx xxxx   xxx x   xx  xx   xxxxxxxxx xxxxxxxxxxxx    xxxx xxxxxxx   x  xx           
  x xxx x xx xxxxx                                                                          xx             xxx x  x  x  xxxxxxx             
                              xx              x                                         xxx    xx x x x xxxxxxxxxx   xx       xx            
                             x  x             xxx  x  xx xxx           xxx     xx x  x     xx xxxx  x x   x  x   xxxx  xxx xxx  xxxx        
               x          x       x x x  x  x                x x  xx x    xxxx    x         x x  x  x x xx x x xx x xxx   xxx       xxx     
                x  x   x                             xx                      xxx     x   x    x x  x       x x     xxxx xx  x xxx         xx
                                                        x x  x    x    x   x     x                 xxx x x     x x x xx         x x xx xx x 
               Tailwind-CSS de-obfuscation tool                                    x  x x  x  x  x                                          
                                                                                                                                            
               Reed Jones 2024                                                                                                              
```
```plaintext
Usage: deobfuscator.py [OPTIONS]

Options:
  -o, --obfuscated-file TEXT  Path to the obfuscated CSS file  [required]
  -r, --original-file TEXT    Path to the original CSS file  [required]
  -out, --output-file TEXT    Path to the output file for deobfuscated CSS
  --help                      Show this message and exit.
```
