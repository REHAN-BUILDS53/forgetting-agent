from pathlib import Path
from datetime import datetime

folder = Path("data")

for item in folder.iterdir():
    modified_time = datetime.fromtimestamp(item.stat().st_mtime)

    print("Name:", item.name)
    print("Size:", item.stat().st_size, "bytes")
    print("Type:", item.suffix)
    print("Modified:", modified_time)
    print()