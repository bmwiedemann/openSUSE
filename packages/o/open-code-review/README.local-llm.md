# Using OCR with a local LLM (Ollama)

OCR normally talks to a cloud LLM API. You can point it at a local model
instead, served by Ollama's OpenAI-compatible endpoint. Nothing leaves
your machine: the model runs locally, and OCR sends it only the diff
you ask it to review.

## 1. Install and run Ollama

Install Ollama (the `ollama` package is in openSUSE, or download it from
<https://ollama.com>), then pull a model and start the server:

```bash
ollama pull qwen3:32b
ollama serve
```

Ollama listens on <http://127.0.0.1:11434> by default; its
OpenAI-compatible endpoint is <http://127.0.0.1:11434/v1>.

> The model must support native tool calling (function calling). OCR drives
> the review entirely through tool calls, so a model that only narrates tool
> calls in its text output (e.g. `deepseek-r1`) cannot work. `qwen3` works.
> Pick any model tagged with tools support at
> <https://ollama.com/search?c=tools>. A code-focused alternative is
> `qwen2.5-coder` — the same requirement applies.

## 2. Point OCR at Ollama

Register Ollama as a custom provider (the method upstream documents):

```bash
ocr config set provider                          ollama
ocr config set custom_providers.ollama.url       http://127.0.0.1:11434/v1
ocr config set custom_providers.ollama.protocol  openai
ocr config set custom_providers.ollama.model     qwen3:32b
ocr config set custom_providers.ollama.api_key   ollama
```

Ollama ignores the API key, but a custom provider requires a non-empty
`api_key`, so any placeholder value works. Settings are stored in
`~/.opencodereview/config.json`.

Local models are slow, and the per-request HTTP timeout defaults to
300 seconds. If requests time out, raise it for the Ollama provider:

```bash
ocr config set custom_providers.ollama.timeout_sec 900
```

or set `OCR_LLM_TIMEOUT=900` (seconds) for a single run.

### Alternative: environment variables

Instead of the config file, export:

```bash
export OCR_LLM_URL=http://127.0.0.1:11434/v1
export OCR_LLM_TOKEN=ollama
export OCR_LLM_MODEL=qwen3:32b
export OCR_LLM_PROTOCOL=openai
```

`OCR_LLM_PROTOCOL=openai` is required here: without it OCR defaults to
the Anthropic protocol, which Ollama does not speak. The config-file
method above sets the protocol explicitly, so it has no such trap.
When both are set, the config file takes precedence.

## 3. Run a review

From inside a Git repository, review the staged, unstaged and untracked
changes against the local model:

```bash
ocr review
```

To review a branch against its base instead:

```bash
ocr review --from master --to dev-ref
```

See `ocr review --help` for the full options, and the upstream docs at
<https://open-codereview.ai> (configuration and FAQ).
