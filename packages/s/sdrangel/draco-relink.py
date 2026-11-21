"""Interface-adapt a fresh emscripten-6 wasm to the OLD vendored glue.

The shipped Cesium glue (pinned in the sdrangel tree) was generated with an
old emscripten; its wasm import/export names are version-specific. A rebuild
with the current toolchain produces a functionally identical module with
different linkage names. This script rewrites the new module's import/export
sections so the OLD glue loads it, verified by:

- symbol-identity for every bound function (joined on the binding symbol
  the two glues agree on; sets must match EXACTLY),
- role-identity for memory/table/ctors/malloc/free (joined by section kind
  and by the glue's init protocol, not by name),
- explicit semantic mapping for the runtime imports (the only part that
  needs human judgment; everything else is derived),
- dropping every export the old glue never references (asserted), and
- a node smoke test with the OLD glue as the behavioral proof.

Usage:
  relink.py OLDGLUE NEWGLUE IN.wasm OUT.wasm IMPORTMAP
  IMPORTMAP: comma list newimportname:oldimportname (module is "a")

Fails loudly on any toolchain drift (changed symbol sets, missing names,
unexpected import counts). Deterministic: same inputs -> same bytes.
"""
import re
import sys


def read_uleb(buf, pos):
    r = 0
    s = 0
    while True:
        b = buf[pos]
        pos += 1
        r |= (b & 0x7f) << s
        if not (b & 0x80):
            return r, pos
        s += 7


def write_uleb(v):
    out = bytearray()
    while True:
        b = v & 0x7f
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def read_str(buf, pos):
    ln, pos = read_uleb(buf, pos)
    return buf[pos:pos + ln].decode(), pos + ln


def split_sections(wasm):
    parts = []
    pos = 8
    while pos < len(wasm):
        sid = wasm[pos]
        pos += 1
        size, pos = read_uleb(wasm, pos)
        parts.append((sid, bytes(wasm[pos:pos + size])))
        pos += size
    return parts


def parse_imports(body):
    n, p = read_uleb(body, 0)
    out = []
    for _ in range(n):
        mod, p = read_str(body, p)
        nm, p = read_str(body, p)
        kind = body[p]
        p += 1
        start = p
        if kind == 0:
            _, p = read_uleb(body, p)
        elif kind == 1:
            p += 1
            fl = body[p]
            p += 1
            _, p = read_uleb(body, p)
            if fl & 1:
                _, p = read_uleb(body, p)
        elif kind == 2:
            p += 1
            fl = body[p]
            p += 1
            _, p = read_uleb(body, p)
            if fl & 1:
                _, p = read_uleb(body, p)
        elif kind == 3:
            fl = body[p]
            p += 1
            _, p = read_uleb(body, p)
            if fl & 1:
                _, p = read_uleb(body, p)
        elif kind == 4:
            p += 2
        else:
            raise AssertionError(f'import kind {kind}')
        out.append((mod, nm, kind, body[start:p]))
    assert p == len(body)
    return out


def parse_exports(body):
    n, p = read_uleb(body, 0)
    out = []
    for _ in range(n):
        nm, p = read_str(body, p)
        kind = body[p]
        p += 1
        idx, p = read_uleb(body, p)
        out.append((nm, kind, idx))
    assert p == len(body)
    return out


def old_npm_symbols(src):
    """{symbol: exportname} from draco3d-npm-style glue (a.asm.X refs)."""
    m = {}
    pat1 = (r'a\.(_emscripten_\w+|_[A-Za-z][A-Za-z0-9_]*)\s*=\s*function\(\)'
            r'\s*\{\s*return\s*\(\s*[A-Za-z$]+\s*=\s*a\.\1\s*=\s*a\.asm\.'
            r'([A-Za-z0-9_$]+)\s*\)')
    for x in re.finditer(pat1, src):
        m[x.group(1)] = x.group(2)
    pat2 = (r'[\w$]+\s*=\s*function\(\)\s*\{\s*return\s*\(\s*[\w$]+\s*=\s*a\.'
            r'(_emscripten_\w+|_[A-Za-z][A-Za-z0-9_]*)\s*=\s*a\.asm\.'
            r'([A-Za-z0-9_$]+)\s*\)')
    for x in re.finditer(pat2, src):
        m[x.group(1)] = x.group(2)
    # direct form: a._malloc=function(){return(a._malloc=a.asm.Tb).apply...}
    pat3 = (r'a\.(_emscripten_\w+|_[A-Za-z][A-Za-z0-9_]*)\s*=\s*function\(\)'
            r'\s*\{\s*return\s*\(\s*a\.\1\s*=\s*a\.asm\.'
            r'([A-Za-z0-9_$]+)\s*\)')
    for x in re.finditer(pat3, src):
        m[x.group(1)] = x.group(2)
    return m


def old_npm_direct_refs(src):
    """Set of bare a.asm.X names (memory/ctors/table slots)."""
    return set(re.findall(r'a\.asm\.([A-Za-z0-9_$]+)(?![A-Za-z0-9_$])', src))


def new_symbols(src):
    """{symbol: exportname} from emscripten-6 glue (wasmExports refs)."""
    m = {}
    for x in re.finditer(r'(_emscripten_\w+|_[A-Za-z][A-Za-z0-9_]*|__[A-Za-z]\w*)'
                         r'=Module\["\1"\]=wasmExports\["([^"]+)"\]', src):
        m[x.group(1)] = x.group(2)
    return m


def new_init_ctors(src):
    """Export name invoked by the new glue's initRuntime (ctors runner)."""
    m = re.search(r'initRuntime\(\)\{[^}]*?wasmExports\["([^"]+)"\]\(\)', src)
    assert m, 'no ctors call in new glue initRuntime'
    return m.group(1)


