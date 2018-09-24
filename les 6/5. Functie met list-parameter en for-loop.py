grond=[4,5,3,-81]
def kwasom(grond):
    som = 0
    for i in grond:
        if i>0:
            som+=(i**2)
    return som
print(kwasom(grond))

