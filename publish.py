#!/usr/bin/env python3
"""Adds an Android build to the update feed.
  publish.py <apk> <versionCode> <version> [--force] [--min N] [--notes TEXT]
"""
import argparse, hashlib, json, os, shutil
BASE = "https://raw.githubusercontent.com/moraxdev/Sahra-Manverse-Releases/main/"
a = argparse.ArgumentParser()
a.add_argument("file"); a.add_argument("code", type=int); a.add_argument("version")
a.add_argument("--force", action="store_true"); a.add_argument("--min", type=int, default=0); a.add_argument("--notes", default="")
o = a.parse_args()
data = open(o.file, "rb").read()
name = f"android/sahra-manverse-{o.version}.apk"
os.makedirs("android", exist_ok=True)
for old in os.listdir("android"): os.remove(os.path.join("android", old))
shutil.copyfile(o.file, name)
feed = json.load(open("update.json")) if os.path.exists("update.json") else {}
feed["android"] = {"version": o.version, "url": BASE + name, "notes": o.notes, "force": o.force,
                   "code": o.code, "minCode": o.min, "sha256": hashlib.sha256(data).hexdigest()}
json.dump(feed, open("update.json", "w"), indent=2, ensure_ascii=False)
print("Published", name)
