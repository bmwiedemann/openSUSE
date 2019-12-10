#
# spec file for package bamf
#
# Copyright (c) 2019 SUSE LLC
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


%define lname   libbamf3-2
%define _binver 3
%define _version 0.5
Name:           bamf
Version:        0.5.4
Release:        0
Summary:        Window matching library
License:        GPL-3.0-only AND LGPL-3.0-only
URL:            https://launchpad.net/bamf
Source:         https://launchpad.net/bamf/%{_version}/%{version}/+download/bamf-%{version}.tar.gz
Source2:        https://launchpad.net/bamf/%{_version}/%{version}/+download/bamf-%{version}.tar.gz.asc
Source3:        %{name}.keyring
# PATCH-FIX-OPENSUSE bamf-fix-gtester2xunit.patch -- Make gtester2xunit requirements easier to meet.
Patch0:         bamf-fix-gtester2xunit.patch
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-lxml
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.2
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.4.7
BuildRequires:  pkgconfig(x11)

%description
bamf matches application windows to desktop files.

%package daemon
Summary:        Window matching daemon
Requires:       %{lname} = %{version}

%description daemon
bamf matches application windows to desktop files.

This package contains the daemon used by the library and a gio
module that facilitates the matching of applications started
through GDesktopAppInfo

%package doc
Summary:        Documentation for libbamf and libbamf3
BuildArch:      noarch

%description doc
This package contains the documentation for the bamf library.

%package -n %{lname}
Summary:        Window matching library

%description -n %{lname}
bamf matches application windows to desktop files.

This package contains libraries to be used by applications.

%package -n typelib-1_0-Bamf-%{_binver}_0
Summary:        Introspection bindings for the BAMF window matching library

%description -n typelib-1_0-Bamf-%{_binver}_0
This package contains introspection data for the Bamf library.

This package provides the GObject Introspection bindings for Bamf.

%package devel
Summary:        Development files for the BAMF window matching library
Requires:       %{lname} = %{version}
Requires:       typelib-1_0-Bamf-%{_binver}_0

%description devel
bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%prep
%autosetup -p1

sed -i '/^CFLAGS=/s/-Werror //' configure.ac

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --disable-static \
  --enable-gtk-doc
%make_build

%install
%make_install

rm -r %{buildroot}%{_datadir}/upstart/

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files daemon
%license COPYING COPYING.LGPL
%doc ChangeLog TODO
%{_libexecdir}/bamf/
%{_datadir}/dbus-1/services/org.ayatana.bamf.service
%{_userunitdir}/bamfdaemon.service

%files -n %{lname}
%license COPYING COPYING.LGPL
%doc ChangeLog TODO
%{_libdir}/libbamf%{_binver}.so.*

%files -n typelib-1_0-Bamf-%{_binver}_0
%{_libdir}/girepository-1.0/

%files devel
%{_includedir}/libbamf%{_binver}/
%{_libdir}/libbamf%{_binver}.so
%{_datadir}/vala/
%{_datadir}/gir-1.0/
%{_libdir}/pkgconfig/libbamf%{_binver}.pc

%files doc
%doc %{_datadir}/gtk-doc/

%changelog
