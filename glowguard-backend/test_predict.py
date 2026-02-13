import requests
from pathlib import Path
import time

BASE = "http://127.0.0.1:8000"
# locate sample image in frontend assets
base_dir = Path(__file__).resolve().parent.parent
img_path = base_dir / "glowguard-frontend" / "src" / "assets" / "sample_image.jpg"
if not img_path.exists():
    print("ERROR: sample image not found at", img_path)
    raise SystemExit(1)

# temporary unique user
ts = int(time.time())
email = f"test{ts}@example.com"
username = f"testuser{ts}"
password = "Pass1234!"

# register (ignore if already exists)
reg = requests.post(f"{BASE}/api/auth/register", json={"email": email, "username": username, "password": password})
print('register:', reg.status_code, reg.text)

# login
login = requests.post(f"{BASE}/api/auth/login", json={"email": email, "password": password})
if login.status_code != 200:
    print('login failed:', login.status_code, login.text)
    raise SystemExit(1)

data = login.json()
token = data.get('access_token') or data.get('accessToken') or (data.get('detail') if isinstance(data, dict) else None)
if not token:
    # try nested
    token = data.get('access_token') if isinstance(data, dict) else None

if not token:
    print('Could not extract access token. Response:', data)
    raise SystemExit(1)

headers = {"Authorization": f"Bearer {token}"}
files = {"file": (img_path.name, open(img_path, "rb"), "image/jpeg")}

resp = requests.post(f"{BASE}/api/predictions/analyze", headers=headers, files=files)
print('analyze:', resp.status_code)
try:
    print(resp.json())
except Exception:
    print(resp.text)
