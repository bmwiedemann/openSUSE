#
# spec file for package python-pingparsing
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
%define skip_python2 1
Name:           python-pingparsing
Version:        1.0.1
Release:        0
Summary:        CLI-tool/Python-library for parsing ping command output
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/pingparsing
Source:         https://github.com/thombashi/pingparsing/archive/v%{version}.tar.gz#/pingparsing-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-humanreadable >= 0.0.7
Requires:       python-loguru >= 0.4.1
Requires:       python-pyparsing >= 2.0.3
Requires:       python-setuptools >= 38.3.0
Requires:       python-six >= 1.10.0
Requires:       python-subprocrunner >= 0.17.0
Requires:       python-typepy >= 0.6.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Logbook >= 0.12.3}
BuildRequires:  %{python_module humanreadable >= 0.0.7}
BuildRequires:  %{python_module pyparsing >= 2.0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module subprocrunner >= 0.17.0}
BuildRequires:  %{python_module typepy >= 0.6.3}
# /SECTION
%python_subpackages

%description
pingparsing is a CLI-tool/Python-library for parsing ping command output.

%prep
%setup -q -n pingparsing-%{version}
sed -i -e '/^#!\//, 1d' pingparsing/cli.py

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/pingparsing
%{python_sitelib}/pingparsing*

%changelog
