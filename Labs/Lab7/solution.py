"""ЛБ7, варіант 3: kwargs, сортування дисків та визначник."""
def disk_config(**kw):
    required={"name","iops","latency_ms","capacity_gb"}
    if required-kw.keys(): raise ValueError(f"Потрібні поля: {sorted(required-kw.keys())}")
    if kw["iops"]<0 or kw["latency_ms"]<0 or kw["capacity_gb"]<=0: raise ValueError("Некоректні параметри")
    return dict(kw)
def sort_disks(items): return sorted(items,key=lambda d:(-d["iops"],d["latency_ms"]))
def determinant(a):
    n=len(a)
    if n==0 or any(len(row)!=n for row in a): raise ValueError("Матриця має бути квадратною")
    if n==1:return a[0][0]
    if n==2:return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return sum((-1)**j*a[0][j]*determinant([row[:j]+row[j+1:] for row in a[1:]]) for j in range(n))
if __name__=="__main__":
    d=[disk_config(name="SSD-A",iops=90000,latency_ms=.08,capacity_gb=1000),disk_config(name="SSD-B",iops=120000,latency_ms=.12,capacity_gb=2000),disk_config(name="NVMe-C",iops=120000,latency_ms=.06,capacity_gb=500)]
    print(sort_disks(d)); print("det(A) =",determinant([[2,1,3],[1,0,2],[4,1,8]]))
