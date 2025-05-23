#
# spec file for package python-azure-cognitiveservices-language-nspkg
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
Name:           python-azure-cognitiveservices-language-nspkg
Version:        3.0.1
Release:        0
Summary:        Microsoft Azure Cognitive Services Language namespace package
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-cognitiveservices-language-nspkg/azure-cognitiveservices-language-nspkg-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-cognitiveservices-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-cognitiveservices-nspkg >= 3.0.0
Requires:       python-azure-nspkg >= 3.0.0
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-cognitiveservices-language-nspkg <= 3.0.1
%endif
BuildArch:      noarch

%python_subpackages

%description
This is the Microsoft Azure Cognitive Services Language namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure.cognitiveservices.language namespace.

%prep
%setup -q -n azure-cognitiveservices-language-nspkg-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-cognitiveservices-language-nspkg-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand mkdir -p %{buildroot}%{$python_sitelib}/azure/cognitiveservices/language

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/azure/cognitiveservices/language
%{python_sitelib}/azure_cognitiveservices_language_nspkg-*.dist-info

%changelog
