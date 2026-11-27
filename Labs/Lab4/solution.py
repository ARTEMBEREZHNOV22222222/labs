"""ЛБ4, варіант 3: N=18, [-30,30], insertion sort, матриця 4x4."""
import random
def insertion_sort(a):
    a=a.copy()
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key: a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a
def saddle_points(m):
    return [(i,j,v) for i,row in enumerate(m) for j,v in enumerate(row)
            if v==min(row) and all(v>=m[r][j] for r in range(len(m)))]
if __name__=="__main__":
    random.seed(3); a=[random.randint(-30,30) for _ in range(18)]
    replaced=[max(0,x) for x in a]
    print("Початковий:",a); print("Після заміни:",replaced); print("Insertion sort:",insertion_sort(replaced))
    m=[[random.randint(-9,20) for _ in range(4)] for _ in range(4)]
    print("Матриця:"); [print(row) for row in m]
    print("Симетрична відносно головної діагоналі:",m==[list(row) for row in zip(*m)])
    print("Сідлові точки (i,j,value):",saddle_points(m))
