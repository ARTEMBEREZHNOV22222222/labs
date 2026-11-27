"""ЛБ11, варіант 3: StorageDrive/NVMeDrive та JBOD."""
class StorageDrive:
    def __init__(self,capacity_gb,wear_percent,power_on_hours):
        self.capacity_gb=capacity_gb; self.wear_percent=wear_percent; self.power_on_hours=power_on_hours; self._telemetry=[]
    @property
    def capacity_gb(self): return self.__capacity_gb
    @capacity_gb.setter
    def capacity_gb(self,v):
        if not isinstance(v,int) or v<=0: raise ValueError("capacity_gb має бути > 0")
        self.__capacity_gb=v
    @property
    def wear_percent(self): return self.__wear_percent
    @wear_percent.setter
    def wear_percent(self,v):
        if not 0<=v<=100: raise ValueError("wear_percent: 0..100")
        self.__wear_percent=float(v)
    @property
    def power_on_hours(self): return self.__hours
    @power_on_hours.setter
    def power_on_hours(self,v):
        if not isinstance(v,int) or v<0: raise ValueError("power_on_hours >= 0")
        self.__hours=v
    def add_telemetry(self,value): self._telemetry.append(float(value))
    def __len__(self): return len(self._telemetry)
    def __getitem__(self,index): return self._telemetry[index]
    def __eq__(self,o): return isinstance(o,StorageDrive) and (self.capacity_gb,self.power_on_hours)==(o.capacity_gb,o.power_on_hours)
    def __lt__(self,o):
        if not isinstance(o,StorageDrive): return NotImplemented
        return self.power_on_hours<o.power_on_hours
    def __add__(self,o):
        if not isinstance(o,StorageDrive): return NotImplemented
        return JBODVolume([self,o])
    def __str__(self): return f"StorageDrive({self.capacity_gb} GB, wear={self.wear_percent}%, hours={self.power_on_hours})"
    def __repr__(self): return f"StorageDrive({self.capacity_gb}, {self.wear_percent}, {self.power_on_hours})"
class NVMeDrive(StorageDrive):
    def __init__(self,capacity_gb,wear_percent,power_on_hours,pcie_lanes):
        super().__init__(capacity_gb,wear_percent,power_on_hours)
        if pcie_lanes not in (1,2,4,8,16): raise ValueError("PCIe lanes: 1,2,4,8,16")
        self.pcie_lanes=pcie_lanes
    def __str__(self): return f"NVMeDrive({self.capacity_gb} GB, PCIe x{self.pcie_lanes}, wear={self.wear_percent}%, hours={self.power_on_hours})"
class JBODVolume:
    def __init__(self,drives): self.drives=list(drives)
    @property
    def capacity_gb(self): return sum(d.capacity_gb for d in self.drives)
    def __len__(self): return len(self.drives)
    def __getitem__(self,i): return self.drives[i]
    def __str__(self): return f"JBOD: {len(self)} drives, {self.capacity_gb} GB total"
if __name__=="__main__":
    a=StorageDrive(1000,5,12000); b=NVMeDrive(2000,2.5,8000,4); a.add_telemetry(34.2); a.add_telemetry(35.1)
    print(a); print(b); print(a+b); print("a < b:",a<b); print("telemetry:",a[0],len(a))
