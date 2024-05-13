# tailwindcss-deobfuscater

![image](https://github.com/reedjones/tailwindcss-deobfuscater/assets/4346136/6b2740df-33d9-4ab6-9ae8-10badd383dac)



```plaintext
O  OO                                                                                                                                                                                                         
O  OO                                                                                            oo o o  o oo                                                                                                 
 OOOO                                                                                       O  OOo           oo  o                                                                                            
 OOOOO  Oooo                                                                           OO   OOOOOO                 o                                                                                          
    O   Oo   o             OO   O  O          OO   O                        O  OOOOOoo        OOOO                   o                                                                                        
  OOOOO O     o o       OOOOOOOO OO  OooOOOOO O O  OOO  OOOOOOO O OO O O    OOO oo O  Oo   O  OOOO                    o o   O                            O                                                    
 OOOO   Oo       o o oOO  O OOOOOOOOOo  OOO   OOoOO oOO OoOOo O  O OOOOO   OOO  o    O  oO O   O O                       o OO oooo        ooo         oo  O                                                   
  O OO  O             Oo o  o OOOO       o OO  Oo   O      OOO OOOOOOoo Oo OOOO o        oOOOOOOOO                        oOO o   oo  OO oo ooo       o o O                                                   
 O OOO OOo             O O  O O          oOOOOOOo             o  Oo  O   OOOOO Oo         oO  oO O                         OO o     o OOo      oo  O oo  oO                                                   
   OOOO Oo                                OOO OOo              oO o          Oo o          OOOoOOO                         OOoo      oO o        o OO    o  O                                                 
  OOOO   O                               OOOOOOO                OOo           o            oO OOOO                         OOo        Ooo         oO      oOO                                                 
  O OOOO Oo                               OOO o    o    oo       o              o           O OO                               o      Ooo          o       o O                                                
  O O OO OO                                OO       o   o         o            oo           o O                                 o     O oo           o      o O                                               
      OO  Oo                                oo        o           oo           o            ooO                                  o       o           o      Oo                                                
       OO OOo                                 o      o            oo           oo            o                                    o       o            o      O                                               
        O  OOOOoOOOOOOOOOo o  ooo              o    o  o o        o o  oooo oooo            oo                                   o         o           o     Oo O                                             
       OO OO OOOOOO OOOOOO     ooo o o   o      oooo     o          ooo o  o     o                               o oo oo  o   o      o      o          o       o                                              
       OO OOOO  O OOOOOOOO      o  OO o o oo  o oo        oo                  o  o           o                                o      o      o          o        O                                             
        O     O  OOO OOOO       oo OOO  O o                 o        o            oo          o                                  oo  o       o         o       OoO                                            
                 OOO  OOO        oo OOO O o                          o             oo        o                                     o  o      o        oo         O                                            
                OOOOOOO o          o OO OOo                           o            o o        ooo        oo o             o        o  oo      o       o          OO                                           
                 OO O OOo           ooO OOo                o          o           oo o          oo       oo o  o  o               o            o     o           Oo                                           
                 O O OOOo            oo OO o               oo          o             o         o      oo      oOOO O o o O oo o ooo             o ooooo            O                                          
                O OO  OOo             oo O o                o                         o        o      o  o      OOOO OO  O O                     o     o            O                                         
                 OOOO O o               O oo                o           o              o        o   o      oo     OOOOO OOO                       o     oo          Oooo  o        oo                         
                 OOOOOO o                Ooo                            o                       o            oo    O o OOOOO            o                 o                 o  o o oooo                       
                 OOOOOO o                O oo               oo           o              o        oo            o   OO  OOOOOo           o                  o                                                  
                 OOOOOO o                O  oo               o                          o        oo                     OO Oo           oo          o       o                           o                     
                  OOOOOOo                    o               oo           o              o       oo             o       OO                                   oo                                               
             OO   OO OOOo                     oo             oo            o             o                      o       O  o             o           o                                    o                   
                  OO OOOO                      oo             oo                                                 o           o            o                    o                           o                  
               O    OOOOOOO                     o             oo           o              o                                                           o         o                            o                
                      OOO O                     o             oo         o o              o                       o            o           o                     o                                            
               O  OO  OOOOOO                   oo             o o        o o              o                                                             o                                     o               
                   OO   OO O                    o             oOOO       o                o             @@         o             o           o                     o                           o              
                   OO   OOOOO                   o             OOOOO       oo              o   @@@@@@@@@@@@@@@@@@                  o o                    o                                      o             
                O     OOOOOO                    oo            OOOOOOO     oo             @o@@@@@@ @@@@@@@@@@@@@@   o                oo       o                      o                                         
                  O O    OOOOO    OO       O   o OO           oOOOOOOoo   o oo         @ @o@x@@@@@@x@x@@@x@@@x@@@@@ o               o         o          o           o                          o             
                  O    OO OOOOO    O       OO oo OOo          oO O OOOOooOOOO oOO    @ @oxox                  xxx@ oo                oo        o         oo       o   o                          o            
                  O      OOOOOO   O        O oOOOOOOOo  OO─── OOOOOO OO  OOOOO O Oo o@ooxx                        x@@@               o o        o        o o       o  o                                       
                  O      O  OOOOO o         o   OO OO ooOOOOOOoO OO   OOO O OOOOOOO oox                            x @                  o        o                 o  o                           o           
                  O          OOOOOOOOOO OO O     OO  O OO OO O OO OO OOO     O O O @xx                              x@@               o          Oo  O OOoO O       o o                             o         
                            OOOO       O  O O     O    OO      OO   OO   O O  OOOOO@x                               oo@@              oOOO      oOOoo O  O  o        ooo                            o         
                             OOOO  O  OO   OO       OOO         O      O  OOO  O OOOx                                 o@              oOOOo     o  OOO O o  OO   OO OO  oOOOOOo oOOO O OoOOOo O      o        
                              O O  O   O                                OO O   O OO x                                 x@              oOOOOOO     OOOOoOOOO OOO      oOO OOOOOOOO OO  OO  O OOOOO O ooo       
                               OO                             o  o o o  OOoO      OO@xxx       xxx@xxxx             xxx@o O           oO  OO    o  OO O  OO O Oo      OOOOOOO  OOOO OOOOOOOOO  O              
                                                                         O     o  xOx@oo       xxx@@xxx  xx  xxxxxxx  x@@OOo           O OOO oOOO  OO O OOOOOOOOoO  o O OOO OO OOO    OO O O   OOO  OO        
                                                                                  xx@xxxx xxxx xxxx@@xx                x@OOOo        O OOO OO OoOO    O OOO OOOOOoOoO O  OO OO O   O               O          
                                    o o   o   o   o  oo o  o o@@o  o o o oo       xxxxxx       xxxxxxxx                xOOOOOoO  O  oo     O OO  OO  OO O  O   O    OOOOOOO   O    O  OO                      
                                                               @@@          oo oo oo x           x                 ooo @OOOOOooo ooOO     o   Oo  O o  o                    O     OO  O                       
                                                                  @@ @               x                                 @OO O OOOOOOOO                        o   o  o   o o  o   o   o o  o  o o   o o  oo    
                                              @@@@@@                 @@@            xx     x                          O@OO                                                                                o oo
                                               @@@@@@@                 @@           x      xx   x                    OOO                                                                                      
                                                @@ @@@@@                @@          x      xx   x                     @ O                                                                                     
                                                @    @ @@                 @         xx     xxxxxx                    @@                                                                                       
                                                @  @   @ @ @ @            @@@ @ @@@@ xxxxxx                        xx@@                                                                                       
                                                @@   @   @ @@  @@           @  @    @ @ x     @@@@x@@@           @@x@@@                                                                                       
                                                @@      @  @  @ @             @@ @     @@@x@x@@@@@@@@@@        x@@@ @@@                                                                                       
                                                @@         @ @@ @@            @@@@  @@@@@@@@@@@@xxx@@@xxx xxxx@@@@@@ @@@                                                                                      
                                                @@            @@@@@            @ @@  @@@@ @   @@@@@@@xxxxxx@@@@@@ @  @@@@                                                                                     
                                                @@              @@@@           @@  @   @@@  @@@@@@@@@@@@@@@@@@@@      @  @@                                                                                   
                                                @                @@@@           @  @@@@@  @@@@@@@ @@@ @ @@             @ @ @                                                                                  
                                               @ @        @@@    @@ @             @  @@@@@@@@@@@ @@                      @ @@                                                                                 
                                               @ @         @   @  @ @              @@@ @@@@ @ @                            @@                                                                                 
                                               @ @           @    @              @ @@@@@@@@                                @@@                                                                                
                                               @ @             @ @@@          @ @@@ @@@  @                                  @@                                                                                
                                               @@ @     @@@@      @@ @       @@@@@ @@  @@      @@                           @ @                                                                               
                                              @@@@@@@@@@ @@@@ @  @@     @   @@@@@@            @@                             @ @                                                                              
                                               @@ @ @ @@ @  @ @@ @@@@@  @ @@ @@@   @         @@            @@                @@                                                                               
                                                 @@  @      @@@@@@@@@ @@@ @@@@@@@ @@@@@@@@@@@@    @  @  @     @@              @@@                                                                             
                                                 @@   @      @@ @@@@@ @ @@@ @  @            @@ @              @@            @@@@@                                                                             
                                                 @@@@@ @ @ @     @@@@  @@@@@@@@@@@                         @@ @               @@@ @                                                                           
                                                     @@@       @  @@    @@@@@@@@@@@@@@  @             @@@@   @                 @@@                                                                            
                                                       @@@@@@@@@@@@@@ @@@  @    @@@   @ @ @@ @@@ @@@@@ @ @ @@@       @@        @@@  @@@                                                                       
                                                   @@  @@   @@@@ @@@ @@  @@       @@@                                 @     @@@@ @@@@@ @                                                                      
                                                             @@@ @@@@@  @@   @  @    @@@@@ @                              @@ @@ @ @@@@@@ @ @@@                                                                
                                                              @  @@@@ @ @@@@   @  @ @@   @  @@                          @  @@@ @ @@@@@@@@@@ @@@@                                                              
                                                              @@ @@@  @      @                                            @  @@@  @@@ @@@ @@@@ @@                                                             
                                                                  @@@@@@@@ @@@@ @@@@  @ @@@                                 @   @@  @@@@@@@@@@@  @@@@                                                         
                                                                         @      @        @    @@                                 @@@@  @@@@ @@@@    @@@@  @  @@                                               
                                                                                                                        @           @@@ @ @@@ @@@@  @@  @  @ @@                                               
                                                                                                                          @            @@@ @@@@  @@ @@@                                                       
                                                             Give me your css please??                                      @             @@@  @@@ @@                                                         
                                                                                                                             @              @@@ @@@@ @                                                        
                                                                                                                                               @@@ @@@                                                        
                                                                                                                                                  @@@@@@                                                      
                                                                                                                                                        @@                                                    
                                                                                                                                                          @@@                                                 
                                                                                                                                                             @@@                                              
                                                                                                                                                                @@                                            
                                                                                                                                                                  @@@                                         


```
