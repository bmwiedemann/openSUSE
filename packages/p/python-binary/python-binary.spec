#
# spec file for package python-binary
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-binary
Version:        1.0.0
Release:        0
License:        MIT or Apache-2.0
Summary:        Library to convert between binary and SI units
Url:            https://github.com/ofek/binary
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/b/binary/binary-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Python library to convert between and within binary (IEC) and decimal (SI) units.

%prep
%setup -q -n binary-%{version}
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}/%{$python_sitelib}/tests/

%check
%python_exec setup.py pytest --addopts="--cov=binary.core --cov-fail-under=100 tests"

%files %{python_files}
%doc README.rst
%license LICENSE-APACHE LICENSE-MIT
%{python_sitelib}/*

%changelog
