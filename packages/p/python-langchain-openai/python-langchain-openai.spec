#
# spec file for package python-langchain-openai
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-langchain-openai
Version:        1.3.3
Release:        0
Summary:        An integration package connecting OpenAI and LangChain
License:        MIT
URL:            https://github.com/langchain-ai/langchain
Source:         https://files.pythonhosted.org/packages/source/l/langchain_openai/langchain_openai-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-langchain-core >= 1.4.7
Requires:       python-openai >= 2.26.0
Requires:       python-tiktoken >= 0.7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module langchain-core >= 1.4.7}
BuildRequires:  %{python_module openai >= 2.26.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module tiktoken >= 0.7.0}
# /SECTION
%python_subpackages

%description
This package contains the LangChain integrations for OpenAI through their
openai SDK.

It provides chat models, LLMs, embeddings and tokenization helpers that let
the OpenAI and Azure OpenAI services be used as components in the LangChain
ecosystem.

%prep
%autosetup -p1 -n langchain_openai-%{version}

# The root tests/conftest.py only provides VCR cassette config for the
# integration tests and unconditionally imports langchain-tests (not in
# Factory); the offline unit tests below do not use any of its fixtures.
rm tests/conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The standard-test bridge modules (test_*_standard.py), test_base, the
# responses streaming tests and the moderation-middleware test need
# python-langchain-tests / python-langchain (not in Factory); the remaining
# unit tests run fully offline. addopts is cleared to drop the --cov default
# (pytest-cov is not needed for the build). The deselected token-counting
# tests call tiktoken with a model whose BPE encoding is not bundled, so
# tiktoken tries to download it from openaipublic.blob.core.windows.net,
# which fails in the offline build.
%pytest tests/unit_tests -o addopts='' --ignore tests/unit_tests/embeddings/test_azure_standard.py --ignore tests/unit_tests/embeddings/test_base_standard.py --ignore tests/unit_tests/chat_models/test_azure_standard.py --ignore tests/unit_tests/chat_models/test_base.py --ignore tests/unit_tests/chat_models/test_base_standard.py --ignore tests/unit_tests/chat_models/test_responses_standard.py --ignore tests/unit_tests/chat_models/test_responses_stream.py --ignore tests/unit_tests/middleware/test_openai_moderation_middleware.py --deselect tests/unit_tests/embeddings/test_base.py::test_embed_documents_with_custom_chunk_size --deselect tests/unit_tests/embeddings/test_base.py::test_embeddings_respects_token_limit --deselect "tests/unit_tests/llms/test_base.py::test_get_token_ids[gpt-3.5-turbo-instruct]" --deselect "tests/unit_tests/test_token_counts.py::test_chat_openai_get_num_tokens[gpt-5.5]" --deselect "tests/unit_tests/test_token_counts.py::test_chat_openai_get_num_tokens[gpt-5-nano]" --deselect "tests/unit_tests/test_token_counts.py::test_chat_openai_get_num_tokens[o3]"
# Recompile the installed modules as hash-based bytecode: the timestamp-based
# .pyc desync from the reproducibility-clamped .py mtimes and trip
# python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langchain_openai
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langchain_openai

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langchain_openai
%{python_sitelib}/langchain_openai-%{version}.dist-info

%changelog
