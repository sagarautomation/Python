def maximumoftwonumber(x,y):
    if x > y:
        return x
    else:
        return y


maximumofTwo = maximumoftwonumber(3, 4)
print(maximumofTwo)


def maximumofthree(x, y, z):
    return maximumoftwonumber(x, maximumoftwonumber(y, z))


maximumofthree = maximumofthree(12, 9, 100)
print(maximumofthree)

def maximumoffour(x, y, z, a):
    return maximumoftwonumber(x, maximumofthree(y, z, a))

maximumofFour = maximumoffour(12, 9, 100, 1000)
print(maximumoffour)
