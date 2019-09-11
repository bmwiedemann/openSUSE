#
# spec file for package libgnome-keyring
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


Name:           libgnome-keyring
Version:        3.12.0
Release:        0
Summary:        Library to integrate with the GNOME Keyring
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/libgnome-keyring/3.12/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  translation-update-upstream
Recommends:     %{name}-lang

%description
The GNOME Keyring is a program that keep password and other secrets
for users. The libgnome-keyring library is used by applications to
integrate with the GNOME Keyring system.

%package -n libgnome-keyring0
Summary:        Library to integrate with the GNOME Keyring
Group:          System/Libraries
Recommends:     %{name}-lang
Recommends:     gnome-keyring
# To make the lang package happy
Provides:       %{name} = %{version}

%description -n libgnome-keyring0
The GNOME Keyring is a program that keep password and other secrets
for users. The libgnome-keyring library is used by applications to
integrate with the GNOME Keyring system.

%package -n typelib-1_0-GnomeKeyring-1_0
Summary:        Library to integrate with the GNOME Keyring -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GnomeKeyring-1_0
The GNOME Keyring is a program that keep password and other secrets
for users. The libgnome-keyring library is used by applications to
integrate with the GNOME Keyring system.

This package provides the GObject Introspection bindings for
libgnome-keyring.

%package devel
Summary:        Library to integrate with the GNOME Keyring - Development Files
Group:          Development/Libraries/GNOME
Requires:       libgnome-keyring0 = %{version}
Requires:       typelib-1_0-GnomeKeyring-1_0 = %{version}
Provides:       gnome-keyring-devel = %{version}
Obsoletes:      gnome-keyring-devel < %{version}
Provides:       gnome-keyring-doc = %{version}
Obsoletes:      gnome-keyring-doc < %{version}

%description devel
The GNOME Keyring is a program that keep password and other secrets
for users. The libgnome-keyring library is used by applications to
integrate with the GNOME Keyring system.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
        --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libgnome-keyring0 -p /sbin/ldconfig
%postun -n libgnome-keyring0 -p /sbin/ldconfig

%files -n libgnome-keyring0
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README
%{_libdir}/libgnome-keyring.so.*

%files -n typelib-1_0-GnomeKeyring-1_0
%{_libdir}/girepository-1.0/GnomeKeyring-1.0.typelib

%files devel
%{_datadir}/gir-1.0/GnomeKeyring-1.0.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gnome-keyring-1
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gnome-keyring

%files lang -f %{name}.lang

%changelog
