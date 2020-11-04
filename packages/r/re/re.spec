#
# spec file for package re
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

# using 0suse0 instead of suse0 due to a bug in rpmlint/post-build-checks
# falsely complaining about name
%global sover   0suse0
%global libname lib%{name}%{sover}
Name:           re
Version:        0.6.1
Release:        0
Summary:        Library for real-time communications with async IO support
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
#Git-Clone:     https://github.com/creytiv/re
URL:            http://www.creytiv.com/re.html
Source:         http://www.creytiv.com/pub/re-%{version}.tar.gz
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
    EXTRA_CFLAGS="%optflags" \
    EXTRA_LFLAGS="-Wl,-soname,libre.so.0suse0" \
    LIB_SUFFIX=".so.0suse0"

%install
make DESTDIR=%{buildroot} LIBDIR=%{_libdir} LIB_SUFFIX=".so.0suse0" install
ln -s %{_libdir}/libre.so.0suse0 %{buildroot}%{_libdir}/libre.so
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
