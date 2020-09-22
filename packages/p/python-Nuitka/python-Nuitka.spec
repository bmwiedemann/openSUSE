#
# spec file for package python-Nuitka
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
Name:           python-Nuitka
Version:        0.6.8.4
Release:        0
Summary:        Python compiler with full language support and CPython compatibility
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://nuitka.net
Source:         https://files.pythonhosted.org/packages/source/N/Nuitka/Nuitka-%{version}.tar.gz
Source1:        nuitka-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  scons
Requires:       gcc-c++
Requires:       python-appdirs
Requires:       python-devel
Requires:       scons
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     chrpath
Recommends:     clang
Recommends:     strace
Suggests:       execstack
Suggests:       gdb
BuildArch:      noarch
# SECTION Testing requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module xml}
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  gdb
BuildRequires:  strace
# TkInter failing, so avoid the extra heavy build dep
# https://github.com/Nuitka/Nuitka/issues/811
# BuildRequires:  tk
# BuildRequires:  %%{python_module tk}
# https://github.com/Nuitka/Nuitka/issues/810
#BuildRequires:  %%{python_module pmw}
# moto currently failing to build
#BuildRequires:  %%{python_module moto}
#BuildRequires:  %%{python_module boto3}
# pyside2 has working tests, however it exists on few arch
#BuildRequires:  python3-pyside2
# /SECTION Testing requirements
%python_subpackages

%description
Python compiler with full language support and CPython compatibility.

This Python compiler achieves full language compatibility and compiles Python
code into compiled objects that are not second class at all. Instead they can be
used in the same way as pure Python objects.

%prep
%setup -q -n Nuitka-%{version}
# De-vendor
rm -r nuitka/build/inline_copy/appdirs/
rm -r nuitka/build/inline_copy/pefile/
# SCons has copies here that are automatically excluded, but remove them to be sure
rm -r nuitka/build/inline_copy/lib/
rm -r nuitka/build/inline_copy/bin/

sed -i '1{/^#!/d}' nuitka/tools/testing/*/__main__.py nuitka/tools/general/dll_report/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_mandir}/man1
gzip -c doc/nuitka.1 > %{buildroot}%{_mandir}/man1/nuitka.1.gz
gzip -c doc/nuitka-run.1 > %{buildroot}%{_mandir}/man1/nuitka-run.1.gz

mv %{buildroot}%{_bindir}/nuitka3 %{buildroot}%{_bindir}/nuitka
%python_clone -a %{buildroot}%{_bindir}/nuitka
%python_clone -a %{buildroot}%{_mandir}/man1/nuitka.1.gz
mv %{buildroot}%{_bindir}/nuitka3-run %{buildroot}%{_bindir}/nuitka-run
%python_clone -a %{buildroot}%{_bindir}/nuitka-run
%python_clone -a %{buildroot}%{_mandir}/man1/nuitka-run.1.gz

%check
export TCL_LIBRARY=%{_libdir}/tcl/tcl8.6
export TK_LIBRARY=%{_libdir}/tcl/tk8.6
# Force using clang https://github.com/Nuitka/Nuitka/issues/809
export CC=clang

# https://github.com/Nuitka/Nuitka/issues/811
mv tests/standalone/SocketUsing.py tests/standalone/TkInterUsing.py /tmp

# Reflection tests are very time consuming and not helpful for smoke tests

%python_exec ./tests/run-tests --skip-reflection-test --no-other-python

mv /tmp/SocketUsing.py /tmp/TkInterUsing.py tests/standalone/

%post
%python_install_alternative nuitka nuitka.1 nuitka-run nuitka-run.1

%postun
%python_uninstall_alternative nuitka

%files %{python_files}
%doc Changelog.rst README.rst Developer_Manual.rst
%license LICENSE.txt
%{python_sitelib}/*
%python_alternative %{_bindir}/nuitka-run
%python_alternative %{_bindir}/nuitka
%python_alternative %{_mandir}/man1/nuitka.1
%python_alternative %{_mandir}/man1/nuitka-run.1

%changelog
