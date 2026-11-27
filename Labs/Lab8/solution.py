"""ЛБ8, варіант 3: perm_checker --path <dir> --mask <octal_mode>."""
import argparse,stat
from pathlib import Path
def audit(root,mask):
    found=[]
    for p in root.rglob("*"):
        try:
            if p.is_symlink() or not p.is_file(): continue
            mode=stat.S_IMODE(p.stat().st_mode)
            if mode & mask and (mode & 0o022 or mode in (0o666,0o777)):
                found.append((p,mode))
        except OSError as e: found.append((p,str(e)))
    return found
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--path",required=True,type=Path); ap.add_argument("--mask",required=True,type=lambda s:int(s,8))
    a=ap.parse_args()
    if not a.path.is_dir(): ap.error("--path має бути каталогом")
    results=audit(a.path,a.mask)
    for p,m in results: print(f"{p}: {oct(m) if isinstance(m,int) else m}")
    print("Знайдено:",len(results))
if __name__=="__main__":main()
