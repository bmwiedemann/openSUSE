# gufo packaging rules for pbuild-ai

## Updating the package

The only build recipe of this package is `ollama.spec` in the workspace root.

After the `Version:` tag in `ollama.spec` has been changed, apply the
GUFO_UPDATE skill (`_agents/skills/GUFO_VERSION_UPDATE.md`) by running
the post-update script `_agents/skills/update_references.sh`.
