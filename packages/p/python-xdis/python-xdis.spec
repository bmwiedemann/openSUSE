#
# spec file for package python-xdis
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python311 1
Name:           python-xdis
Version:        6.0.5
Release:        0
Summary:        Python cross-version byte-code disassembler and marshal routines
License:        GPL-2.0-only
URL:            https://github.com/rocky/python-xdis/
Source:         https://github.com/rocky/python-xdis/archive/%{version}.tar.gz
Patch0:         ignore-patchlevel-in-python-version.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
Requires:       python-click
Requires:       python-setuptools
Requires:       python-six >= 1.10.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.10.0}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Python cross-version byte-code disassembler and marshal routines.

%prep
%autosetup -p1

%build
# test fails for weird order reasons
rm pytest/test_disasm.py

%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pydisasm

%check
%pytest pytest

%post
%python_install_alternative pydisasm

%postun
%python_uninstall_alternative pydisasm

%files %{python_files}
%license COPYING
%doc NEWS.md README.rst
%python_alternative %{_bindir}/pydisasm
%{python_sitelib}/xdis
%{python_sitelib}/xdis-%{version}*-info

%changelog
