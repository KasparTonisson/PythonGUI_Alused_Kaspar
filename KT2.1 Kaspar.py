####################
#    Ülesanne 1    #
#       KT2       #
#  Kaspar Tõnisson #
#    10.03.2022    #
#      IT-21       #
####################

mehed = 0
naised = 0
sood = []

with open('palk.txt', 'r') as tootajad:
    for rida in tootajad:
        a = rida.split(" ")
        print(f'{a[0]:11}{a[1]:11}{a[2]:4}{a[3]:5}', end="")
        
        
print()
print()

with open('palk.txt','r') as f:
    contents = f.read()
    mehed = contents.count("M")
    naised = contents.count("N")
print("Meeste arv:", mehed)
print("Naiste arv:", naised)







 
        
