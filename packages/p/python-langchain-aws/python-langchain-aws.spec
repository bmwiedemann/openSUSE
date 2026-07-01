#
# spec file for package python-langchain-aws
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


Name:           python-langchain-aws
Version:        1.6.1
Release:        0
Summary:        LangChain integrations for AWS
License:        MIT
URL:            https://github.com/langchain-ai/langchain-aws
Source:         https://files.pythonhosted.org/packages/source/l/langchain_aws/langchain_aws-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-boto3 >= 1.42.42
Requires:       python-langchain-core >= 1.4.7
Requires:       python-numpy >= 1.0.0
Requires:       python-pydantic >= 2.10.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module boto3 >= 1.42.42}
BuildRequires:  %{python_module langchain-core >= 1.4.7}
BuildRequires:  %{python_module numpy >= 1.0.0}
BuildRequires:  %{python_module pydantic >= 2.10.6}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module syrupy}
# /SECTION
%python_subpackages

%description
This package contains the LangChain integrations with AWS, connecting
LangChain to AWS services such as Amazon Bedrock, SageMaker, Neptune and
Kendra.

%prep
%autosetup -p1 -n langchain_aws-%{version}
# The top-level tests/conftest.py is only used by the recorded integration
# tests; it imports python-langchain-tests (not in Factory) and would abort
# unit-test collection. Drop it so the offline unit tests can be collected.
rm tests/conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignored modules pull in packages not available in Factory:
# - test_standard / chat_models test_anthropic / test_bedrock_converse use the
#   python-langchain-tests ChatModel unit-test bridge;
# - middleware/test_prompt_caching needs the full python-langchain meta package;
# - test_versioning exercises ChatAnthropicBedrock (the langchain-aws[anthropic]
#   extra: anthropic + python-langchain-anthropic).
# The ToolNode compatibility tests need langgraph (not in Factory).
%pytest tests/unit_tests --ignore tests/unit_tests/test_standard.py --ignore tests/unit_tests/chat_models/test_anthropic.py --ignore tests/unit_tests/chat_models/test_bedrock_converse.py --ignore tests/unit_tests/middleware/test_prompt_caching.py --ignore tests/unit_tests/test_versioning.py --deselect tests/unit_tests/tools/test_nova_tools.py::TestToolNodeCompatibility
# Recompile the installed modules as hash-based bytecode so the
# timestamp-clamped .pyc do not trip python-bytecode-inconsistent-mtime.
%python_expand $python -m compileall -q -f --invalidation-mode=unchecked-hash -o 0 -o 1 -s %{buildroot} %{buildroot}%{$python_sitelib}/langchain_aws
%python_expand %fdupes %{buildroot}%{$python_sitelib}/langchain_aws

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langchain_aws
%{python_sitelib}/langchain_aws-%{version}.dist-info

%changelog
