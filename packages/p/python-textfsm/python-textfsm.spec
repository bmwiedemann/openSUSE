#
# spec file for package python-textfsm
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


%{?sle15_python_module_pythons}
Name:           python-textfsm
Version:        1.1.3
Release:        0
Summary:        Python module for parsing semi-structured text into python tables
License:        Apache-2.0
URL:            https://github.com/google/textfsm
Source:         https://github.com/google/textfsm/archive/v%{version}.tar.gz#/textfsm-%{version}.tar.gz
# PATCH-FIX-OPENSUSE https://github.com/google/textfsm/issues/118
Patch0:         correct-version.patch
# https://github.com/google/textfsm/commit/c8843d69daa9b565fea99a0283ad13c324d5b563
Patch1:         python-textfsm-no-python2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%prep
%autosetup -p1 -n textfsm-%{version}
# drop shebang
sed -i -e '/^#!\//, 1d' textfsm/*.py

%build
%pyproject_wheel

%install
%pyproject_install
# don't install broken textfsm wrapper binary
%python_expand rm -f %{buildroot}%{_bindir}/textfsm
# or the testdata
%python_expand rm -r %{buildroot}%{$python_sitelib}/testdata
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/textfsm
%{python_sitelib}/textfsm-%{version}.dist-info

%changelog
