#
# spec file for package python-azure-cognitiveservices-language-textanalytics
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-azure-cognitiveservices-language-textanalytics
Version:        0.1.0
Release:        0
Summary:        Microsoft Azure Cognitive Services Text Analytics Client Library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-cognitiveservices-language-textanalytics/azure-cognitiveservices-language-textanalytics-%{version}.zip
Source1:        LICENSE.txt
Patch1:         aclt_drop-compatible-releases-operator.patch
BuildRequires:  %{python_module azure-cognitiveservices-language-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-cognitiveservices-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-cognitiveservices-language-nspkg >= 3.0.0
Requires:       python-azure-cognitiveservices-nspkg >= 3.0.0
Requires:       python-azure-common < 2.0.0
Requires:       python-azure-common >= 1.1
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest < 2.0.0
Requires:       python-msrest >= 0.4.24
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Cognitive Services Text Analytics Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

%prep
%setup -q -n azure-cognitiveservices-language-textanalytics-%{version}
%patch1 -p1

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cognitiveservices-language-textanalytics-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/language/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/language/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/cognitiveservices/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc HISTORY.rst README.rst
%license LICENSE.txt
%{python_sitelib}/azure/cognitiveservices/language/textanalytics
%{python_sitelib}/azure_cognitiveservices_language_textanalytics-*.egg-info

%changelog
