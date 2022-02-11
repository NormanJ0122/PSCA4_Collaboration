bottles = 99
nextbottles = 98

while (bottles > 0):
    print(bottles, "Bottles of beer on the wall,", bottles, "bottles of beer. Take 1 down, pass it around,", nextbottles, "bottles of beer on the wall.")
    bottles = bottles - 1
    nextbottles = bottles - 1
print("No more bottles of beer!")
