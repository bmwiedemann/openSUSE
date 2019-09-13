#
# spec file for package python-pydocumentdb
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
Name:           python-pydocumentdb
Version:        2.3.3
Release:        0
Summary:        Azure DocumentDB Python SDK
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-documentdb-python
Source:         https://files.pythonhosted.org/packages/source/p/pydocumentdb/pydocumentdb-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n pydocumentdb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand py.test-%{$python_version}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
