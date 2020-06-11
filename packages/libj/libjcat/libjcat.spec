#
# spec file for package libjcat
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


%define sover 1

Name:           libjcat
Version:        0.1.2+3
Release:        0
Summary:        Library for reading and writing gzip-compressed JSON catalog files
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/hughsie/libjcat
Source:         %{name}-%{version}.tar.xz
# for certtool
BuildRequires:  gnutls
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  meson >= 0.47.0
BuildRequires:  python3-setuptools
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.45.8
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.1.1

%description
This library allows reading and writing gzip-compressed JSON
catalog files, which can be used to store GPG, PKCS-7 and
SHA-256 checksums for each file. This provides  equivalent
functionality to the catalog files supported in Microsoft Windows.

%package -n %{name}%{sover}
Summary:        Library for reading and writing gzip-compressed JSON catalog files
Group:          System/Libraries

%description -n %{name}%{sover}
This library allows reading and writing gzip-compressed JSON
catalog files, which can be used to store GPG, PKCS-7 and
SHA-256 checksums for each file. This provides  equivalent
functionality to the catalog files supported in Microsoft Windows.

%package -n typelib-1_0-Jcat-1_0
Summary:        Introspection bindings for %{name}
Group:          System/Libraries

%description -n typelib-1_0-Jcat-1_0
This package provides the GObject Introspection bindings for
%{name}.

%package -n jcat-tool
Summary:        Optional tool for %{name}
Group:          Development/Libraries/Other

%description -n jcat-tool
This package provides the optional jcat-tool for %{name}.

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{sover} = %{version}
Requires:       jcat-tool = %{version}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dgtkdoc=true \
	-Dintrospection=true \
	-Dtests=true \
	%{nil}
%meson_build

%install
%meson_install

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/%{name}.so.%{sover}*

%files -n typelib-1_0-Jcat-1_0
%{_libdir}/girepository-1.0/Jcat-1.0.typelib

%files -n jcat-tool
%doc NEWS README.md
%{_bindir}/jcat-tool
%{_mandir}/man1/jcat-tool.1.gz
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/jcat.*
%{_includedir}/%{name}-%{sover}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/jcat.pc

%changelog
