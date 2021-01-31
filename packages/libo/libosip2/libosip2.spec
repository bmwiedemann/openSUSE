#
# spec file for package libosip2
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


%define soname libosip2-12
Name:           libosip2
Version:        5.2.0
Release:        0
Summary:        Implementation of SIP (RFC 3261)
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://www.gnu.org/software/osip/osip.html
Source:         https://ftp.gnu.org/gnu/osip/libosip2-5.2.0.tar.gz
Patch0:         libosip2-5.0.0.patch
BuildRequires:  docbook2x
BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n %{soname}
Summary:        Implementation of SIP (RFC 3261)
Group:          System/Libraries

%description -n %{soname}
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package devel
Summary:        Header files for the GNU SIP implementation
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       glibc-devel
Provides:       libosip2:%{_includedir}/osip2/osip.h

%description devel
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%prep
%setup -q
%patch0

%build
autoreconf -fiv
%configure \
  --enable-pthread \
  --enable-mt \
  --enable-sysv \
  --enable-gperf \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/osipparser2
%{_includedir}/osip2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libosip2.pc
%{_mandir}/man1/*

%changelog
