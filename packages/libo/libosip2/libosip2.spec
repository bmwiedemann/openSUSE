#
# spec file for package libosip2
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


%define sover 15
Name:           libosip2
Version:        5.3.1
Release:        0
Summary:        Implementation of SIP (RFC 3261)
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://www.gnu.org/software/osip/osip.html
Source:         https://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=3960#/%{name}.keyring
BuildRequires:  docbook2x
BuildRequires:  gperf
BuildRequires:  pkgconfig

%description
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n %{name}-%{sover}
Summary:        Implementation of SIP (RFC 3261)
Group:          System/Libraries

%description -n %{name}-%{sover}
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package devel
Summary:        Header files for the GNU SIP implementation
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{sover} = %{version}
Requires:       glibc-devel
Provides:       libosip2:%{_includedir}/osip2/osip.h

%description devel
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%prep
%setup -q

%build
%configure \
  --enable-pthread \
  --enable-mt \
  --enable-gperf \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%files -n %{name}-%{sover}
%license COPYING
%{_libdir}/lib*.so.%{sover}{,.*}

%files devel
%license COPYING
%doc HISTORY NEWS README FEATURES BUGS AUTHORS ChangeLog
%{_includedir}/osipparser2
%{_includedir}/osip2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libosip2.pc
%{_mandir}/man1/*

%changelog
