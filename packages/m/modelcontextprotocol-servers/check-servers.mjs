// Start an MCP server on stdio, call the tools given as name=arguments and
// print each result. Any error, also one a tool reports, fails the run.
import { spawn } from "node:child_process";
import { createInterface } from "node:readline";

const [server, ...calls] = process.argv.slice(2);
const child = spawn(server, { stdio: ["pipe", "pipe", "inherit"] });
const replies = createInterface({ input: child.stdout })[Symbol.asyncIterator]();
const send = (message) => child.stdin.write(JSON.stringify({ jsonrpc: "2.0", ...message }) + "\n");
const fail = (reason) => {
  console.error(`${server}: ${reason}`);
  child.kill();
  process.exit(1);
};
let id = 0;
const request = async (method, params) => {
  send({ id: ++id, method, params });
  for (;;) {
    const { value, done } = await replies.next();
    if (done) fail(`${method}: no reply`);
    const reply = JSON.parse(value);
    if (reply.id !== id) continue;
    if (reply.error || reply.result.isError) fail(value);
    console.log(JSON.stringify(reply.result));
    return;
  }
};

setTimeout(fail, 30000, "timeout");
await request("initialize", {
  protocolVersion: "2025-06-18",
  capabilities: {},
  clientInfo: { name: "rpm-check", version: "0" },
});
send({ method: "notifications/initialized" });
for (const call of calls) {
  const split = call.indexOf("=");
  await request("tools/call", { name: call.slice(0, split), arguments: JSON.parse(call.slice(split + 1)) });
}
child.kill();
process.exit(0);
