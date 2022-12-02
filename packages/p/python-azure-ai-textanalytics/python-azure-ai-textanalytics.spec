#
# spec file for package python-azure-ai-textanalytics
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-ai-textanalytics
Version:        5.2.1
Release:        0
Summary:        Azure Text Analytics client library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-textanalytics/azure-ai-textanalytics-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-azure-common < 2.0.0
Requires:       python-azure-common >= 1.1
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.24.0
Requires:       python-msrest >= 0.7.0
Requires:       python-typing_extensions >= 4.0.1
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Text Analytics is a cloud-based service that provides advanced natural language
processing over raw text, and includes six main functions:

* Sentiment Analysis
* Named Entity Recognition
* Personally Identifiable Information (PII) Entity Recognition
* Linked Entity Recognition
* Language Detection
* Key Phrase Extraction

%prep
%setup -q -n azure-ai-textanalytics-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-textanalytics-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/textanalytics
%{python_sitelib}/azure_ai_textanalytics-*.egg-info

%changelog