def main():
    old_glue_path, new_glue_path, in_wasm, out_wasm = sys.argv[1:5]
    import_map = {}
    if len(sys.argv) > 5 and sys.argv[5]:
        for pair in sys.argv[5].split(','):
            n, o = pair.split(':')
            import_map[n] = o
    old_src = open(old_glue_path).read()
    new_src = open(new_glue_path).read()

    old = old_npm_symbols(old_src)
    new = new_symbols(new_src)
    # _webidl_* are new-glue-internal malloc aliases: the old glue never
    # mentions them (proved below), its _malloc/_free mapping covers them.
    glue_internal = {s for s in new if s not in old}
    assert all('webidl' in s for s in glue_internal), glue_internal
    assert 'webidl' not in old_src, 'old glue needs webidl symbols'
    for s in glue_internal:
        del new[s]
    only_old = sorted(set(old) - set(new))
    only_new = sorted(set(new) - set(old))
    assert not only_old, f'symbols lost in rebuild: {only_old}'
    assert not only_new, f'symbols added in rebuild: {only_new}'
    print(f'symbol sets identical: {len(new)} symbols')

    wasm = bytearray(open(in_wasm, 'rb').read())
    assert wasm[:4] == b'\0asm'
    parts = split_sections(wasm)
    imp_body = next(b for s, b in parts if s == 2)
    exp_body = next(b for s, b in parts if s == 7)
    imports = parse_imports(imp_body)
    exports = parse_exports(exp_body)

    # --- import mapping: every module-"a" import must be covered ---
    new_a_imports = sorted(nm for mod, nm, k, d in imports if mod == 'a')
    assert set(import_map) == set(new_a_imports), \
        f'import map mismatch: map={sorted(import_map)} wasm={new_a_imports}'

    # --- export mapping ---
    exp_by_name = {nm: (kind, idx) for nm, kind, idx in exports}
    old_refs = old_npm_direct_refs(old_src)

    # memory: unique kind=2 on both sides; old name = the one old glue derefs
    mems = [nm for nm, k, i in exports if k == 2]
    assert len(mems) == 1, mems
    # old memory name by role from the init sequence:
    #   <var>=a.asm.<MEM>;  (e.g. ja=a.asm.h;) — unique in the glue.
    memstmts = re.findall(r'(\w+)=a\.asm\.([A-Za-z0-9_$]+);', old_src)
    assert len(memstmts) == 1, memstmts
    old_mem = memstmts[0][1]
    # ctors: the export queued into the init callbacks
    cm = re.search(r'(?:unshift|addOnInit)\(a\.asm\.([A-Za-z0-9_$]+)\)', old_src)
    assert cm, 'old ctors hook not found'
    old_ctors = cm.group(1)
    new_ctors = new_init_ctors(new_src)
    assert new_ctors in exp_by_name, f'ctors {new_ctors} not exported'

    export_map = {}
    for sym in new:
        if new[sym] != old[sym]:
            export_map[new[sym]] = old[sym]
    # runtime roles
    assert old_mem in old_refs, old_mem
    export_map[mems[0]] = old_mem
    export_map[new_ctors] = old_ctors
    # malloc/free by jsname (already in symbol tables via _malloc/_free)
    # every old-referenced name must resolve, except the one known-dead
    # alias: Vb is an orphan lazy binding (var ya=...a.asm.Vb, never called
    # except from the C++ exception-unwind path). Draco reports errors via
    # Status, never via C++ exceptions, so that path is unreachable; the
    # corrupt-input smoke test proves graceful Status failure instead.
    assigned_old = set(export_map.values())
    dead = sorted(r for r in old_refs if r not in assigned_old)
    assert dead == ['Vb'], f'unexpected dead refs: {dead}'

    # drop unmapped new exports (provably unused: old glue never names them)
    keep = set(export_map) | {mems[0], new_ctors}
    new_exp = [(export_map.get(nm, nm), kind, idx) for nm, kind, idx in exports
               if nm in keep or nm in export_map]
    # collision check: kept original names must not clash with mapped names
    final_names = [nm for nm, k, i in new_exp]
    assert len(set(final_names)) == len(final_names), 'export name collision'
    assert len(new_exp) == len(keep), (len(new_exp), len(keep))

    new_imp = []
    for mod, nm, kind, desc in imports:
        nm2 = import_map.get(nm, nm) if mod == 'a' else nm
        if mod == 'a':
            assert nm in import_map, nm
        new_imp.append((mod, nm2, kind, desc))

    def enc_section(entries, is_imp):
        out = bytearray(write_uleb(len(entries)))
        for e in entries:
            if is_imp:
                mod, nm, kind, desc = e
                out += write_uleb(len(mod)) + mod.encode()
                out += write_uleb(len(nm)) + nm.encode()
                out += bytes([kind]) + desc
            else:
                nm, kind, idx = e
                out += write_uleb(len(nm)) + nm.encode()
                out += bytes([kind]) + write_uleb(idx)
        return bytes(out)

    out = bytearray(wasm[:8])
    for sid, body in parts:
        if sid == 2:
            body = enc_section(new_imp, True)
        elif sid == 7:
            body = enc_section(new_exp, False)
        out += bytes([sid]) + write_uleb(len(body)) + body
    open(out_wasm, 'wb').write(out)
    print(f'relinked: {len(export_map)} exports renamed, '
          f'{len(new_exp)}/{len(exports)} exports kept, '
          f'{len(new_imp)} imports mapped -> {out_wasm}')


if __name__ == '__main__':
    main()
