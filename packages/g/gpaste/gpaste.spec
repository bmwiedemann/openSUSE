#
# spec file for package gpaste
#
# Copyright (c) 2023 SUSE LLC
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


%global __requires_exclude typelib\\(Clutter|St\\)
%global alt_name GPaste
Name:           gpaste
Version:        43.2+6
Release:        0
Summary:        Clipboard management system for GNOME
License:        BSD-2-Clause
Group:          System/GUI/GNOME
URL:            https://github.com/Keruspe/GPaste
# Source url disabled as we are using a git checkout
# Source0:        http://www.imagination-land.org/files/%%{name}/%%{alt_name}-%%{version}.tar.xz
Source0:        %{alt_name}-%{version}.tar.xz
# For directory ownership
BuildRequires:  gnome-shell >= 3.28
BuildRequires:  gobject-introspection-devel >= 1.58.0
BuildRequires:  intltool >= 0.50.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gjs-1.0) >= 1.54.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mutter-clutter-12)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vapigen) >= 0.42
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)

%description
GPaste is a clipboard management daemon with DBus interface.

%package -n libgpaste2-0
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste2-0
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n libgpaste-gtk-3-0
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste-gtk-3-0
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n libgpaste-gtk4-0
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste-gtk4-0
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n libgpaste-gnome-shell-client0
Summary:        Library for managing clipboard history
Group:          System/Libraries

%description -n libgpaste-gnome-shell-client0
GPaste is a clipboard management daemon with DBus interface.

This package provides a library for managing clipboard history.

%package -n typelib-1_0-GPaste-2
Summary:        Introspection bindings for the gpaste clipboard history manager
Group:          System/Libraries

%description -n typelib-1_0-GPaste-2
GPaste is a clipboard management daemon with DBus interface.

This package provides the GObject Introspection bindings for the library
managing clipboard history.

%package -n typelib-1_0-GPasteGtk-3
Summary:        Introspection bindings for the gpaste clipboard history manager
Group:          System/Libraries

%description -n typelib-1_0-GPasteGtk-3
GPaste is a clipboard management daemon with DBus interface.

This package provides the GObject Introspection bindings for the library
managing clipboard history.

%package -n typelib-1_0-GPasteGtk-4
Summary:        Introspection bindings for the gpaste clipboard history manager
Group:          System/Libraries

%description -n typelib-1_0-GPasteGtk-4
GPaste is a clipboard management daemon with DBus interface.

This package provides the GObject Introspection bindings for the library
managing clipboard history.

%package devel
Summary:        Development files for the gpaste clipboard history manager
Group:          Development/Libraries/GNOME
Requires:       libgpaste-gtk-3-0 = %{version}
Requires:       libgpaste-gtk4-0 = %{version}
Requires:       libgpaste2-0 = %{version}
Requires:       typelib-1_0-GPaste-2 = %{version}

%description devel
GPaste is a clipboard management daemon with DBus interface.

This package provides the development files for the library managing
clipboard history.

%package -n gnome-shell-extension-gpaste
Summary:        GPaste status menu extension for GNOME Shell
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-extension-gpaste
GPaste is a clipboard management daemon with DBus interface.

This GNOME Shell extension adds a clipboard item in the status
menu, and provides the ability to copy/paste text.

%package zsh-completion
Summary:        Zsh tab-completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
GPaste is a clipboard management daemon with DBus interface.
This package provides zsh tab-completion for %{name}.

%lang_package

%prep
%autosetup -p1 -n %{alt_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
desktop-file-edit --set-icon=edit-paste --remove-key Categories --add-category=Applet --add-only-show-in=GNOME %{buildroot}%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
%find_lang GPaste %{?no_lang_C}

%ldconfig_scriptlets -n libgpaste2-0
%ldconfig_scriptlets -n libgpaste-gtk-3-0
%ldconfig_scriptlets -n libgpaste-gtk4-0

%files
%license COPYING
%{_bindir}/gpaste-client
%{_libexecdir}/gpaste/
%{_datadir}/applications/org.gnome.GPaste.Ui.desktop
%{_datadir}/applications/org.gnome.GPaste.Preferences.desktop
%{_datadir}/bash-completion/completions/gpaste-client
%{_datadir}/dbus-1/services/org.gnome.GPaste.Ui.service
%{_datadir}/dbus-1/services/org.gnome.GPaste.Preferences.service
%{_datadir}/dbus-1/services/org.gnome.GPaste.service
%{_datadir}/glib-2.0/schemas/org.gnome.GPaste.gschema.xml
%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml
%{_mandir}/man1/gpaste-client.1%{?ext_man}
%{_userunitdir}/org.gnome.GPaste.Ui.service
%{_userunitdir}/org.gnome.GPaste.Preferences.service
%{_userunitdir}/org.gnome.GPaste.service

%files -n libgpaste2-0
%{_libdir}/libgpaste-2.so.*

%files -n libgpaste-gtk-3-0
%{_libdir}/libgpaste-gtk-3.so.*

%files -n libgpaste-gtk4-0
%{_libdir}/libgpaste-gtk4.so.*

%files -n typelib-1_0-GPaste-2
%{_libdir}/girepository-1.0/GPaste-2.typelib

%files -n typelib-1_0-GPasteGtk-3
%{_libdir}/girepository-1.0/GPasteGtk-3.typelib

%files -n typelib-1_0-GPasteGtk-4
%{_libdir}/girepository-1.0/GPasteGtk-4.typelib

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_includedir}/%{name}-2/
%{_libdir}/libgpaste*.so
%{_libdir}/pkgconfig/gpaste*.pc
%{_datadir}/gir-1.0/GPaste*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gpaste-*.deps
%{_datadir}/vala/vapi/gpaste-*.vapi

%files -n gnome-shell-extension-%{name}
%{_datadir}/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/
%{_datadir}/gnome-shell/search-providers/org.gnome.GPaste.search-provider.ini
%{_datadir}/gnome-control-center/keybindings/42-gpaste.xml

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_gpaste-client

%files lang -f GPaste.lang

%changelog
