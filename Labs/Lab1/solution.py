"""ЛБ1, варіант 3: діагностика шляхів пошуку Python."""
import json, sys
from pathlib import Path
def diagnose():
    paths=[str(Path(p).resolve()) for p in sys.path]
    prefix=str(Path(sys.prefix).resolve()); base=str(Path(sys.base_prefix).resolve())
    return {"python_version":sys.version,"sys_path":paths,"sys_prefix":prefix,"sys_base_prefix":base,
            "virtual_environment_active":prefix!=base,"path_entries_exist":[Path(p).exists() for p in paths]}
if __name__=="__main__":
    data=diagnose(); print(json.dumps(data,ensure_ascii=False,indent=4))
    Path("path_diagnostics.json").write_text(json.dumps(data,ensure_ascii=False,indent=4),encoding="utf-8")
