#
# spec file for package libfaketime
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


# LTO: fixed upstream after 0.9.13, gh#wolfcw/libfaketime#557
%define _lto_cflags %{nil}
Name:           libfaketime
Version:        0.9.13
Release:        0
Summary:        FakeTime Preload Library
License:        GPL-2.0-only
URL:            https://github.com/wolfcw/libfaketime
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-NULL-contract-tests.patch gh#wolfcw/libfaketime#555
Patch0:         remove-NULL-contract-tests.patch
BuildRequires:  bash
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl

%description
Report faked system time to programs without having to change the system-wide time.

%prep
%autosetup -p1

%build
%ifarch ppc64le
export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif
%{set_build_flags}
%make_build PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}

%install
%make_install PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}
chmod -c 0755 %{buildroot}%{_libdir}/%{name}/libfaketime*.so.1
rm -r %{buildroot}%{_datadir}/doc/faketime

%check
%ifarch ppc64le
export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif
%ifarch riscv64
export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif
# -j1: the test 'all' target runs the suite while helpers still build
%make_build -j1 PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name} -C test

%files
%doc NEWS README
%license COPYING
%{_bindir}/faketime
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libfaketime.so.1
%{_libdir}/%{name}/libfaketimeMT.so.1
%{_mandir}/man1/faketime.1%{?ext_man}

%changelog
