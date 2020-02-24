print("fa")
def fa(p,q,r):
    return  p and  (p or q)
tv = [True, False]
for p in tv:
    for q in tv:
        for r in tv:
            print(p, q, r, fa(p,q,r))
print("fb")
def fb(p,q,r):
    return  (p and q) or (p and r)
for p in tv:
    for q in tv:
        for r in tv:
            print(p, q, r, fb(p,q,r))
print("f1")
def f1(p,q,r):
    return  p or  (q or r)
for p in tv:
    for q in tv:
        for r in tv:
            print(p, q, r, f1(p,q,r))
print("f2")
def f2(p,q,r):
    return  (p or q) or r
for p in tv:
    for q in tv:
        for r in tv:
            print(p, q, r, f2(p,q,r))

def compare(f,g):
    tv = [True,False]
    # Initialize empty lists xl and yl
    xl = []
    yl = []
    count = 0
    # Loop through possible values of p, q and r
    for p in tv:
        for q in tv:
            for r in tv:
                x = f(p,q,r)
                y = g(p,q,r)
                #incraments count
                count+=1
                # Append truth values for current p, q, r values
                xl.append(x)
                yl.append(y)

    # Determine conclusion
    i=0
    while( i < count ):
        if xl[i] == yl[i]:
            conclusion = "Yes - Equivalent"
            i+= 1
        else:
            conclusion = "No - Not Equivalent"
            break
    return conclusion
# compares a false expration the two examples above
print("fa, fb: " +compare(fa, fb))

# compares a true expration
print("f1, f2: " + compare(f1,f2))

