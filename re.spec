#
# spec file for package re
#
# Copyright (c) 2021 SUSE LLC
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


%global sover   1
%global libname lib%{name}%{sover}
Name:           re
Version:        2.0.1
Release:        0
Summary:        Library for real-time communications with async IO support
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
#Git-Clone:     https://github.com/baresip/re.git
URL:            https://github.com/baresip/re
Source:         https://github.com/baresip/re/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
Libre is a library for real-time communications
with async IO support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

%package -n %{libname}
Summary:        Library for real-time communications with async IO support
Group:          System/Libraries

%description -n %{libname}
Libre is a library for real-time communications
with async IO support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

%package devel
Summary:        Development files for libre
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libre is a portable and generic library for real-time communications
with async IO support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

This subpackage contains libraries and header files for developing
applications that want to make use of libre.

%prep
%setup -q
sed -e 's|@$(CC)|$(CC)|g' \
    -e 's|@$(LD)|$(LD)|g' \
    -e 's|@$(AR)|$(AR)|g' \
    -e 's|@rm -rf|rm -rf|g' -i Makefile

%build
%make_build \
    RELEASE=1 \
    USE_OPENSSL=1 \
    EXTRA_CFLAGS="%optflags"

%install
make DESTDIR=%{buildroot} LIBDIR=%{_libdir} install
rm %{buildroot}/%{_libdir}/libre.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license docs/COPYING
%doc README.md
%{_libdir}/libre.so.%{sover}*

%files devel
%{_includedir}/re
%{_datadir}/re
%{_libdir}/libre.so
%{_libdir}/pkgconfig/libre.pc

%changelog
