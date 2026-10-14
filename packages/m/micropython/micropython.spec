#
# spec file for package micropython
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# needed if upstream doesn't bundle mbedtls with recent security patches
%define mbedtls_version 3.6.7
%{?sle15_python_module_pythons}
Name:           micropython
Version:        1.29.0
Release:        0
Summary:        Implementation of Python 3 with very low memory footprint
License:        MIT
URL:            https://micropython.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        prepare.sh
Source2:        https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-%{mbedtls_version}/mbedtls-%{mbedtls_version}.tar.bz2#/mbedtls-%{mbedtls_version}.tar.bz2
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libffi)
Recommends:     micropython-lib
ExcludeArch:    %{ix86} %{arm} ppc64 ppc64le

%package -n mpremote
Summary:        MicroPython remote control
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-platformdirs
Requires:       python3-pyserial >= 3.3
BuildArch:      noarch

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
%autosetup -p1 -a2

%define make_flags V=1 MICROPY_PY_BTREE=0 MICROPY_PY_USSL=0

# needed if upstream doesn't bundle mbedtls with recent security patches
rm -rf lib/mbedtls
mv mbedtls-%{mbedtls_version} lib/mbedtls

%build
# micropython
export CFLAGS="%{optflags} -Wno-dangling-pointer"
pwd
ls -l
%make_build -C mpy-cross
%make_build -C ports/unix STRIP=true
pushd tools/mpremote
# inject version info as there is no git checkout to get tags from
echo "VERSION = '%{version}'" > version.py
sed -i -e 's/source = "vcs"/path = "version.py"/' pyproject.toml
# remove useless shebang lines
sed -i -e 's_#!%{_bindir}/env python3__' mpremote/{__main__,transport,transport_serial}.py
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
%{python3_fix_shebang}

%check
%ifnarch x86_64
%endif
export MICROPY_CPYTHON3=python%{python_version}
%make_build -C ports/unix PYTHON=%{_bindir}/python%{python_version} test

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
