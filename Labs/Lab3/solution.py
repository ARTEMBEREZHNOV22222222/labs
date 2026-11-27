"""ЛБ3, варіант 3: табулювання кусочної функції та ряд cos(x)."""
import math
EPS=1e-7
def piecewise(x):
    if x<=0: return math.exp(-x*x)+2
    if x<3: return math.log(x*x+1)
    return 1/(x*x+1)
def cosine_series(x,eps=EPS):
    term=total=1.0; k=0
    while abs(term)>=eps:
        k+=1; term *= -x*x/(2*k*(2*k-1)); total+=term
        if k>10000: raise ArithmeticError("Ряд не збігається")
    return total,k
if __name__=="__main__":
    print(f"{'x':>6} {'f(x)':>12} {'series':>14} {'math.cos':>14} {'terms':>6}")
    for i in range(31):
        x=-1+i*.2; approx,n=cosine_series(x)
        print(f"{x:6.2f} {piecewise(x):12.7f} {approx:14.10f} {math.cos(x):14.10f} {n:6d}")
