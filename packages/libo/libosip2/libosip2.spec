#
# spec file for package libosip2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libosip2
Version:        5.0.0
Release:        0
Summary:        Implementation of SIP--RFC 3261
License:        LGPL-2.1+
Group:          Productivity/Networking/Other
Url:            http://www.fsf.org/software/osip/osip.html
Source:         http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         libosip2-5.0.0.patch
Patch1:         SIP_body_len_underflow.patch
BuildRequires:  docbook2x
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package devel
Summary:        Implementation of SIP--RFC 3261
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Provides:       libosip2:/usr/include/osip2/osip.h

%description devel
This is the GNU oSIP library. It has been designed to provide the
Internet community with a simple way to support the Session Initiation
Protocol. SIP is described in the RFC 3261, which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%prep
%setup -q
%patch0
%patch1 -p2

%build
%if 0%{?suse_version} >= 1300
# autotools on sle11 are to old for this
autoreconf -fiv
%endif
%configure \
  --enable-pthread \
  --enable-mt \
  --enable-sysv \
  --enable-gperf \
  --disable-static \
  --with-pic
make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/osipparser2
%{_includedir}/osip2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libosip2.pc
%{_mandir}/man1/*

%changelog
