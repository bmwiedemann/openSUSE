#
# spec file for package python-drgn
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


%define skip_python2 1

%{?!python_module:%define python_module() python3-%{**}}

Name:           python-drgn
Version:        0.0.30
Release:        0
Summary:        Scriptable debugger library
License:        LGPL-2.1-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/osandov/drgn
Source:         https://github.com/osandov/drgn/archive/refs/tags/v%{version}.tar.gz#/drgn-%{version}.tar.gz
Patch1:         libdrgn-kdump-simplify-getting-the-PRSTATUS-attribut.patch
Patch2:         libdrgn-kdump-prepare-for-incompatible-changes-in-li.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  fdupes
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libkdumpfile-devel
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
drgn (pronounced “dragon”) is a debugger with an emphasis on
programmability. drgn exposes the types and variables in a program
for easy, expressive scripting in Python.

%prep
%setup -q -n drgn-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/drgn
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%post
%python_install_alternative drgn

%postun
%python_uninstall_alternative drgn

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/drgn
%{python_sitearch}/drgn
%{python_sitearch}/drgn-%{version}*-info
%{python_sitearch}/_drgn*.pyi
%{python_sitearch}/_drgn*.so
%{python_sitearch}/_drgn_util

%changelog
