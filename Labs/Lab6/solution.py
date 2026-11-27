"""ЛБ6, варіант 3: мережеві комутатори L2/L3."""
from dataclasses import dataclass,field
@dataclass
class Switch:
    mac:str; model:str; vlans:set=field(default_factory=set); ports_count:int=24; ip:str="192.168.3.2"; stp_changes:int=0
    def audit_trunk(self,allowed,standard={1,10,20,30}):
        return {"missing":sorted(standard-allowed),"unexpected":sorted(allowed-standard),"allowed":sorted(allowed)}
class SwitchRegistry:
    def __init__(self): self.devices={}
    def add(self,s):
        if s.mac in self.devices: raise ValueError("MAC вже існує")
        self.devices[s.mac]=s
    def stp_counter(self,mac): return self.devices[mac].stp_changes
if __name__=="__main__":
    r=SwitchRegistry(); s=Switch("00:1A:2B:3C:4D:5E","Catalyst 2960",{1,10,20},24,"192.168.3.2",2); r.add(s)
    print(r.devices); print(s.audit_trunk({1,10,20,99})); print("STP:",r.stp_counter(s.mac))
