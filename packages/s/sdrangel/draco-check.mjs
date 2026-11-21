// Decode smoke test for the rebuilt draco_decoder.wasm: instantiates draco's
// own nodejs glue (the same interface version the shipped Cesium glue was
// built against) with the freshly relinked wasm and checks structural output
// against values verified with the prebuilt module. Covers both Cesium decode
// paths: mesh (GltfDraco) and point cloud (I3S), plus graceful rejection of
// corrupt input (Status, never a throw).
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { strict as assert } from 'node:assert';
import path from 'node:path';

const dir = path.resolve(process.argv[2]);
const require = createRequire(import.meta.url);
const createDecoderModule = require(path.join(dir, 'draco_decoder_nodejs.js'));

const module = await createDecoderModule({});

// Mesh path (bunny.drc, draco's own sample)
{
  const data = new Uint8Array(readFileSync(path.join(dir, 'bunny.drc')));
  const decoder = new module.Decoder();
  const buf = new module.DecoderBuffer();
  buf.Init(data, data.length);
  assert.equal(decoder.GetEncodedGeometryType(buf), module.TRIANGULAR_MESH);
  const geom = new module.Mesh();
  const status = decoder.DecodeBufferToMesh(buf, geom);
  assert.ok(status.ok(), 'decode failed');
  const faces = geom.num_faces(), points = geom.num_points();
  console.log('draco-check: faces=' + faces + ' points=' + points);
  assert.equal(faces, 69451);
  assert.equal(points, 34834);
  const posId = decoder.GetAttributeId(geom, module.POSITION);
  const pos = decoder.GetAttribute(geom, posId);
  const tmp = new module.DracoFloat32Array();
  decoder.GetAttributeFloatForAllPoints(geom, pos, tmp);
  const vals = [tmp.GetValue(0), tmp.GetValue(1), tmp.GetValue(2)];
  console.log('draco-check: pos0=' + vals.join(','));
  const expected = [-0.09055579453706741, 0.14438968896865845, 0.027556151151657104];
  for (let i = 0; i < 3; ++i) {
    assert.ok(Math.abs(vals[i] - expected[i]) < 1e-9, 'pos mismatch at ' + i);
  }
  // face indices (the Cesium decodeDraco path)
  const fi = new module.DracoInt32Array();
  assert.ok(decoder.GetFaceFromMesh(geom, 0, fi));
  console.log('draco-check: face0=' + [fi.GetValue(0), fi.GetValue(1), fi.GetValue(2)].join(','));
  module.destroy(fi);
  // unique-id lookup (the Cesium compressed-attributes path)
  const pa2 = decoder.GetAttributeByUniqueId(geom, pos.unique_id());
  const tmp2 = new module.DracoFloat32Array();
  decoder.GetAttributeFloatForAllPoints(geom, pa2, tmp2);
  assert.equal(tmp2.GetValue(0), tmp.GetValue(0));
  assert.equal(tmp2.GetValue(1), tmp.GetValue(1));
  console.log('draco-check: unique-id roundtrip OK');
  module.destroy(tmp2);
  module.destroy(buf);
  module.destroy(geom);
  module.destroy(decoder);
}
// Point-cloud path (cube_pc.drc from draco's testdata)
{
  const data = new Uint8Array(readFileSync(path.join(dir, 'cube_pc.drc')));
  const decoder = new module.Decoder();
  const buf = new module.DecoderBuffer();
  buf.Init(data, data.length);
  assert.equal(decoder.GetEncodedGeometryType(buf), module.POINT_CLOUD);
  const geom = new module.PointCloud();
  assert.ok(decoder.DecodeBufferToPointCloud(buf, geom).ok());
  assert.equal(geom.num_points(), 24);
  assert.equal(geom.num_attributes(), 3);
  const pa = decoder.GetAttribute(geom, decoder.GetAttributeId(geom, module.POSITION));
  const tmp = new module.DracoFloat32Array();
  decoder.GetAttributeFloatForAllPoints(geom, pa, tmp);
  assert.equal(tmp.size(), 72);
  const vals = [];
  for (let i = 0; i < 6; ++i) vals.push(tmp.GetValue(i));
  assert.deepEqual(vals, [0, 0, 0, 1, 1, 0]);
  console.log('draco-check: pointcloud OK (24 pts, pos head 0,0,0,1,1,0)');
  module.destroy(buf);
  module.destroy(geom);
  module.destroy(decoder);
}
// Small quantized mesh (cube_att.drc from draco's testdata)
{
  const data = new Uint8Array(readFileSync(path.join(dir, 'cube_att.drc')));
  const decoder = new module.Decoder();
  const buf = new module.DecoderBuffer();
  buf.Init(data, data.length);
  assert.equal(decoder.GetEncodedGeometryType(buf), module.TRIANGULAR_MESH);
  const geom = new module.Mesh();
  assert.ok(decoder.DecodeBufferToMesh(buf, geom).ok());
  assert.equal(geom.num_faces(), 12);
  assert.equal(geom.num_points(), 24);
  console.log('draco-check: small mesh OK (12 faces, 24 points)');
  module.destroy(buf);
  module.destroy(geom);
  module.destroy(decoder);
}
// Corrupt input must fail gracefully (Status, never a throw)
{
  const decoder = new module.Decoder();
  const buf = new module.DecoderBuffer();
  buf.Init(new Uint8Array([68, 82, 65, 67, 79, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 16);
  const geom = new module.Mesh();
  assert.ok(!decoder.DecodeBufferToMesh(buf, geom).ok(), 'corrupt input decoded?!');
  console.log('draco-check: corrupt input rejected as expected');
  module.destroy(buf);
  module.destroy(geom);
  module.destroy(decoder);
}
console.log('draco-check: OK');
