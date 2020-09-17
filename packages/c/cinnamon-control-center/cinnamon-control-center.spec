#
# spec file for package cinnamon-control-center
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


%define soname  libcinnamon-control-center
%define sover   1
Name:           cinnamon-control-center
Version:        4.6.2
Release:        0
Summary:        Utilities to configure the Cinnamon desktop
License:        GPL-2.0-only AND GPL-3.0-or-later AND MIT
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-control-center
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE %%{name}-ignore-polkit-rules.patch - marguerite@opensuse.org fix boo#1125427
Patch:          %{name}-ignore-polkit-rules.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  desktop-data
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cinnamon-desktop)
BuildRequires:  pkgconfig(cinnamon-settings-daemon)
BuildRequires:  pkgconfig(colord) >= 0.1.14
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.23.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(goa-1.0) >= 3.18.0
BuildRequires:  pkgconfig(goa-backend-1.0) >= 3.18.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.13
BuildRequires:  pkgconfig(libcinnamon-menu-3.0)
BuildRequires:  pkgconfig(libgnomekbd)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(libnotify) >= 0.7.3
BuildRequires:  pkgconfig(libpulse) >= 1.1
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 1.1
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxklavier) >= 5.1
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.2
Requires:       %{name}-common = %{version}
Requires:       accountsservice
Requires:       adwaita-icon-theme
Requires:       cinnamon-settings-daemon
Requires:       desktop-data
Requires:       gnome-online-accounts
Requires:       polkit-gnome
Recommends:     %{name}-lang
Recommends:     iso-codes
Recommends:     mousetweaks
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libnm) >= 1.2.0
BuildRequires:  pkgconfig(libnma) >= 1.2.0
BuildRequires:  pkgconfig(mm-glib) >= 0.7
%endif

%description
This package contains configuration applets for the Cinnamon
desktop, allowing to set accessibility configuration, desktop
fonts, keyboard and mouse properties, sound setup, desktop theme
and background, user interface properties, screen resolution, and
other Cinnamon parameters.

%package common
Summary:        Common files for the Cinnamon configuration utilities
Group:          System/GUI/Other
Recommends:     %{name}-lang
BuildArch:      noarch

%description common
This package contains common files (icons, pixmaps, locales files)
needed by the configuration applets in the cinnamon-control-center
package.

%package -n %{soname}%{sover}
Summary:        Shared libraries for the Cinnamon configuration utilities
Group:          System/Libraries

%description -n %{soname}%{sover}
This package provides shared libraries used by Cinnamon control
centre applets.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications that require these.

%prep
%setup -q
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static         \
  --disable-update-mimedb  \
%if 0%{?suse_version} < 1500
  --disable-networkmanager \
  --disable-modemmanager   \
%endif
  --enable-systemd
make %{?_smp_mflags} V=1

%install
%make_install

ls %{buildroot}%{_datadir}/applications/cinnamon-* | while read desktop; do
    %suse_update_desktop_file $desktop
done

find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name}-timezones
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun

%post common
%icon_theme_cache_post

%postun common
%icon_theme_cache_postun
%endif

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README debian/changelog
%{_bindir}/cinnamon-*
%{_datadir}/applications/cinnamon-*.desktop

%files common -f %{name}-timezones.lang
%config %{_sysconfdir}/xdg/menus/cinnamoncc.menu
%{_datadir}/%{name}/
%dir %{_datadir}/desktop-directories/
%{_datadir}/desktop-directories/cinnamoncc.directory
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.cinnamon.controlcenter.datetime.policy

%files -n %{soname}%{sover}
%{_libdir}/%{name}-%{sover}/
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/%{name}-%{sover}/
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/%{soname}.so

%changelog
