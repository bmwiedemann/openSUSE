#
# spec file for package python-pathable
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


%{?sle15_python_module_pythons}
Name:           python-pathable
Version:        0.4.4
Release:        0
Summary:        Object-oriented paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/pathable
Source:         https://github.com/p1c2u/pathable/archive/refs/tags/%{version}.tar.gz#/pathable-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# I know self obsoletion, but se want following, right?
# Unfortunately dictpath v. 0.4.3 exists
# change <= to < 0.4.4 as soon as 0.4.4 is out
Obsoletes:      python-dictpath <= 0.4.3
Provides:       python-dictpath = 0.4.3
BuildArch:      noarch
%python_subpackages

%description
Python object-oriented paths.

%prep
%setup -q -n pathable-%{version}
sed -i '/--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pathable
%{python_sitelib}/pathable-%{version}.dist-info

%changelog
