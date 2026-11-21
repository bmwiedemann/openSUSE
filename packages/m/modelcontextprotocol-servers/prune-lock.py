#!/usr/bin/python3
# Reduce upstream's package-lock.json to the packaged workspaces plus their
# type declarations, mirroring prune-workspace.mjs.
import json
import sys

WS = ["src/everything", "src/filesystem", "src/memory", "src/sequentialthinking"]
lock = json.load(open(sys.argv[1]))
pk = lock["packages"]
out = {}

root = dict(pk[""])
root["workspaces"] = WS
root.pop("dependencies", None)
root.pop("devDependencies", None)
out[""] = root

for ws in WS:
    e = dict(pk[ws])
    e["devDependencies"] = {k: v for k, v in e["devDependencies"].items() if k.startswith("@types/")}
    out[ws] = e
    out["node_modules/" + e["name"]] = pk["node_modules/" + e["name"]]


def resolve(frm, name):
    base = frm
    while True:
        cand = (base + "/node_modules/" if base else "node_modules/") + name
        if cand in pk:
            return cand
        if not base:
            raise SystemExit("unresolved " + name + " from " + frm)
        idx = base.rfind("/node_modules/")
        base = base[:idx] if idx >= 0 else ""


todo = []
for ws in WS:
    e = out[ws]
    for d in list(e.get("dependencies", {})) + list(e["devDependencies"]):
        todo.append(resolve(ws, d))
while todo:
    k = todo.pop()
    if k in out:
        continue
    e = pk[k]
    out[k] = e
    for d in e.get("dependencies", {}):
        todo.append(resolve(k, d))
    for d in e.get("optionalDependencies", {}):
        print("optional dependency:", k, d, file=sys.stderr)

lock["packages"] = {k: out[k] for k in pk if k in out}
sys.stdout.write(json.dumps(lock, indent=2) + "\n")
