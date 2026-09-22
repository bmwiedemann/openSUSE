# ai-bwrap config — adds the Gemini CLI and Kit agents.
# Point ai-bwrap at this file with:  AI_BWRAP_CONFIG=./config.sh ai-bwrap gemini

# ---------------------------------------------------------------------------
# Shared by ALL agents (built-in + custom): the system CA certificate store.
# On SUSE/openSUSE the CA bundle lives under /var/lib/ca-certificates/ and
# /etc/ssl/certs + /etc/ssl/ca-bundle.pem are relative symlinks out of /etc.
# bwrap mounts /etc ro but never /var, so those symlinks dangle → curl/libcurl
# can't build a trust chain. Bind the real store (--ro-bind-try no-ops where
# absent, e.g. RHEL /etc/pki/tls) and pin it for tools that ignore OS defaults.
EXTRA_RO_BINDS+=( "/var/lib/ca-certificates" )
EXTRA_ENV_VARS+=( "SSL_CERT_FILE=/etc/ssl/ca-bundle.pem" )
EXTRA_ENV_VARS+=( "SSL_CERT_DIR=/etc/ssl/certs" )

# gemini — Google's Gemini CLI (https://github.com/google-gemini/gemini-cli).
# Node-based: ~/.npm (already a common passthrough) covers the npx cache and
# install dir; ~/.gemini holds settings, commands, skills and OAuth creds.
agent_gemini() {
    mkdir -p "$HOME/.gemini" "$HOME/.cache/gemini"
    AGENT_BINDS+=(
        --bind-try "$HOME/.gemini"      "$HOME/.gemini"
        --bind-try "$HOME/.cache/gemini" "$HOME/.cache/gemini"
    )

    # Pass through the auth/config vars the CLI needs, but only the ones that
    # are actually set: bwrap does not inherit the shell environment, and
    # injecting an unset/empty var would be noise. Define these in your shell
    # or in this config file.
    local v
    for v in \
        GEMINI_API_KEY \
        GEMINI_MODEL \
        GOOGLE_API_KEY \
        GOOGLE_CLOUD_PROJECT \
        GOOGLE_CLOUD_PROJECT_ID \
        GOOGLE_CLOUD_LOCATION \
        GOOGLE_APPLICATION_CREDENTIALS \
        GOOGLE_GENAI_API_VERSION \
        GOOGLE_GEMINI_BASE_URL \
        GOOGLE_VERTEX_BASE_URL \
        GEMINI_CLI_HOME \
        GEMINI_CLI_TRUST_WORKSPACE \
        NO_COLOR \
        CLI_TITLE
    do
        [[ -n "${!v:-}" ]] && AGENT_BINDS+=(--setenv "$v" "${!v}")
    done

    if command -v gemini >/dev/null 2>&1; then
        EXEC_CMD=("$(command -v gemini)")
    else
        local npx
        npx="$(command -v npx 2>/dev/null)" || die "neither 'gemini' nor 'npx' found on PATH"
        EXEC_CMD=("$npx" -y @google/gemini-cli)
    fi
}

# kit — Knowledge Inference Tool (https://github.com/mark3labs/kit).
# A Go binary installed to ~/.local/bin (already a common passthrough) or via
# npm (covered by the ~/.npm passthrough). State lives in:
#   ~/.kit/          sessions (<cwd-path>/<timestamp>_<id>.jsonl), prompt templates
#   ~/.kit.yml       global config (model, temperature, mcpServers, ...)
#   ~/.config/kit/   credentials.json, preferences.yml, themes, agents, extensions
agent_kit() {
    mkdir -p "$HOME/.kit/sessions" "$HOME/.kit/prompts" "$HOME/.config/kit"
    AGENT_BINDS+=(
        --bind-try  "$HOME/.kit"          "$HOME/.kit"
        --bind-try  "$HOME/.kit.yml"      "$HOME/.kit.yml"
        --bind-try  "$HOME/.kit.yaml"     "$HOME/.kit.yaml"
        --bind-try  "$HOME/.kit.json"     "$HOME/.kit.json"
        --bind-try  "$HOME/.config/kit"   "$HOME/.config/kit"
        --bind-try  "$HOME/.local/share/kit" "$HOME/.local/share/kit" # git-installed packages
    )
    local kit
    kit="$(command -v kit 2>/dev/null)" || die "'kit' not found on PATH (install: npm i -g @mark3labs/kit)"
    EXEC_CMD=("$kit")
}
