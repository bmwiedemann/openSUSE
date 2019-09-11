#
# spec file for package python-dennis
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
Name:           python-dennis
Version:        0.9
Release:        0
Summary:        Utilities for working with PO and POT files
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/willkg/dennis
Source:         https://files.pythonhosted.org/packages/source/d/dennis/dennis-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test runner
BuildRequires:  %{python_module pytest}
# Module dependencies
BuildRequires:  %{python_module click >= 6}
BuildRequires:  %{python_module polib >= 1.0.8}
Requires:       python-click >= 6
Requires:       python-polib >= 1.0.8
BuildArch:      noarch

%python_subpackages

%description
Dennis is a set of utilities for working with PO files. They
translate POT files to find problems with localization in code, and
lint PO files for common problems like variable formatting,
mismatched HTML, missing variables, etc.

%prep
%setup -q -n dennis-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF-8"
%python_expand pytest-%{$python_bin_suffix} tests

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%python3_only %{_bindir}/dennis-cmd
%{python_sitelib}/*

%changelog
