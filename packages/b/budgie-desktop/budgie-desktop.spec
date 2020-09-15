#
# spec file for package budgie-desktop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2016 Ikey Doherty <ikey@solus-project.com>
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
%if !0%{?is_backports}
%define brandingsuffix openSUSE
%else
%define brandingsuffix SLE
%endif
%define gnome_version %(rpm -q --queryformat='%%{VERSION}' libgnome-desktop-3-devel | sed 's/\.[0-9]*$//g')
Name:           budgie-desktop
Version:        10.5.1+1ed6276b
Release:        0
Summary:        GTK3 Desktop Environment
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://getsol.us/solus/experiences/
Source:         %{name}-%{version}.tar.xz
#Source1:        https://github.com/solus-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
#Source2:        %{name}.keyring
Source3:        budgie-desktop-nemo-autostart.desktop
# PATCH-FIX-OPENSUSE: Create a clean separation between Budgie and GNOME desktops
Patch:          desktop-override.patch
# PATCH-FIX-OPENSUSE: Use nemo instead of nautilus for desktop icons
Patch1:         nemo-instead-of-nautilus.patch
# PATCH-FIX-UPSTREAM gh#solus-project/budgie-desktop#2029
Patch2:         vala-0.49.patch
# PATCH-FIX-OPENSUSE Re-add Leap 15.2 support
Patch3:         Revert-GNOME-3.38-support.patch
BuildRequires:  intltool
BuildRequires:  meson >= 0.41.2
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen) >= 0.28
BuildRequires:  (pkgconfig(libmutter-5) or pkgconfig(libmutter-6) or pkgconfig(libmutter-7))
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(alsa)
Requires:       typelib-1_0-PeasGtk-1_0
Requires:       typelib-1_0-Budgie-1_0
Requires:       ibus
Requires:       gnome-session-core
Requires:       gnome-settings-daemon
Requires:       gnome-control-center
Requires:       budgie-screensaver
Requires:       nemo
Recommends:     gnome-software
Recommends:     NetworkManager-applet
Recommends:     gnome-backgrounds
Recommends:     budgie-desktop-doc
Recommends:     budgie-desktop-branding-%{brandingsuffix}
%define vala_version %(rpm -q --queryformat='%%{VERSION}' vala | sed 's/\.[0-9]*$//g')

%description
Budgie Desktop is the flagship desktop for the Solus Operating System.

%package -n typelib-1_0-Budgie-1_0
Summary:        Introspection bindings for the Budgie Desktop
Group:          System/Libraries 
Requires:       %{name} = %{version}-%{release}

%description -n typelib-1_0-Budgie-1_0
This package provides GObject Introspection files required for
developing Budgie Applets using interpreted languages, such as Python
GObject Introspection bindings.

%package devel
Summary:        Development files for the Budgie Desktop
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}-%{release}
Requires:       typelib-1_0-Budgie-1_0 = %{version}-%{release}

%description devel
This package provides development files required for software to be
able to use and link against the Budgie APIs, to create their own
applets for the Budgie Panel.

%package doc
Summary:        Documentation files for the Budgie Desktop
Group:          Documentation/HTML

%description doc
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.

%package -n libraven0
Summary:        Shared library for Raven
Group:          System/Libraries

%description -n libraven0
Budgie Desktop Notification Center.

%package -n libbudgietheme0
Summary:        Shared library for Budgie theming
Group:          System/Libraries

%description -n libbudgietheme0
Budgie theming engine shared library package.

%package -n libbudgie-plugin0
Summary:        Shared library for Budgie plugins
Group:          System/Libraries

%description -n libbudgie-plugin0
Shared library for budgie plugins to link against.

%package -n libbudgie-private0
Summary:        Private library for Budgie
Group:          System/Libraries

%description -n libbudgie-private0
Private library for Budgie desktop to link against.

%lang_package

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%if "%{gnome_version}" < "3.36"
%patch3 -p1
%endif

%build
%meson
%meson_build

%install
export LANG=en_US.UTF-8
%meson_install

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

# nemo autostart
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/autostart

%find_lang %{name}

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop 20

%postun
[ -f %{_datadir}/xsessions/budgie-desktop.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/budgie-desktop.desktop

%post   -n libraven0 -p /sbin/ldconfig
%postun -n libraven0 -p /sbin/ldconfig
%post   -n libbudgietheme0 -p /sbin/ldconfig
%postun -n libbudgietheme0 -p /sbin/ldconfig
%post   -n libbudgie-plugin0 -p /sbin/ldconfig
%postun -n libbudgie-plugin0 -p /sbin/ldconfig
%post   -n libbudgie-private0 -p /sbin/ldconfig
%postun -n libbudgie-private0 -p /sbin/ldconfig

%files
%license LICENSE LICENSE.LGPL2.1
%{_datadir}/gnome-session
%{_bindir}/budgie-*
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop
%{_sysconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop
%{_sysconfdir}/xdg/autostart/budgie-desktop-nm-applet.desktop
%{_sysconfdir}/xdg/autostart/budgie-desktop-nemo-autostart.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop

%files -n libraven0
%{_libdir}/libraven.so.*

%files -n libbudgietheme0
%{_libdir}/libbudgietheme.so.*

%files -n libbudgie-plugin0
%{_libdir}/libbudgie-plugin.so.*

%files -n libbudgie-private0
%{_libdir}/libbudgie-private.so.*

%files devel
%{_includedir}/budgie-desktop
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/vala/vapi/budgie-1.0.*

%files -n typelib-1_0-Budgie-1_0
%{_libdir}/girepository-1.0/Budgie-1.0.typelib

%files doc
%{_datadir}/gtk-doc/html/budgie-desktop

%files lang -f %{name}.lang

%changelog
