#
# spec file for package python-pingparsing
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
Name:           python-pingparsing
Version:        1.4.2
Release:        0
Summary:        CLI-tool/Python-library for parsing ping command output
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/pingparsing
Source:         https://github.com/thombashi/pingparsing/archive/v%{version}.tar.gz#/pingparsing-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-humanreadable >= 0.3
Requires:       python-loguru >= 0.4.1
Requires:       python-pyparsing >= 2.0.3
Requires:       python-pytz >= 2018.9
Requires:       python-setuptools >= 38.3.0
Requires:       python-simplejson
Requires:       python-subprocrunner >= 1.2.2
Requires:       python-typepy >= 1.3.2
Requires(post): alts
Requires(postun): alts
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module humanreadable >= 0.3}
BuildRequires:  %{python_module pyparsing >= 2.0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2018.9}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module subprocrunner >= 1.2.2}
BuildRequires:  %{python_module typepy >= 1.3.2}
# /SECTION
%python_subpackages

%description
pingparsing is a CLI-tool/Python-library for parsing ping command output.

%prep
%autosetup -p1 -n pingparsing-%{version}
sed -i -e '/^#!\//, 1d' pingparsing/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pingparsing
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pingparsing

%postun
%python_uninstall_alternative pingparsing

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pingparsing
%{python_sitelib}/pingparsing*

%changelog
