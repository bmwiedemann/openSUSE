#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Splice a source-built Emscripten basis factory into Cesium's worker bundle.

Provenance:
- BUNDLE (vendored, Cesium 1.145.0): plugins/feature/map/Cesium/Workers/transcodeKTX2.js
  The Emscripten MODULARIZE factory blob ("var Pt=(function(){...})();", built by the
  Cesium team with 2021-era emscripten from BinomialLLC/basis_universal
  webgl/transcoder/basis_wasm_transcoder.cpp) is byte-replaced with a factory built
  from source in %build with system emscripten from the SAME upstream C++ file.
- The surrounding Cesium worker logic (KTX2 parse, format selection, task wiring) is
  NOT touched: it only uses the stable embind public API (initializeBasis, KTX2File
  + methods, transcoder_texture_format), which the replacement provides identically.
- The wasm instantiated by the factory is likewise built from source in %build.

Usage: basis-splice.py <new-glue.js> <bundle-in.js> <bundle-out.js>
  <new-glue.js> is the emcc MODULARIZE output (UMD wrapper stripped here).
"""
import sys

START = 'var Pt=(function(){'
END = '})();typeof ot'


def extract_factory(glue: str) -> str:
    head = 'var BASIS='
    assert glue.startswith(head), 'unexpected glue wrapper'
    tail = ';if(typeof exports==="object"'
    i = glue.find(tail)
    assert i > 0, 'UMD tail anchor not found'
    expr = glue[len(head):i]
    assert expr.startswith('(()=>{') and expr.endswith('})()'), 'factory IIFE shape changed'
    # Cesium always configures this worker with {wasmBinaryFile: url} (see the
    # initWebAssemblyModule call site in Cesium.js). emscripten >= 4 no longer
    # reads Module['wasmBinaryFile'], so without help the factory would ignore
    # the URL and fetch its own baked-in filename next to the worker (404 in
    # production). Wrap the factory to restore the old contract via the
    # still-supported Module['locateFile'] hook (default INCOMING_MODULE_JS_API):
    # when the caller passes wasmBinaryFile and no custom locateFile, every
    # findWasmBinary() call resolves to that URL. Pure JS, per factory call,
    # no emcc involvement; the Emscripten factory blob itself is untouched.
    return ('(()=>{var F=' + expr + ';return function(m){m=m||{};'
            'if(m.wasmBinaryFile&&!m.locateFile){var u=m.wasmBinaryFile;'
            'm.locateFile=function(){return u}}return F(m)}})()')


def main():
    glue_p, in_p, out_p = sys.argv[1:4]
    glue = open(glue_p).read()
    bundle = open(in_p).read()
    factory = extract_factory(glue)
    a = bundle.find(START)
    assert a >= 0 and bundle.count(START) == 1, 'factory start anchor not unique'
    e = bundle.find(END)
    assert e > a, 'factory end anchor missing'
    e += len('})();')
    spliced = bundle[:a] + 'var Pt=' + factory + ';' + bundle[e:]
    # The outer Cesium logic must be byte-identical: only the blob changed.
    assert bundle[:a] == spliced[:a]
    assert bundle[e:] == spliced[a + len('var Pt=' + factory + ';'):]
    open(out_p, 'w').write(spliced)
    print(f'splice ok: blob {e - a} -> {len(factory) + len("var Pt=;")} bytes')


main()
