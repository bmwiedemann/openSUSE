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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define skip_python314 1

Name:           python-litellm
Version:        1.89.1
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
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Requires:       python-aiohttp >= 3.10
Requires:       python-click
Requires:       python-fastuuid >= 0.13.0
Requires:       python-httpx >= 0.23.0
Requires:       python-importlib-metadata >= 6.8.0
Requires:       python-jinja2 >= 3.1.2
Requires:       python-jsonschema >= 4.22.0
Requires:       python-openai >= 2.8.0
Requires:       python-pydantic >= 2.5.0
Requires:       python-python-dotenv >= 0.2.0
Requires:       python-tiktoken >= 0.7.0
Requires:       python-tokenizers

BuildArch:      noarch
%python_subpackages

%description
LiteLLM manages:

- Translate inputs to provider's `completion`, `embedding`, and `image_generation` endpoints
- [Consistent output](https://docs.litellm.ai/docs/completion/output), text responses will always be available at `['choices'][0]['message']['content']`
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Set Budgets & Rate limits per project, api key, model [LiteLLM Proxy Server (LLM Gateway)](https://docs.litellm.ai/docs/simple_proxy)

%prep
%autosetup -p1 -n litellm-%{version}
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
%python_clone -a %{buildroot}%{_bindir}/litellm-proxy

%pre
%python_libalternatives_reset_alternative litellm
%python_libalternatives_reset_alternative litellm-proxy

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/litellm
%python_alternative %{_bindir}/litellm-proxy
%{python_sitelib}/litellm
%{python_sitelib}/litellm-%{version}.dist-info

%changelog
