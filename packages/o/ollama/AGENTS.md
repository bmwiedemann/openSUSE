# ollama packaging rules for pbuild-ai

## Updating the package

The only build recipe of this package is `ollama.spec` in the workspace root.

After the `Version:` tag in `ollama.spec` has been changed, apply the
OLLAMA_UPDATE skill (`_agents/skills/OLLAMA_VERSION_UPDATE.md`) by running
the post-update script `_agents/skills/update_references.sh`.
