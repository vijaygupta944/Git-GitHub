count = 0

def fun(count):
    if count == 6:
        return
    
    print(count)
    count+=1

    fun(count)

