#
# spec file for package gcr
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gcr
Version:        3.34.0
Release:        0
# FIXME: Verify if the requires in typelib-1_0-Gcr-3 is still correct and required (see bgo#725501).
Summary:        Library for Crypto UI related tasks
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gcr/3.34/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-SLE gcr-bsc932232-use-libgcrypt-allocators.patch bsc#932232 hpj@suse.com -- use libgcrypt allocators for FIPS mode
Patch1:         gcr-bsc932232-use-libgcrypt-allocators.patch
# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  gettext >= 0.19.8
BuildRequires:  gobject-introspection-devel >= 1.34
# configure is looking for the gpg2 path
BuildRequires:  gpg2
BuildRequires:  gtk-doc
BuildRequires:  libgcrypt-devel >= 1.4.5
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.18.0.22
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.12
BuildRequires:  pkgconfig(p11-kit-1) >= 0.19.0
BuildRequires:  pkgconfig(pango)

%description
GCR is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides the viewer for crypto files on the GNOME
desktop.

GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package viewer
Summary:        Viewer for Crypto Files
Group:          Productivity/Security
Recommends:     %{name}-lang

%description viewer
This packages provides the viewer for crypto files on the GNOME desktop.

%package data
Summary:        Data and icon set for gcr
Group:          System/Libraries

%description data
This package provides the GSettings schemas and a collection of icons
needed by libgcr.

%package prompter
Summary:        Prompt dialog for gcr
Group:          System/Libraries

%description prompter
This package provides the prompt dialog needed by libgcr.

%package ssh-askpass
Summary:        SSH password callback helper for gcr
Group:          System/Libraries
Supplements:    packageand(gpg2:gnome-shell)

%description ssh-askpass
gcr-ssh-askpass allows an ssh command to callback for a password.

%package -n libgcr-3-1
Summary:        Library for Crypto UI related tasks
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
Requires:       %{name}-prompter >= %{version}
Recommends:     %{name}-ask-pass
Recommends:     %{name}-lang
Recommends:     %{name}-viewer = %{version}
# To make lang package installable
Provides:       %{name} = %{version}

%description -n libgcr-3-1
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n typelib-1_0-Gcr-3
Summary:        Introspection bindings for gcr, a library for crypto UI related tasks
# Due to broken typelib files, this one cannot be automatically inspected
Group:          System/Libraries
Requires:       typelib-1_0-Gck-1

%description -n typelib-1_0-Gcr-3
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

This package provides the GObject Introspection bindings for GCR.

%package -n typelib-1_0-GcrUi-3
Summary:        Introspection bindings for gcr, a library for crypto UI related tasks
Group:          System/Libraries

%description -n typelib-1_0-GcrUi-3
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

This package provides the GObject Introspection bindings for GCR.

%package -n libgcr-devel
Summary:        Development files for gcr, a library for crypto UI related tasks
Group:          Development/Libraries/GNOME
Requires:       libgcr-3-1 = %{version}
Requires:       typelib-1_0-Gcr-3 = %{version}
Requires:       typelib-1_0-GcrUi-3 = %{version}

%description -n libgcr-devel
GCR is a library for displaying certificates, and crypto UI, accessing
key stores.

%package -n libgck-1-0
Summary:        GObject library to access PKCS#11 modules
Group:          System/Libraries
Recommends:     %{name}-lang
# Small hack, to help gnome-keyring subpackage containing gck
# modules have a proper dependency, without having to care about
# the soname.
Provides:       gck = %{version}

%description -n libgck-1-0
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%package -n typelib-1_0-Gck-1
Summary:        Introspection bindings for gck, a GObject library to access PKCS#11 modules
Group:          System/Libraries

%description -n typelib-1_0-Gck-1
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

This package provides the GObject Introspection bindings for GCK.

%package -n libgck-devel
Summary:        Development files for gck, a GObject library to access PKCS#11 modules
Group:          Development/Libraries/GNOME
Requires:       libgck-1-0 = %{version}
Requires:       typelib-1_0-Gck-1 = %{version}

%description -n libgck-devel
GCK is a library for accessing PKCS#11 modules like smart cards, in a
(G)object oriented way.

%lang_package

%prep
%setup -q
%if !0%{?is_opensuse}
%patch1 -p1
%endif

%build
%configure \
    --disable-static \
    --enable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file gcr-prompter
%suse_update_desktop_file gcr-viewer
%find_lang %{name}

%post -n libgcr-3-1 -p /sbin/ldconfig
%postun -n libgcr-3-1 -p /sbin/ldconfig
%post -n libgck-1-0 -p /sbin/ldconfig
%postun -n libgck-1-0 -p /sbin/ldconfig

%files viewer
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README
%{_bindir}/gcr-viewer
%{_datadir}/applications/gcr-viewer.desktop
%{_datadir}/mime/packages/gcr-crypto-types.xml

%files data
%doc AUTHORS ChangeLog HACKING NEWS README
%{_datadir}/icons/hicolor/*/apps/*
# Own the directory since we can't depend on gconf providing them
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp.convert
%{_datadir}/GConf/gsettings/org.gnome.crypto.pgp_keyservers.convert
%{_datadir}/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml

%files prompter
%{_libexecdir}/gcr-prompter
%{_datadir}/applications/gcr-prompter.desktop
%{_datadir}/dbus-1/services/org.gnome.keyring.PrivatePrompter.service
%{_datadir}/dbus-1/services/org.gnome.keyring.SystemPrompter.service

%files ssh-askpass
%{_prefix}/lib/gcr-ssh-askpass

%files -n libgcr-3-1
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README
%{_libdir}/libgcr-3.so.*
%{_libdir}/libgcr-base-3.so.*
%{_libdir}/libgcr-ui-3.so.*

%files -n typelib-1_0-Gcr-3
%{_libdir}/girepository-1.0/Gcr-3.typelib

%files -n typelib-1_0-GcrUi-3
%{_libdir}/girepository-1.0/GcrUi-3.typelib

%files -n libgcr-devel
%doc %{_datadir}/gtk-doc/html/gcr-3/
%{_libdir}/libgcr-3.so
%{_libdir}/libgcr-base-3.so
%{_libdir}/libgcr-ui-3.so
%{_libdir}/pkgconfig/gcr-3.pc
%{_libdir}/pkgconfig/gcr-base-3.pc
%{_libdir}/pkgconfig/gcr-ui-3.pc
%dir %{_includedir}/gcr-3
%{_includedir}/gcr-3
%{_datadir}/gir-1.0/GcrUi-3.gir

%files -n libgck-1-0
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README
%{_libdir}/libgck-1.so.*

%files -n typelib-1_0-Gck-1
%{_libdir}/girepository-1.0/Gck-1.typelib

%files -n libgck-devel
%doc %{_datadir}/gtk-doc/html/gck/
%{_libdir}/libgck-1.so
%{_libdir}/pkgconfig/gck-1.pc
%{_includedir}/gck-1/
%{_datadir}/gir-1.0/Gck-1.gir
%{_datadir}/gir-1.0/Gcr-3.gir
%{_datadir}/vala/vapi/

%files lang -f %{name}.lang

%changelog
