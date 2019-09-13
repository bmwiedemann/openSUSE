#
# spec file for package gloox
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 17
Name:           gloox
Version:        1.0.21
Release:        0
Summary:        High-level XMPP Library for C++
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            http://camaya.net/gloox
Source:         http://camaya.net/download/gloox-%{version}.tar.bz2
Source200:      baselibs.conf
Patch0:         gloox-fix_TLSGnuTLS_test.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel >= 2.12
BuildRequires:  libidn-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
gloox is a portable high-level Jabber/XMPP library for C++. It is fully
compliant with the XMPP RFCs, supports all of the XMPP features (including
SRV lookups, TLS, SASL, roster management, and privacy lists), and implements
several XEPs that make it ideal for writing any kind of Jabber/XMPP client
or component.

%package -n lib%{name}%{soname}
Summary:        High-level XMPP Library for C++
Group:          System/Libraries

%description -n lib%{name}%{soname}
gloox is a portable high-level Jabber/XMPP library for C++. It is fully
compliant with the XMPP RFCs, supports all of the XMPP features (including
SRV lookups, TLS, SASL, roster management, and privacy lists), and implements
several XEPs that make it ideal for writing any kind of Jabber/XMPP client
or component.

%package devel
Summary:        High-level XMPP Library for C++
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}
Requires:       libstdc++-devel

%description devel
gloox is a portable high-level Jabber/XMPP library for C++. It is fully
compliant with the XMPP RFCs, supports all of the XMPP features (including
SRV lookups, TLS, SASL, roster management, and privacy lists), and implements
several XEPs that make it ideal for writing any kind of Jabber/XMPP client
or component.

%prep
%setup -q -n gloox-%{version}
%patch0 -p1

%build
export SUSE_ASNEEDED=0
%configure --enable-shared --disable-static --enable-getaddrinfo
make %{?_smp_mflags}

%install
%make_install

rm -f "%{buildroot}%{_libdir}/libgloox".{a,la}

h=%{_datadir}/doc/licenses/md5/$(md5sum COPYING|cut -f1 -d" ")
test -e "$h" && ln -s -f "$h" COPYING

%check
make %{?_smp_mflags} test

%post   -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files -n lib%{name}%{soname}
%license COPYING
%doc AUTHORS README ChangeLog TODO
%{_libdir}/libgloox.so.%{soname}
%{_libdir}/libgloox.so.%{soname}.*.*

%files devel
%{_bindir}/gloox-config
%{_includedir}/gloox
%{_libdir}/libgloox.so
%{_libdir}/pkgconfig/gloox.pc

%changelog
