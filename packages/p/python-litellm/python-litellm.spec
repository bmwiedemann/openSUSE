#
# spec file for package python-litellm
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define skip_python314 1
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-litellm
Version:        1.101.0
Release:        0
Summary:        Library to easily interface with LLM API providers
License:        MIT
URL:            https://www.litellm.ai/
Source0:        https://github.com/BerriAI/litellm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uv-build}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.14.2
Requires:       python-boto3 >= 1.43.1
Requires:       python-click >= 8.0
Requires:       python-fastuuid >= 0.14.0
Requires:       python-httpx >= 0.28.0
Requires:       python-importlib-metadata >= 8.0
Requires:       python-jinja2 >= 3.1.6
Requires:       python-jsonschema >= 4.22.0
Requires:       python-openai >= 2.20.0
Requires:       python-pydantic >= 2.10.0
Requires:       python-pydantic-settings >= 2.14.1
Requires:       python-python-dotenv >= 1.0
Requires:       python-tiktoken >= 0.8
Requires:       python-tokenizers >= 0.21
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
LiteLLM manages:

- Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints
- [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Set Budgets & Rate limits per project, api key, model [LiteLLM Proxy Server (LLM Gateway)](https://docs.litellm.ai/docs/simple_proxy)

%prep
%autosetup -p1 -n litellm-%{version}
# 1.101.0 switched the PEP 517 backend to maturin to build a new Rust extension
# (litellm.rust_bridge._native). That bridge is opt-in at runtime
# (LITELLM_RUST, default off) and falls back to the pure-Python path when the
# native module is absent, so we keep the pure-Python noarch wheel and build it
# with uv_build, the backend this package used up to 1.89.1 and that is present
# in the build environment.
#
# 1.101.0 also moved its flat-layout ("module-root = """) and enterprise-exclude
# configuration into [tool.maturin], so a bare build-backend swap is not enough:
# left on its defaults, uv_build assumes the src/ layout and fails with "Expected
# a Python module at: src/litellm/__init__.py", and it would no longer exclude the
# litellm/proxy/enterprise symlink. Restore the block 1.89.1's build relied on.
sed -i -e 's/^requires = \[[^]]*\]$/requires = ["uv_build"]/' \
    -e 's/^build-backend = .*$/build-backend = "uv_build"/' pyproject.toml
cat >> pyproject.toml <<'PYPROJECT_UV_BACKEND'

[tool.uv.build-backend]
module-root = ""
source-exclude = [
    "litellm/proxy/enterprise",
    "**/__pycache__",
    "**/__pycache__/**",
    "**/.mypy_cache",
    "**/.mypy_cache/**",
    "**/.pytest_cache",
    "**/.pytest_cache/**",
    "**/.ruff_cache",
    "**/.ruff_cache/**",
]
PYPROJECT_UV_BACKEND
# Remove shebangs from non-executable Python modules
sed -i '1{/^#!.*python/d}' litellm/proxy/guardrails/guardrail_hooks/azure/prompt_shield.py
sed -i '1{/^#!.*python/d}' litellm/proxy/guardrails/guardrail_hooks/azure/text_moderation.py
sed -i '1{/^#!.*python/d}' litellm/proxy/guardrails/guardrail_hooks/openai/moderations.py
sed -i '1{/^#!.*python/d}' litellm/proxy/guardrails/guardrail_hooks/panw_prisma_airs/panw_prisma_airs.py
# Remove .gitignore files
find . -name .gitignore -delete

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/litellm
%python_clone -a %{buildroot}%{_bindir}/lite
%python_clone -a %{buildroot}%{_bindir}/litellm-proxy

%pre
%python_libalternatives_reset_alternative litellm
%python_libalternatives_reset_alternative lite
%python_libalternatives_reset_alternative litellm-proxy

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/litellm
%python_alternative %{_bindir}/lite
%python_alternative %{_bindir}/litellm-proxy
%{python_sitelib}/litellm
%{python_sitelib}/litellm-%{version}.dist-info

%changelog
