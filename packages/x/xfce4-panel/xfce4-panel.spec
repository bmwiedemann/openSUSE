#
# spec file for package xfce4-panel
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


%bcond_with git
%define libname_gtk2 libxfce4panel-1_0-4
%define libname_gtk3 libxfce4panel-2_0-4

Name:           xfce4-panel
Version:        4.14.1
Release:        0
Summary:        Panel for the Xfce Desktop Environment
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfce4-panel/start
Source0:        https://archive.xfce.org/src/xfce/%{name}/4.14/%{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
Source2:        %{name}-restore-defaults
Source3:        %{name}-restore-defaults.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(garcon-gtk3-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.13.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.13.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.13.2
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Provides:       xfce4-panel-doc = %{version}
Obsoletes:      xfce4-panel-doc <= 4.12.0
Provides:       xfce4-panel-plugins = %{version}
Obsoletes:      xfce4-panel-plugins < %{version}
Recommends:     %{name}-lang = %{version}
Requires:       %{name}-branding = %{version}
# menu data
Requires:       libgarcon-data
# uses exo-open
Requires:       exo-tools
Recommends:     %{name}-restore-defaults

%description
xfce4-panel is the panel for the Xfce desktop environment.

%package        devel
Summary:        Development Files for xfce4-panel
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The xfce4-panel-devel package contains development files needed to to develop
panel plugins.

%package -n %{libname_gtk2}
Summary:        Xfce Panel Shared Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname_gtk2}
This package contains GTK 2 variant of the xfce4-panel shared library.

%package -n %{libname_gtk3}
Summary:        Xfce Panel Shared Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname_gtk3}
This package contains GTK 3 variant of the xfce4-panel shared library.

%package branding-upstream
Summary:        Upstream Branding for xfce4-panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
#BRAND: Provide default panel configuration in /etc/xdg/xfce4/panel/default.xml
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for xfce4-panel.

%package restore-defaults
Summary:        Script to restore Xfce Panel Defaults
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/XFCE
Requires:       zenity

%description restore-defaults
This package provides a script %{_bindir}/%{name}-restore-defaults which calls allows to restore the Xfce Panel factory defaults.
A desktop file and application launcher is provided.

%lang_package

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-gtk2 \
    --enable-vala=yes \
    --disable-static
%else
%configure \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-gtk2 \
    --enable-vala=yes \
    --disable-static
%endif
%make_build

%install
%make_install

install -m0755 %{SOURCE2} %{buildroot}/%{_bindir}/%{name}-restore-defaults

desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications         \
%{SOURCE3}

rm -f %{buildroot}%{_libdir}/*.la \
    %{buildroot}%{_libdir}/xfce4/panel/plugins/*.la \
    %{buildroot}%{_datadir}/xfce4/xfce4-panel/README.gtkrc-2.0

mkdir -p %{buildroot}%{_datadir}/xfce4/panel-plugins
mkdir -p %{buildroot}%{_libdir}/xfce4
mkdir -p %{buildroot}%{_libdir}/xfce4/panel-plugins
mkdir -p %{buildroot}%{_libexecdir}/xfce4
mkdir -p %{buildroot}%{_libexecdir}/xfce4/panel-plugins

%suse_update_desktop_file panel-desktop-handler
%suse_update_desktop_file panel-preferences

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name}

%fdupes %{buildroot}%{_includedir}

%post -n %{libname_gtk2} -p /sbin/ldconfig

%postun -n %{libname_gtk2} -p /sbin/ldconfig

%post -n %{libname_gtk3} -p /sbin/ldconfig

%postun -n %{libname_gtk3} -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS docs/README.gtkrc-2.0
%{!?with_git:%doc AUTHORS NEWS docs/README.gtkrc-2.0}
%license COPYING COPYING.LIB
%{_bindir}/xfce4-panel
%{_bindir}/xfce4-popup-applicationsmenu
%{_bindir}/xfce4-popup-directorymenu
%{_bindir}/xfce4-popup-windowmenu
%dir %{_libexecdir}/xfce4
%dir %{_libexecdir}/xfce4/panel
%{_libexecdir}/xfce4/panel/migrate
%{_libexecdir}/xfce4/panel/wrapper-1.0
%{_libexecdir}/xfce4/panel/wrapper-2.0
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/panel-plugins
%{_datadir}/xfce4/panel/
%{_datadir}/icons/hicolor/*/apps/xfce4-panel*
%{_datadir}/applications/panel-*.desktop
%dir %{_libexecdir}/xfce4/panel-plugins
%{_libdir}/girepository-1.0/libxfce4panel-2.0.typelib
%{_libdir}/xfce4/panel/
%dir %{_sysconfdir}/xdg/xfce4/panel

%files lang -f %{name}.lang

%files -n %{libname_gtk2}
%license COPYING
%{_libdir}/libxfce4panel-1.0.so.*

%files -n %{libname_gtk3}
%license COPYING
%{_libdir}/libxfce4panel-2.0.so.*

%files devel
%{_includedir}/xfce4/libxfce4panel-*
%{_libdir}/libxfce4panel-*.so
%{_libdir}/pkgconfig/libxfce4panel-*.pc
%{_datadir}/gtk-doc/html/libxfce4panel-*
%{_datadir}/vala/vapi/libxfce4panel-2.0.*
%{_datadir}/gir-1.0/libxfce4panel-2.0.gir

%files branding-upstream
%config %{_sysconfdir}/xdg/xfce4/panel/default.xml

%files restore-defaults
%{_bindir}/xfce4-panel-restore-defaults
%{_datadir}/applications/%{name}-restore-defaults.desktop

%changelog
