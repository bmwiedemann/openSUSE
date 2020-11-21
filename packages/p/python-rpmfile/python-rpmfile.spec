#
# spec file for package python-rpmfile
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-rpmfile
Version:        1.0.4
Release:        0
Summary:        Python module to read rpm files
License:        MIT
URL:            https://github.com/srossross/rpmfile
Source:         https://files.pythonhosted.org/packages/source/r/rpmfile/rpmfile-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-zstandard >= 0.13.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zstandard >= 0.13.0}
# /SECTION
%python_subpackages

%description
Tools for inspecting RPM files in python. This module is modeled after the tarfile module.

%prep
%setup -q -n rpmfile-%{version}
sed -i '1{/#!/d}' rpmfile/cpiofile.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# https://github.com/srossross/rpmfile/issues/35
# test_extract depend on github.com
%pytest -k 'not test_extract'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
