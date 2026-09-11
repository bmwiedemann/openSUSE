#
# spec file for package nng
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2018-2026, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
Name:           nng
Version:        1.12.2
Release:        0
Summary:        Nanomsg NG - brokerless messaging
License:        MIT
URL:            https://nanomsg.github.io/nng/
Source:         https://github.com/nanomsg/nng/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
nng (nanomsg next-generation) is a C socket library providing
several common communication patterns.

%package -n libnng%{sover}
Summary:        Shared library for nng

%description -n libnng%{sover}
nng (nanomsg next-generation) is a C socket library providing
several common communication patterns.

%package devel
Summary:        Header files for nng
# nngcat lived in -devel before the split, so -devel must keep pulling it.
# Hard dep rather than Recommends: OBS does not install recommends into the
# build root, so a Recommends would make it differ from a system install.
Requires:       %{name}-utils = %{version}
Requires:       libnng%{sover} = %{version}

%description devel
Development and header files for nng (nanomsg next-generation).

%package utils
Summary:        Command line access to Scalability Protocols
Requires:       libnng%{sover} = %{version}

%description utils
nngcat, a command line tool that sends and receives messages over nng
(nanomsg next-generation) sockets.  It speaks every Scalability Protocol
the library implements, which makes it useful for probing, testing and
debugging applications built on nng.

%prep
%autosetup

%build
%cmake \
    -DNNG_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
# The %%ctest macro takes no extra flags, so drive ctest directly.  Restricted
# to the offline unit tests: the transport, protocol, nngcat and stress tests
# bind fixed loopback ports, and resolver_test/tcp_test/httpclient need public
# DNS and httpbin.org, so they cannot gate a build worker.  The selected set
# covers the URL/HTTP message parsing fixed in 1.12.1.
# reconnect_test is excluded on top of that: test_reconnect_back_off_zero
# gives listen+send+recv a hard 100 ms budget (NUTS_BEFORE at
# reconnect_test.c:154), which a slow worker misses - it flipped red on half
# the s390x builds of an unchanged source tree.
# Offline is not the same as deterministic: aio_test keeps upper bounds of
# 500-1000 ms (upstream itself skips two of them off GitHub macOS), so it is
# the next candidate if s390x flakes again.
ctest --test-dir %{__builddir} --output-on-failure --force-new-ctest-process -j1 \
    -R "^nng\.(core|supplemental)\." -E "^nng\.core\.reconnect_test$"

%ldconfig_scriptlets -n libnng%{sover}

%files -n libnng%{sover}
%doc README.adoc
%license LICENSE.txt
%{_libdir}/libnng.so.*

%files devel
%{_includedir}/nng
%{_libdir}/libnng.so
%{_libdir}/cmake/nng/

%files utils
%license LICENSE.txt
%{_bindir}/nngcat

%changelog
