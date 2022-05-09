#!/usr/bin/env python3

# Generates `file.json`, which is an array
# of the names of the files in `/data`.

import os
import json

files = []
for walk in sorted(os.walk("data")):
    if len([char for char in walk[0] if char == "/"]) == 2:
        _, grp_name, k = walk[0].split("/")
        ntubes = walk[2][0][walk[2][0].index("_")+1:-5]
        files.append(f"--{grp_name}-{ntubes}--")
        for file in sorted(walk[2], key=lambda f: int(f[:f.index("c")])):
            files.append(f"{grp_name}/{k}/{file[:-5]}")

with open("files.json", "w") as f:
    json.dump(files, f, indent=4)
