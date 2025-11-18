#
# spec file for package libvalkey
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 0
%bcond_without tls
%bcond_without rdma
Name:           libvalkey
Version:        0.2.1
Release:        0
Summary:        Valkey client library in C
License:        BSD-3-Clause
URL:            https://github.com/valkey-io/libvalkey
Source:         https://github.com/valkey-io/libvalkey/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/valkey-io/libvalkey/issues/247
# https://github.com/valkey-io/libvalkey/pull/248
Patch0:         libvalkey-0.2.1-linker-errors.patch
# https://github.com/valkey-io/libvalkey/issues/251
# https://github.com/valkey-io/libvalkey/pull/252/commits/2cb723cb9c7a3831b43f144d3fa38c24a97b962b
Patch1:         libvalkey-0.2.1-32-bit.patch
BuildRequires:  cmake
%if %{with tls}
BuildRequires:  pkgconfig(libcrypto)
%endif
%if %{with rdma}
BuildRequires:  pkgconfig(libibverbs)
BuildRequires:  pkgconfig(librdmacm)
%endif

%description
Libvalkey is the official C client for the Valkey database. It also supports
any server that uses the RESP protocol (version 2 or 3). This project supports
both standalone and cluster modes.

%package -n %{name}%{sover}
Summary:        Valkey client library in C

%description -n %{name}%{sover}
Libvalkey is the official C client for the Valkey database. It also supports
any server that uses the RESP protocol (version 2 or 3). This project supports
both standalone and cluster modes.

This package contains the shared library.

%if %{with tls}
%package -n %{name}_tls%{sover}
Summary:        Valkey client library in C - TLS support

%description -n %{name}_tls%{sover}
Libvalkey is the official C client for the Valkey database. It also supports
any server that uses the RESP protocol (version 2 or 3). This project supports
both standalone and cluster modes.

This package contains the shared library providing TLS support.
%endif

%if %{with rdma}
%package -n %{name}_rdma%{sover}
Summary:        Valkey client library in C - RDMA support

%description -n %{name}_rdma%{sover}
Libvalkey is the official C client for the Valkey database. It also supports
any server that uses the RESP protocol (version 2 or 3). This project supports
both standalone and cluster modes.

This package contains the shared library providing RDMA support.
%endif

%package devel
Summary:        Valkey client library in C
Requires:       %{name}%{sover} = %{version}
%if %{with tls}
Requires:       %{name}_tls%{sover} = %{version}
%endif
%if %{with rdma}
Requires:       %{name}_rdma%{sover} = %{version}
%endif

%description devel
Libvalkey is the official C client for the Valkey database. It also supports
any server that uses the RESP protocol (version 2 or 3). This project supports
both standalone and cluster modes.

%prep
%autosetup -p1

%build
%cmake \
	-DDISABLE_TESTS:BOOL=ON \
%if %{with tls}
	-DENABLE_TLS:BOOL=ON \
%endif
%if %{with rdma}
	-DENABLE_RDMA:BOOL=ON \
%endif
	%{nil}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{name}%{sover}
%if %{with tls}
%ldconfig_scriptlets -n %{name}_tls%{sover}
%endif
%if %{with rdma}
%ldconfig_scriptlets -n %{name}_rdma%{sover}
%endif

%files -n %{name}%{sover}
%license COPYING
%{_libdir}/libvalkey.so.%{sover}{,.*}

%if %{with tls}
%files -n %{name}_tls%{sover}
%license COPYING
%{_libdir}/libvalkey_tls.so.%{sover}{,.*}
%endif

%if %{with rdma}
%files -n %{name}_rdma%{sover}
%license COPYING
%{_libdir}/libvalkey_rdma.so.%{sover}{,.*}
%endif

%files devel
%license COPYING
%doc README.md
%{_includedir}/valkey
%{_libdir}/libvalkey.so
%{_libdir}/pkgconfig/valkey.pc
%{_libdir}/cmake/valkey
%if %{with tls}
%{_libdir}/libvalkey_tls.so
%{_libdir}/pkgconfig/valkey_tls.pc
%{_libdir}/cmake/valkey_tls
%endif
%if %{with rdma}
%{_libdir}/libvalkey_rdma.so
%{_libdir}/pkgconfig/valkey_rdma.pc
%{_libdir}/cmake/valkey_rdma
%endif

%changelog
