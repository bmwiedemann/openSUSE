#
# spec file for package loudmouth
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


Name:           loudmouth
Version:        1.5.4
Release:        0
Summary:        Jabber Client Library Written in C
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/mcabber/loudmouth
Source0:        https://mcabber.com/files/loudmouth/%{name}-%{version}.tar.bz2
BuildRequires:  check-devel
# Docs don't build in loudmouth 1.5.4
# BuildRequires:  gtk-doc
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libidn)

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

# %%package doc
# Summary:        Jabber Client Library Written in C
# Group:          Productivity/Networking/Other
# Requires:       libloudmouth-1-0 = %%{version}
# 
# %%description doc
# Loudmouth is a lightweight and easy-to-use C library for programming
# with the Jabber protocol. It's designed to be easy to get started with
# and yet extensible to let you do anything the Jabber protocol allows.

%prep
%setup -q

%build
%configure\
  --with-compile-warnings=yes \
  --disable-static \
  --with-ssl=openssl \
#   --enable-gtk-doc-html \
#   --enable-gtk-doc

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libloudmouth-1-0 -p /sbin/ldconfig
%postun -n libloudmouth-1-0 -p /sbin/ldconfig

%files -n libloudmouth-1-0
%license COPYING
%doc AUTHORS README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/loudmouth-1.0

# %%files doc
# %%{_datadir}/gtk-doc/html/loudmouth

%changelog
