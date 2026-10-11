
from pathlib import Path
from datetime import datetime

folder = Path("data")
if not folder.exists():
    print("Error: data folder not found.")
    exit()



for item in folder.iterdir():
    if not item.is_file():
        continue

    modified_time = datetime.fromtimestamp(item.stat().st_mtime)

    age = datetime.now() - modified_time
    age_in_days = age.days

    if age_in_days >= 30:
        status = "OLD"
    else:
        status = "RECENT"

    print("Name:", item.name)
    print("Size:", item.stat().st_size, "bytes")
    print("Type:", item.suffix)
    print("Modified:", modified_time)
    print("Age:", age_in_days, "days")
    print("Status:", status)
    print()
