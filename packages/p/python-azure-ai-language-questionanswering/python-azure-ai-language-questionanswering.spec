#
# spec file for package python-azure-ai-language-questionanswering
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-azure-ai-language-questionanswering
Version:        1.1.0
Release:        0
Summary:        Microsoft Azure Question Answering Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-language-questionanswering/azure-ai-language-questionanswering-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-language-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-ai-language-nspkg >= 1.0.0
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-isodate >= 0.6.1
Requires:       (python-azure-core >= 1.24.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-ai-language-questionanswering < 1.1.0
%endif
BuildArch:      noarch
%python_subpackages

%description
Question Answering is a cloud-based API service that lets you create a conversational
question-and-answer layer over your existing data. Use it to build a knowledge base
by extracting questions and answers from your semi-structured content, including FAQ,
manuals, and documents. Answer users’ questions with the best answers from the QnAs
in your knowledge base—automatically. Your knowledge base gets smarter, too, as it
continually learns from users' behavior.

%prep
%setup -q -n azure-ai-language-questionanswering-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-language-questionanswering-%{version}
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/azure/ai/language/questionanswering
%{python_sitelib}/azure_ai_language_questionanswering-*.dist-info

%changelog
