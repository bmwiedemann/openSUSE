#
# spec file for package libcryptui
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libcryptui
Version:        3.12.2
Release:        0
# FIXME: find out why building introspection support for this package requires libtool
Summary:        Library for prompting for PGP keys
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://projects.gnome.org/seahorse/
Source:         http://download.gnome.org/sources/libcryptui/3.12/%{name}-%{version}.tar.xz
# adapted from https://gitlab.archlinux.org/archlinux/packaging/packages/libcryptui/-/blob/main/fix-configure-gpgme.patch?ref_type=heads
Patch0:         fix-configure-gpgme.patch
# taken from https://gitlab.archlinux.org/archlinux/packaging/packages/libcryptui/-/blob/main/gpgme-2.0.patch?ref_type=heads
Patch1:         gpgme-2.0.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpg2
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(sm)
# for Patch0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  gtk-doc
BuildRequires:  libtool
#

%description
Libcryptui is a library used for prompting for PGP keys.

%package -n libcryptui0
Summary:        Library for prompting for PGP keys
License:        LGPL-2.1-or-later
Group:          System/Libraries
# Need some schema from gnome-keyring
Requires:       %{name}-data
Requires:       gnome-keyring
# The library talks to seahorse-daemon
Recommends:     seahorse-daemon
# To make lang package installable
Provides:       %{name} = %{version}

%description -n libcryptui0
Libcryptui is a library used for prompting for PGP keys.

%package -n typelib-1_0-CryptUI-0_0
Summary:        Introspection bindings for libcryptui, a PGP key prompting library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-CryptUI-0_0
Libcryptui is a library used for prompting for PGP keys.

This package provides the GObject Introspection bindings for
libcryptui.

%package -n libcryptui-data
Summary:        Data files for libcryptui, a PGP key prompting library
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
%glib2_gsettings_schema_requires

%description -n libcryptui-data
Libcryptui is a library used for prompting for PGP keys.

%package -n seahorse-daemon
Summary:        Daemon for PGP prompting by libcryptui
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Requires:       %{name}-data

%description -n seahorse-daemon
Libcryptui is a library used for prompting for PGP keys.

%package devel
Summary:        Development files for libcryptui, a PGP key prompting library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       libcryptui0 = %{version}
Requires:       typelib-1_0-CryptUI-0_0 = %{version}

%description devel
Libcryptui is a library used for prompting for PGP keys.

%lang_package

%prep
%autosetup -p1

%build
# for Patch0
autoconf -i
%configure \
        --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang cryptui %{?no_lang_C}

%ldconfig_scriptlets -n libcryptui0

%post -n libcryptui-data
%glib2_gsettings_schema_post

%postun -n libcryptui-data
%glib2_gsettings_schema_postun

%files -n libcryptui0
%license COPYING
%doc AUTHORS ChangeLog COPYING-LIBCRYPTUI NEWS README
%{_libdir}/libcryptui.so.*

%files -n typelib-1_0-CryptUI-0_0
%license COPYING
%{_libdir}/girepository-1.0/CryptUI-0.0.typelib

%files -n libcryptui-data
%license COPYING
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.seahorse.recipients.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml

%files -n seahorse-daemon
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/seahorse-daemon
%{_datadir}/dbus-1/services/org.gnome.seahorse.service
%{_datadir}/cryptui/
%{_datadir}/pixmaps/cryptui/
%{_mandir}/man1/seahorse-daemon.1%{?ext_man}

%files lang -f cryptui.lang
%license COPYING

%files devel
%license COPYING
%{_includedir}/libcryptui/
%{_libdir}/pkgconfig/cryptui-0.0.pc
%{_libdir}/libcryptui.so
%{_datadir}/gir-1.0/CryptUI-0.0.gir
%doc %{_datadir}/gtk-doc/html/libcryptui/

%changelog
