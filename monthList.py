month = ["January","February","March","April","May","June","July","August" +
          "September","October","November","December"]
greeting = ["Happy New Year!","Happy Valentines Day!","March Madness!","April Fools!","May the 4th be with you!","Can't think of anything for June!","Happy Freedom Day!","Happy Independence Day!","Have a great Labor Day!","Halloween!!!","Happy Thanksgiving!","Christmas is almost here!"]

monthNumber = 1
listIndex = 0

for l in month:
    print(" Month",monthNumber,"is ",month[listIndex],"...",greeting[listIndex])
    monthNumber+=1
    listIndex+=1
print("\n","Program Complete")
