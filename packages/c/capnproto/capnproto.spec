#
# spec file for package capnproto
#
# Copyright (c) 2022 SUSE LLC
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


%define _libver 0_10_3
Name:           capnproto
Version:        0.10.3
Release:        0
Summary:        A Data Serialization Format
License:        MIT
URL:            https://capnproto.org
Source:         https://capnproto.org/capnproto-c++-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7-c++
%endif
BuildRequires:  pkgconfig
Requires:       libcapnp-%{_libver} = %{version}

%description
Cap'n Proto is a binary data interchange format and capability-based
RPC system.

%package     -n libcapnp-%{_libver}
Summary:        The Cap'n Proto data serialization library
Conflicts:      libcapnp-0_9 = 0.9.1

%description -n libcapnp-%{_libver}
Cap'n Proto is a binary data interchange format and capability-based
RPC system.

This package provides runtime libraries for capnproto.

%package     -n libcapnp-devel
Summary:        Development headers for the Cap'n Proto C++ Library
Requires:       libcapnp-%{_libver} = %{version}

%description -n libcapnp-devel
Cap'n Proto is a binary data interchange format and capability-based
RPC system.

This package provides development headers for capnproto.

%prep
%autosetup -n %{name}-c++-%{version}

%build
export CXX=g++
test -x "$(type -p g++-7)" && export CXX=g++-7
%configure
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f \( -name "*.a" -o -name "*.la" \) -delete -print

%post -n libcapnp-%{_libver} -p /sbin/ldconfig
%postun -n libcapnp-%{_libver} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/capnp
%{_bindir}/capnpc
%{_bindir}/capnpc-c++
%{_bindir}/capnpc-capnp

%files -n libcapnp-%{_libver}
%{_libdir}/libcapnp-%{version}.so
%{_libdir}/libcapnp-rpc-%{version}.so
%{_libdir}/libcapnpc-%{version}.so
%{_libdir}/libcapnp-json-%{version}.so
%{_libdir}/libcapnp-websocket-%{version}.so
%{_libdir}/libkj-test-%{version}.so
%{_libdir}/libkj-%{version}.so
%{_libdir}/libkj-async-%{version}.so
%{_libdir}/libkj-http-%{version}.so

%files -n libcapnp-devel
%{_includedir}/capnp
%{_includedir}/kj
%{_libdir}/libcapnp-rpc.so
%{_libdir}/libcapnp.so
%{_libdir}/libcapnpc.so
%{_libdir}/libcapnp-json.so
%{_libdir}/libcapnp-websocket.so
%{_libdir}/libkj-test.so
%{_libdir}/libkj-async.so
%{_libdir}/libkj-http.so
%{_libdir}/libkj.so
%dir %{_libdir}/cmake/CapnProto
%{_libdir}/cmake/CapnProto/CapnProtoConfig.cmake
%{_libdir}/cmake/CapnProto/CapnProtoConfigVersion.cmake
%{_libdir}/cmake/CapnProto/CapnProtoMacros.cmake
%{_libdir}/cmake/CapnProto/CapnProtoTargets.cmake
%{_libdir}/pkgconfig/capnp.pc
%{_libdir}/pkgconfig/capnpc.pc
%{_libdir}/pkgconfig/capnp-json.pc
%{_libdir}/pkgconfig/capnp-rpc.pc
%{_libdir}/pkgconfig/capnp-websocket.pc
%{_libdir}/pkgconfig/kj-async.pc
%{_libdir}/pkgconfig/kj-gzip.pc
%{_libdir}/pkgconfig/kj-http.pc
%{_libdir}/pkgconfig/kj-test.pc
%{_libdir}/pkgconfig/kj-tls.pc
%{_libdir}/pkgconfig/kj.pc

%changelog
