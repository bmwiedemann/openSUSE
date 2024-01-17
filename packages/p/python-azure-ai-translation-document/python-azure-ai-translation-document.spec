#
# spec file for package python-azure-ai-translation-document
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


%define realversion 1.0.0

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-ai-translation-document
Version:        1.0.0.0
Release:        0
Summary:        Microsoft Azure Document Translation Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-ai-translation-document/azure-ai-translation-document-%{realversion}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-ai-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-ai-translation-nspkg >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-ai-nspkg >= 1.0.0
Requires:       python-azure-ai-translation-nspkg >= 1.0.0
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.14.0
Requires:       python-msrest >= 0.6.21
Conflicts:      python-azure-sdk <= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Azure Cognitive Services Document Translation is a cloud service that translates documents
to and from 90 languages and dialects while preserving document structure and data format.
Use the client library for Document Translation to:

 * Translate numerous, large files from an Azure Blob Storage container to a target container
   in your language of choice.
 * Check the translation status and progress of each document in the translation operation.
 * Apply a custom translation model or glossaries to tailor translation to your specific case.

%prep
%setup -q -n azure-ai-translation-document-%{realversion}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-ai-translation-document-%{realversion}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/translation/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/translation/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/ai/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/ai/translation/document
%{python_sitelib}/azure_ai_translation_document-*.egg-info

%changelog
