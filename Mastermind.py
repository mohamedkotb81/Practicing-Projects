import random
num = random.randint(1001, 9999)
nums = list(str(num))
values = ["X", "X", "X", "X"]
tries= 0
while values != nums:
    v = input("select number of 4 digits: ")
    z = list(str(v))


    if nums[0] == z[0]:
        values[0]=z[0]
    else:
        pass

    if nums[1] == z[1]:
        values[1]=z[1]
    else:
        pass
    if nums[2] == z[2]:
        values[2]=z[2]
    else:
        pass
    if nums[3] == z[3]:
        values[3]=z[3]
    else:
        pass

    x = " ".join(values)
    print(x)
    tries +=1
    if values == nums:
        if tries <= 9:
            print(f"WOW, you got it in {tries}, you have a MasterMind :)")
        elif 10 <= tries <= 15:
                    print(f"OH, you got it in {tries}, you have a ValuableMind :)")
        else:
                    print(f"OH, you got it in {tries}, please take more trains :)")

        exit()
    else:
        pass
     
     






