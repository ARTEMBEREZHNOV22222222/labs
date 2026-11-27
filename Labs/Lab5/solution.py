"""ЛБ5, варіант 3: конфігурація інтерфейсу комутатора Cisco."""
import ipaddress
from dataclasses import dataclass
@dataclass
class SwitchInterface:
    interface:str; ip_address:str; cidr:int; admin_status:str; duplex:str; speed_mbps:int
    def validate(self):
        ipaddress.IPv4Address(self.ip_address)
        if not 0<=self.cidr<=32: raise ValueError("CIDR повинен бути 0..32")
        if self.admin_status not in {"up","down"}: raise ValueError("Статус: up/down")
        if self.duplex.lower() not in {"full","half"}: raise ValueError("Duplex: Full/Half")
        if self.speed_mbps not in {10,100,1000,2500,5000,10000}: raise ValueError("Невідома швидкість")
    def render(self):
        self.validate()
        mask=ipaddress.IPv4Network(f"0.0.0.0/{self.cidr}").netmask
        return f"interface {self.interface}\n ip address {self.ip_address} {mask}\n {'no shutdown' if self.admin_status=='up' else 'shutdown'}\n duplex {self.duplex.lower()}\n speed {self.speed_mbps}\n"
if __name__=="__main__": print(SwitchInterface("GigabitEthernet0/1","192.168.3.1",24,"up","Full",1000).render())
