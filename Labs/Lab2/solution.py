"""ЛБ2, варіант 3: математична модель та 16-бітний регістр живлення."""
import math
def model(x,y): return math.atan2(y,x)*math.exp(-0.1*x)+math.sinh(y)/(math.cosh(x)+1)
# [15] PWR_GOOD, [14..8] VOLT_MV, [7..3] TEMP_C, [2..0] STATUS
def pack_register(pwr_good,volt_mv,temp_c,status):
    if not 0<=volt_mv<=127: raise ValueError("VOLT_MV: 0..127")
    if not 0<=temp_c<=31: raise ValueError("TEMP_C: 0..31")
    if not 0<=status<=7: raise ValueError("STATUS: 0..7")
    return (int(bool(pwr_good))<<15)|(volt_mv<<8)|(temp_c<<3)|status
def unpack_register(word):
    if not 0<=word<=0xffff: raise ValueError("Очікується 16-бітне слово")
    return {"PWR_GOOD":bool((word>>15)&1),"VOLT_MV":(word>>8)&127,"TEMP_C":(word>>3)&31,"STATUS":word&7}
if __name__=="__main__":
    x,y=1.2,.5; word=pack_register(True,120,25,3)
    print(f"f({x},{y})={model(x,y):.8f}"); print(f"0x{word:04X}",unpack_register(word))
