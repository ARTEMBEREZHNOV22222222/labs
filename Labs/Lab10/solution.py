"""ЛБ10, варіант 3: traffic.csv, сигнатура PKTS, JSON-звіт."""
import csv,json
from collections import defaultdict
from pathlib import Path
MAGIC=b"PKTS"
def analyze_csv(src,out):
    totals=defaultdict(int); filtered=[]
    with src.open(newline="",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        if not {"IP","Bytes","Drop"}.issubset(reader.fieldnames or []): raise ValueError("Потрібні колонки IP, Bytes, Drop")
        for row in reader:
            totals[row["IP"]]+=int(row["Bytes"])
            if int(row["Drop"])>0: filtered.append(row)
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["IP","Bytes","Drop"]); w.writeheader(); w.writerows(filtered)
    return dict(totals),len(filtered)
def audit_binary(path):
    with path.open("rb") as f:
        signature=f.read(4)
        if signature!=MAGIC: raise ValueError(f"Очікується {MAGIC!r}, отримано {signature!r}")
        f.seek(4); payload=f.read(); size=f.tell()
    return {"signature":signature.decode("ascii"),"payload_bytes":len(payload),"file_size":size}
def main():
    folder=Path(__file__).parent
    totals,count=analyze_csv(folder/"traffic.csv",folder/"traffic_dropped.csv")
    binary=audit_binary(folder/"traffic_sample.bin")
    report={"variant":3,"bytes_by_ip":totals,"rows_with_drop":count,"binary_audit":binary}
    (folder/"station_snapshot.json").write_text(json.dumps(report,ensure_ascii=False,indent=4),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=4))
if __name__=="__main__":main()
