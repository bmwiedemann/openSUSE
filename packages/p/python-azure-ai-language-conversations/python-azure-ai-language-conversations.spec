#
# spec file for package python-azure-ai-language-conversations
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-azure-ai-language-conversations
Version:        1.1.0
Release:        0
Summary:        Microsoft Azure Conversational Language Understanding Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-language-conversations/azure-ai-language-conversations-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-language-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-ai-language-nspkg >= 1.0.0
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-six >= 1.11.0
Requires:       (python-azure-common >= 1.1 with python-azure-common < 2.0.0)
Requires:       (python-azure-core >= 1.24.0 with python-azure-core < 2.0.0)
Requires:       (python-isodate >= 0.6.1 with python-isodate < 1.0.0)
Requires:       (python-typing_extensions >= 4.3.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%{?sle15_python_module_pythons}
%python_subpackages

%description
Conversational Language Understanding, aka CLU for short, is a cloud-based conversational
AI service which is mainly used in bots to extract useful information from user utterance
(natural language processing). The CLU analyze api encompasses two projects; conversation,
and orchestration projects. You can use the "conversation" project if you want to extract
intents (intention behind a user utterance) and custom entities. You can also use the
"orchestration" project which orchestrates multiple language apps to get the best response
(language apps like Question Answering, Luis, and Conversation).

%prep
%setup -q -n azure-ai-language-conversations-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-language-conversations-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/language/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/language/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/language/conversations
%{python_sitelib}/azure_ai_language_conversations-*.egg-info

%changelog
