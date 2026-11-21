'use strict';
// End-to-end smoke test for the source-built basis transcoder inside the
// shipped Cesium worker bundle: drives Workers/transcodeKTX2.js through its
// real two-message task protocol (init, then KTX2 transcode of kodim23.ktx2)
// and checks dimensions and level bytes against verified values.
// Usage: node basis-e2e.cjs <bundle-path> <workdir>
//   <workdir> holds copies of kodim23.ktx2 and basis_transcoder.wasm.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert');

const bundlePath = path.resolve(process.argv[2]);
const dir = path.resolve(process.argv[3]);
// Test-only shims: the Emscripten factory's node branch reads __dirname and
// require (in production it runs in a WebEngine worker, neither is touched).
globalThis.require = require;
globalThis.__dirname = dir;
globalThis.__filename = path.join(dir, 'basis-e2e.cjs');

const posted = [];
globalThis.self = {};
globalThis.postMessage = (msg) => { posted.push(msg); };

(async () => {
  await import(bundlePath);
  const onmessage = globalThis.self.onmessage;
  assert.equal(typeof onmessage, 'function');
  const ktx2 = new Uint8Array(fs.readFileSync(path.join(dir, 'kodim23.ktx2')));
  const wasmFile = path.join(dir, 'basis_transcoder.wasm');

  await onmessage({ data: { id: 1, baseUrl: 'http://localhost/', canTransferArrayBuffer: true,
    parameters: { webAssemblyConfig: { wasmBinaryFile: wasmFile } } } });
  await new Promise((r) => setTimeout(r, 500));
  assert.equal(posted.length, 1);
  assert.equal(posted[0].result, true);
  console.log('basis-e2e: init OK');

  await onmessage({ data: { id: 2, baseUrl: 'http://localhost/', canTransferArrayBuffer: true,
    parameters: { ktx2Buffer: ktx2, supportedTargetFormats: { etc: true } } } });
  await new Promise((r) => setTimeout(r, 500));
  assert.equal(posted.length, 2);
  const m = posted[1];
  if (m.error) { console.error('WORKER ERROR:', m.error); process.exit(1); }
  assert.equal(m.result.length, 10);
  const px = m.result[0].positiveX;
  console.log('basis-e2e: level0 ' + px.width + 'x' + px.height +
    ' internalFormat=' + px.internalFormat + ' bufBytes=' + px.levelBuffer.byteLength);
  assert.equal(px.width, 768);
  assert.equal(px.height, 512);
  assert.equal(px.levelBuffer.byteLength, 192 * 128 * 8);
  console.log('basis-e2e: OK');
})().catch((e) => { console.error('HARNESS FAIL:', e); process.exit(1); });
