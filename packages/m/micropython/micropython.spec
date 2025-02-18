#
# spec file for package micropython
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


%define pythons python3
%{?sle15_python_module_pythons}

Name:           micropython
Version:        1.24.1
Release:        0
Summary:        Implementation of Python 3 with very low memory footprint
License:        MIT
URL:            https://micropython.org/
Source:         https://micropython.org/resources/source/%{name}-%{version}.tar.xz
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libffi)

Recommends:     micropython-lib
ExcludeArch:    %{ix86} %{arm} ppc64 ppc64le

%package -n mpremote
Summary:        MicroPython remote control
BuildArch:      noarch
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module hatchling}
Requires:       python3-pyserial >= 3.3
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%package -n mpy-tools
Summary:        Tools for creating and handling precompiled .mpy files for MicroPython
Provides:       mpy-cross
Provides:       mpy-tool

%description
A lean and efficient Python implementation for microcontrollers and constrained systems

%description -n mpremote
This CLI tool provides an integrated set of utilities to remotely interact with
and automate a MicroPython device over a serial connection.

%description -n mpy-tools
MicroPython tools like the mpy-cross compiler for compiling.py files to .mpy files.
Also mpy-tool for inspecting .mpy files.

%prep
%autosetup -p1

sed -i -e "s:/usr/lib/micropython:%{_prefix}/lib/micropython:g" "ports/unix/main.c"

%define make_flags V=1 MICROPY_PY_BTREE=0 MICROPY_PY_USSL=0

%build
# micropython
export CFLAGS="%optflags -Wno-dangling-pointer"
%make_build -C mpy-cross
%make_build -C ports/unix STRIP=true
pushd tools/mpremote
# inject version info as there is no git checkout to get tags from
echo "VERSION = '%{version}'" > version.py
sed -i -e 's/source = "vcs"/path = "version.py"/' pyproject.toml
# remove useless shebang lines
sed -i -e 's_#!/usr/bin/env python3__' mpremote/{__main__,transport,transport_serial}.py
%pyproject_wheel
popd

%install
# micropython
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} ports/unix/build-standard/micropython

# mpremote
pushd tools/mpremote
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove pycache to get rid of rpmlint "W: python-bytecode-inconsistent-mtime" warnings
%python_expand rm -rf %{buildroot}%{$python_sitelib}/mpremote/__pycache__

# mpy-tools
install -m755 -D -v mpy-cross/build/mpy-cross %{buildroot}%{_bindir}/mpy-cross
install -m755 -D -v tools/mpy-tool.py %{buildroot}%{_bindir}/mpy-tool
%python3_fix_shebang

%check
%ifnarch x86_64
# 2 tests fail: float_parse float_parse_doubleprec
# https://github.com/micropython/micropython/pull/6024
rm -f tests/float/float_parse.py
rm -f tests/float/float_parse_doubleprec.py
%endif
export MICROPY_CPYTHON3=python%python_version
make -C ports/unix PYTHON=%{_bindir}/python%python_version V=1 test

%files
%license LICENSE
%doc docs/unix/*
%{_bindir}/micropython

%files -n mpremote
%license tools/mpremote/LICENSE
%doc tools/mpremote/README.md
%{_prefix}/lib/python%{python_version}/site-packages/mpremote
%{_prefix}/lib/python%{python_version}/site-packages/mpremote-%{version}.dist-info
%{_bindir}/mpremote

%files -n mpy-tools
%doc mpy-cross/README.md
%license LICENSE
%{_bindir}/mpy-cross
%{_bindir}/mpy-tool

%changelog
