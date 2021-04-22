#
# spec file for package gpaste
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Simone Tolotti, <simone.tolotti@gmail.com>.
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


%global __requires_exclude typelib\\(Clutter\\)
Name:           gpaste
Version:        3.40.1
Release:        0
Summary:        Clipboard management system for GNOME
License:        BSD-2-Clause
Group:          System/GUI/GNOME
URL:            https://github.com/Keruspe/GPaste
Source0:        http://www.imagination-land.org/files/%{name}/%{name}-%{version}.tar.xz

# For directory ownership
BuildRequires:  gnome-shell >= 3.28
BuildRequires:  gobject-introspection-devel >= 1.58.0
BuildRequires:  intltool >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.54.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mutter-clutter-8)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vapigen) >= 0.42
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)

%description
GPaste is a clipboard management daemon with DBus interface.

%package -n libgpaste13
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste13
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n libgpaste-gnome-shell-client0
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste-gnome-shell-client0
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n typelib-1_0-GPaste-1_0
Summary:        Introspection bindings for the gpaste clipboard history manager
Group:          System/Libraries

%description -n typelib-1_0-GPaste-1_0
GPaste is a clipboard management daemon with DBus interface.

This package provides the GObject Introspection bindings for the library
managing clipboard history.

%package devel
Summary:        Development files for the gpaste clipboard history manager
Group:          Development/Libraries/GNOME
Requires:       libgpaste13 = %{version}
Requires:       typelib-1_0-GPaste-1_0 = %{version}

%description devel
GPaste is a clipboard management daemon with DBus interface.

This package provides the development files for the library managing
clipboard history.

%package -n gnome-shell-extension-gpaste
Summary:        GPaste status menu extension for GNOME Shell
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-extension-gpaste
GPaste is a clipboard management daemon with DBus interface.

This GNOME Shell extension adds a clipboard item in the status
menu, and provides the ability to copy/paste text.

%lang_package

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%configure --enable-vala
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
desktop-file-edit --set-icon=edit-paste --remove-key Categories --add-category=Applet --add-only-show-in=GNOME %{buildroot}%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
%find_lang GPaste %{?no_lang_C}

%post -n libgpaste13 -p /sbin/ldconfig
%postun -n libgpaste13 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/gpaste-client
%{_libexecdir}/gpaste/
%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
%{_datadir}/bash-completion/completions/gpaste-client
%{_datadir}/dbus-1/services/org.gnome.GPaste.Ui.service
%{_datadir}/dbus-1/services/org.gnome.GPaste.service
%{_datadir}/glib-2.0/schemas/org.gnome.GPaste.gschema.xml
%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml
%{_datadir}/zsh/site-functions/_gpaste-client
%{_mandir}/man1/gpaste-client.1%{?ext_man}
%{_userunitdir}/org.gnome.GPaste.Ui.service
%{_userunitdir}/org.gnome.GPaste.service
# Bah, we need to own this...
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%files -n libgpaste13
%{_libdir}/libgpaste.so.*

%files -n typelib-1_0-GPaste-1_0
%{_libdir}/girepository-1.0/GPaste-1.0.typelib

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_includedir}/gpaste/
%{_libdir}/libgpaste*.so
%{_libdir}/pkgconfig/gpaste*.pc
%{_datadir}/gir-1.0/GPaste-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gpaste-1.0.deps
%{_datadir}/vala/vapi/gpaste-1.0.vapi

%files -n gnome-shell-extension-%{name}
%{_datadir}/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/
%{_datadir}/gnome-shell/search-providers/org.gnome.GPaste.search-provider.ini
%{_datadir}/gnome-control-center/keybindings/42-gpaste.xml

%files lang -f GPaste.lang

%changelog
