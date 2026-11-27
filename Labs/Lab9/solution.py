"""ЛБ9, варіант 3: firewall appliance та користувацькі винятки."""
import ipaddress
class FirewallPolicyError(Exception): pass
class InvalidPortRangeError(FirewallPolicyError): pass
class SessionLimitExceededError(FirewallPolicyError): pass
def validate_firewall(ip,port_start,port_end,sessions):
    try: ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError as e: raise FirewallPolicyError(f"Некоректна IPv4: {ip}") from e
    if not (1<=port_start<=65535 and 1<=port_end<=65535 and port_start<=port_end):
        raise InvalidPortRangeError("Діапазон портів має бути 1..65535")
    if not 0<=sessions<=10000: raise SessionLimitExceededError("Ліміт сесій: 0..10000")
    return {"ip":ip,"ports":[port_start,port_end],"sessions":sessions,"valid":True}
if __name__=="__main__":
    print(validate_firewall("192.168.3.1",80,443,5000))
    for case in [("bad",80,443,1),("192.168.3.1",0,80,1),("192.168.3.1",80,443,10001)]:
        try: print(validate_firewall(*case))
        except FirewallPolicyError as e: print(type(e).__name__,e)
