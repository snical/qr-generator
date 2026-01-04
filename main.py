import qrcode
from pathlib import Path

codes_dir = Path("codes")
codes_dir.mkdir(exist_ok=True)

url = input("URL: ").strip()
name = input("QR name: ").strip().replace(" ", "_")

if not url or not name:
    raise SystemExit("URL and name are required.")

file_path = codes_dir / f"{name}.png"
qrcode.make(url).save(file_path)

print(f"Saved: {file_path}")
