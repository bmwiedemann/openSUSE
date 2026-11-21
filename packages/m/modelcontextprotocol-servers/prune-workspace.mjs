// Reduce the npm workspace to the packaged servers. tsc comes from the
// distribution, so of the dev dependencies only the type declarations stay.
import { readFileSync, writeFileSync } from "node:fs";

const edit = (file, change) => {
  const json = JSON.parse(readFileSync(file, "utf8"));
  change(json);
  writeFileSync(file, JSON.stringify(json, null, 2) + "\n");
};
const workspaces = ["src/everything", "src/filesystem", "src/memory", "src/sequentialthinking"];

edit("package.json", (json) => {
  json.workspaces = workspaces;
  delete json.dependencies;
  delete json.devDependencies;
});
for (const ws of workspaces) {
  edit(`${ws}/package.json`, (json) => {
    json.devDependencies = Object.fromEntries(
      Object.entries(json.devDependencies).filter(([name]) => name.startsWith("@types/")),
    );
  });
}
