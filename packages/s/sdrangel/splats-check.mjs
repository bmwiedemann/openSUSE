// Smoke-test for the from-source wasm_splats_bg.wasm build: instantiates the
// module with its generated JS glue and checks both exported functions against
// outputs verified bit-identical with the previously shipped prebuilt module.
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { strict as assert } from 'node:assert';

const outDir = process.argv[2];
const glue = await import(pathToFileURL(`${outDir}/wasm_splats.js`).href);
const bytes = readFileSync(`${outDir}/wasm_splats_bg.wasm`);
await glue.default(new Response(bytes, { headers: { 'Content-Type': 'application/wasm' } }));

const positions = new Float32Array([0,0,1, 1,2,3, -1,0,2, 0.5,0.5,0.5, 2,2,2]);
const scales = new Float32Array([1,1,1, 2,2,2, 0.5,0.5,0.5, 1,2,1, 3,3,3]);
const rotations = new Float32Array([0,0,0,1, 0,0,0,1, 0,0,0,1, 0,0,0,1, 0,0,0,1]);
const colors = new Uint8Array([255,0,0,255, 0,255,0,255, 0,0,255,255, 255,255,0,255, 0,255,255,255]);
const modelView = new Float32Array([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]);

const tex = glue.generate_splat_texture(positions, scales, rotations, colors, 5);
assert.equal(tex.width, 2048);
assert.equal(tex.height, 1);
assert.deepEqual(Array.from(tex.data.slice(0, 8)), [0, 0, 1065353216, 0, 17408, 1140850688, 1140850688, 4278190335]);

const idx = glue.radix_sort_gaussians_indexes(positions, modelView, 5);
assert.deepEqual(Array.from(idx), [3, 0, 2, 4, 1]);

console.log('splats-check: generate_splat_texture + radix_sort_gaussians_indexes OK');
