#
# spec file for package python-azure-template
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
Name:           python-azure-template
Version:        0.1.0b3920641
Release:        0
Summary:        Microsoft Azure Template Package Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-template/azure-template-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-azure-core >= 1.23.0 with python-azure-core < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-template < 0.1.0b3511266
%endif
BuildArch:      noarch

%python_subpackages

%description
This template package matches necessary patterns that the development team has established to
create a unified sdk functional from Python 2.7 onwards. The packages contained herein can be
installed singly or as part of the azure namespace.

This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8

%prep
%setup -q -n azure-template-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-template-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/template
%{python_sitelib}/azure_template-*.dist-info

%changelog
