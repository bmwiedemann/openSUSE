#
# spec file for package python-pingparsing
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pingparsing
Version:        0.18.2
Release:        0
License:        MIT
Summary:        CLI-tool/Python-library for parsing ping command output
Url:            https://github.com/thombashi/pingparsing
Group:          Development/Languages/Python
Source:         https://github.com/thombashi/pingparsing/archive/v%{version}.tar.gz#/pingparsing-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools >= 38.3.0}
# SECTION test requirements
BuildRequires:  %{python_module humanreadable >= 0.0.7}
BuildRequires:  %{python_module Logbook >= 0.12.3}
BuildRequires:  %{python_module pyparsing >= 2.0.3}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module subprocrunner >= 0.17.0}
BuildRequires:  %{python_module typepy >= 0.6.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
BuildRequires:  fdupes
Requires:       python-humanreadable >= 0.0.7
Requires:       python-Logbook >= 0.12.3
Requires:       python-pyparsing >= 2.0.3
Requires:       python-setuptools >= 38.3.0
Requires:       python-six >= 1.10.0
Requires:       python-subprocrunner >= 0.17.0
Requires:       python-typepy >= 0.6.3
BuildArch:      noarch
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
