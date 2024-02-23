#
# spec file for package python-pydocumentdb
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


%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-pydocumentdb
Version:        2.3.5
Release:        0
Summary:        Azure DocumentDB Python SDK
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-documentdb-python
Source:         https://files.pythonhosted.org/packages/source/p/pydocumentdb/pydocumentdb-%{version}.tar.gz
Patch0:         p_disable-changelog-parsing.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.10.0
Requires:       python-six >= 1.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.10.0}
BuildRequires:  %{python_module six >= 1.6}
# /SECTION
%python_subpackages

%description
This is the Microsoft Azure Cosmos DB Python SDK.

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.

%prep
%autosetup -p1 -n pydocumentdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Do not ship docs configuration as a module
%python_expand rm -r %{buildroot}%{$python_sitelib}/doc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/pydocumentdb
%{python_sitelib}/pydocumentdb-%{version}.dist-info

%changelog
