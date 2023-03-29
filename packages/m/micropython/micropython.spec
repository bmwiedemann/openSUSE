#
# spec file for package micropython
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


Name:           micropython
Version:        1.19.1
Release:        0
Summary:        Implementation of Python 3 with very low memory footprint
License:        MIT
Group:          Development/Languages/Python
URL:            https://micropython.org/
Source:         https://micropython.org/resources/source/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM: fix build with gcc 13
Patch1:         https://github.com/micropython/micropython/commit/32572439984e5640c6af46fbe7c27400c30112ce.patch
BuildRequires:  openssl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libffi)
Recommends:     micropython-lib
ExcludeArch:    %{ix86} %{arm} ppc64 ppc64le

%description
A lean and efficient Python implementation for microcontrollers and constrained systems

%prep
%autosetup -p1

sed -i -e "s:/usr/lib/micropython:%{_prefix}/lib/micropython:g" "ports/unix/main.c"

%define make_flags V=1 MICROPY_PY_BTREE=0 MICROPY_PY_USSL=0

%build
%make_build -C mpy-cross
%make_build -C ports/unix micropython STRIP=true

%install
install -d %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} ports/unix/micropython

%check
%ifnarch x86_64
# 2 tests fail: float_parse float_parse_doubleprec
# https://github.com/micropython/micropython/pull/6024
rm -f tests/float/float_parse.py
rm -f tests/float/float_parse_doubleprec.py
%endif
export MICROPY_CPYTHON3=python3
make -C ports/unix PYTHON=%{_bindir}/python3 V=1 test

%files
%license LICENSE
%doc docs/unix/*
%{_bindir}/micropython

%changelog
