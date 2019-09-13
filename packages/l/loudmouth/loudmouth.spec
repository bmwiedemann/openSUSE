#
# spec file for package loudmouth
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           loudmouth
Version:        1.5.3
Release:        0
Summary:        Jabber Client Library Written in C
License:        LGPL-2.1+
Group:          Productivity/Networking/Other
Url:            https://github.com/mcabber/loudmouth
Source:         https://mcabber.com/files/loudmouth/%{name}-%{version}.tar.bz2
BuildRequires:  check-devel
BuildRequires:  openssl-devel
BuildRequires:  gtk-doc
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  sgml-skel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libidn)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define debug_package_requires libloudmouth-1-0 = %{version}-%{release}

%description
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It is designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package -n libloudmouth-1-0
Summary:        Jabber Client Library Written in C
Group:          Productivity/Networking/Other

%description -n libloudmouth-1-0
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It is designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package devel
Summary:        Jabber Client Library Written in C
Group:          Productivity/Networking/Other
Requires:       libloudmouth-1-0 = %{version}

%description devel
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It's designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%package doc
Summary:        Jabber Client Library Written in C
Group:          Productivity/Networking/Other
Requires:       libloudmouth-1-0 = %{version}

%description doc
Loudmouth is a lightweight and easy-to-use C library for programming
with the Jabber protocol. It's designed to be easy to get started with
and yet extensible to let you do anything the Jabber protocol allows.

%prep
%setup -q

%build
%configure\
	--disable-static \
	--with-ssl=openssl \
	--enable-gtk-doc-html \
	--enable-gtk-doc
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libloudmouth-1-0 -p /sbin/ldconfig

%postun -n libloudmouth-1-0 -p /sbin/ldconfig

%files -n libloudmouth-1-0
%defattr (-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/loudmouth-1.0

%files doc
%defattr (-, root, root)
%{_datadir}/gtk-doc/html/loudmouth

%changelog
