#
# spec file for package python-drgn
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

%if %{undefined primary_python}
%define primary_python python3
%endif

Name:           python-drgn
Version:        0.0.33
Release:        0
Summary:        Scriptable debugger library
License:        LGPL-2.1-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/osandov/drgn
Source:         drgn-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
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

This package contains the Python module.

%package -n drgn
Summary:        Scriptable debugger CLI
Conflicts:      %{python_module drgn < 0.0.33}
Provides:       %{python_module drgn:/usr/bin/drgn}
Requires:       %{primary_python}-drgn

%description -n drgn
drgn (pronounced “dragon”) is a debugger with an emphasis on
programmability. drgn exposes the types and variables in a program
for easy, expressive scripting in Python.

This package contains the CLI program.

%prep
%setup -q -n drgn-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v

%files %{python_files}
%license COPYING
%{python_sitearch}/drgn
%{python_sitearch}/drgn-%{version}*-info
%{python_sitearch}/_drgn*.pyi
%{python_sitearch}/_drgn*.so
%{python_sitearch}/_drgn_util

%files -n drgn
%doc README.rst
%license COPYING
%{_bindir}/drgn

%changelog
