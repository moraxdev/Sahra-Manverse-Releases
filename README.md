# Sahra Manverse releases

Public update feed for Sahra Manverse. `update.json` tells the installed app about the current
build. This repository holds built files only; there is no source code or account data here.
Android builds are verified by the app signing key and the SHA-256 in `update.json`.

Publish a build with `python3 publish.py <apk> <versionCode> <version> --notes "..."`, then commit and push.
