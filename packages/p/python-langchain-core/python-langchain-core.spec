#
# spec file for package python-langchain-core
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


Name:           python-langchain-core
Version:        1.4.9
Release:        0
Summary:        Building applications with LLMs through composability
License:        MIT
URL:            https://python.langchain.com
Source:         https://files.pythonhosted.org/packages/source/l/langchain_core/langchain_core-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mentioned in https://github.com/langchain-ai/langchain/issues/7100 (auto-closed)
Patch0:         pytest-args.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.3
Requires:       python-jsonpatch >= 1.33
Requires:       python-langchain-protocol >= 0.0.17
Requires:       python-langsmith >= 0.3.45
Requires:       python-packaging >= 23.2
Requires:       python-pydantic >= 2.7.4
Requires:       python-tenacity >= 8.1.0
Requires:       python-typing-extensions >= 4.7
Requires:       python-uuid-utils >= 0.12.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.3}
BuildRequires:  %{python_module blockbuster}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module jsonpatch >= 1.33}
BuildRequires:  %{python_module langchain-protocol >= 0.0.17}
BuildRequires:  %{python_module langsmith >= 0.3.45}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging >= 23.2}
BuildRequires:  %{python_module pydantic >= 2.7.4}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module tenacity >= 8.1.0}
BuildRequires:  %{python_module typing-extensions >= 4.7}
BuildRequires:  %{python_module uuid-utils >= 0.12.0}
# /SECTION
%python_subpackages

%description
LangChain Core contains the base abstractions that power the rest of the
LangChain ecosystem.

These abstractions are designed to be as modular and simple as possible.
Examples of these abstractions include those for language models, document
loaders, embedding models, vectorstores, retrievers, and more.

The benefit of having these abstractions is that any provider can implement the
required interface and then easily be used in the rest of the LangChain
ecosystem.

%prep
%autosetup -p1 -n langchain_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Notes on the ignores/deselects below (the %%pytest invocation must stay on a
# single line: line continuations break the macro's brace expansion):
# - in-memory store/indexer/vectorstore tests and the chat-model compat bridge
#   need python-langchain-tests (not in Factory);
# - the ascii-graph draw_ascii tests need python-grandalf (not in Factory);
# - the SSRF transport tests construct an httpx transport whose openSUSE certifi
#   does a blocking os.stat on the CA bundle that blockbuster flags in the async
#   tests (openSUSE-specific), so the whole transport module is skipped;
# - the public-URL/webhook SSRF tests need live DNS resolution (offline build);
# - the repr/serialization snapshot tests below mismatch only because Factory's
#   pydantic (2.13) emits the default output_version field that the upstream
#   snapshots (pydantic 2.12) omit.
%pytest tests/unit_tests --ignore tests/unit_tests/indexing/test_in_memory_indexer.py --ignore tests/unit_tests/language_models/test_compat_bridge.py --ignore tests/unit_tests/stores/test_in_memory.py --ignore tests/unit_tests/vectorstores/test_in_memory.py --ignore tests/unit_tests/test_ssrf_policy_transport.py --deselect tests/unit_tests/runnables/test_graph.py::test_graph_single_runnable --deselect tests/unit_tests/runnables/test_graph.py::test_graph_sequence --deselect tests/unit_tests/runnables/test_graph.py::test_graph_sequence_map --deselect tests/unit_tests/language_models/chat_models/test_cache.py::test_llm_representation_for_serializable --deselect tests/unit_tests/runnables/test_runnable.py::test_prompt_with_chat_model --deselect tests/unit_tests/runnables/test_runnable.py::test_prompt_with_chat_model_async --deselect tests/unit_tests/runnables/test_runnable.py::test_prompt_with_chat_model_and_parser --deselect tests/unit_tests/runnables/test_runnable.py::test_combining_sequences --deselect tests/unit_tests/runnables/test_runnable.py::test_seq_dict_prompt_llm --deselect tests/unit_tests/runnables/test_runnable.py::test_seq_prompt_dict --deselect tests/unit_tests/runnables/test_runnable.py::test_seq_prompt_map --deselect tests/unit_tests/test_ssrf_protection.py::TestValidateSafeUrl::test_valid_public_https_url --deselect tests/unit_tests/test_ssrf_protection.py::TestValidateSafeUrl::test_valid_public_http_url --deselect tests/unit_tests/test_ssrf_protection.py::TestValidateSafeUrl::test_https_only_mode --deselect tests/unit_tests/test_ssrf_protection.py::TestIsSafeUrl::test_safe_url_returns_true --deselect tests/unit_tests/test_ssrf_protection.py::TestSSRFProtectedUrlType::test_valid_url_accepted --deselect tests/unit_tests/test_ssrf_protection.py::TestRealWorldURLs::test_slack_webhook --deselect tests/unit_tests/test_ssrf_protection.py::TestRealWorldURLs::test_discord_webhook --deselect tests/unit_tests/test_ssrf_protection.py::TestRealWorldURLs::test_webhook_site --deselect tests/unit_tests/test_ssrf_protection.py::TestRealWorldURLs::test_ngrok_url
# Recompile the installed modules as hash-based bytecode: this package ships
# many modules whose timestamp-based .pyc desync from the reproducibility-clamped
# .py mtimes and trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langchain_core
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langchain_core

%files %{python_files}
%doc README.md
%{python_sitelib}/langchain_core
%{python_sitelib}/langchain_core-%{version}.dist-info

%changelog
