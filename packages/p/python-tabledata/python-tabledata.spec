#
# spec file for package python-tabledata
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-tabledata
Version:        1.3.4
Release:        0
Summary:        Python library to represent tabular data
License:        MIT
URL:            https://github.com/thombashi/tabledata
Source:         https://files.pythonhosted.org/packages/source/t/tabledata/tabledata-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
## SECTION test requirements
BuildRequires:  %{python_module DataProperty >= 1.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typepy >= 1.2.0}
## /SECTION
Requires:       python-DataProperty >= 1.0.1
Requires:       python-typepy >= 1.2.0
BuildArch:      noarch
%python_subpackages

%description
tabledata is a Python library to represent tabular data.

%prep
%setup -q -n tabledata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tabledata
%{python_sitelib}/tabledata-%{version}.dist-info

%changelog
