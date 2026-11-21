// The MCP SDK inlines fast-uri into its ajv chunks. Replace that copy with
// the sources of the release unpacked in the directory given as argument.
import { readFileSync, readdirSync, writeFileSync } from "node:fs";

const [from, to, release] = process.argv.slice(2);
const dist = "node_modules/@modelcontextprotocol/server/dist";
const chunks = readdirSync(dist).filter((name) => /^ajvProvider-.*\.[cm]js$/.test(name));
if (chunks.length !== 2) throw new Error(`expected two ajv chunks, found ${chunks.length}`);

for (const chunk of chunks) {
  let text = readFileSync(`${dist}/${chunk}`, "utf8");
  for (const file of ["lib/utils.js", "lib/schemes.js", "index.js"]) {
    const start = text.indexOf(`/fast-uri@${from}/node_modules/fast-uri/${file}\n`);
    const open = text.indexOf("\n", start) + 1;
    const body = text.indexOf("\n", open) + 1;
    const close = text.indexOf("\n}));\n\n//#endregion\n", body) + 1;
    if (start < 0 || close < 1) throw new Error(`${chunk}: no fast-uri ${from} ${file}`);
    const source = readFileSync(`${release}/${file}`, "utf8")
      .replace(/require\('\.\/(lib\/)?utils'\)/, "require_utils()")
      .replace("require('./lib/schemes')", "require_schemes()");
    if (source.includes("require(")) throw new Error(`${file}: unexpected require()`);
    text = text.slice(0, body) + source + text.slice(close);
  }
  writeFileSync(`${dist}/${chunk}`, text.replaceAll(`/fast-uri@${from}/`, `/fast-uri@${to}/`));
}
