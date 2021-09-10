ptf=[3.36,3.47,4.37,5.4,6.36,7.54,6.5,4.64,4.27,3.9]
ptg=[1.19,0.27,0.72,0.53,1.18,1.96,1.81,1.52,1.22,1.48]
x=1
contadorf=0
contadorg=0
def sum_fx():
    global contadorf
    for i in range(0,10):
        k=ptf[i]*x
        contadorf=contadorf+k
    print(contadorf)
def sum_gx():
    global contadorg
    for i in range(0,10):
        k=ptg[i]*x
        contadorg=contadorg+k
    print(contadorg)
def area():
    A=contadorf-contadorg
    print(A)
sum_fx()
sum_gx()
area()