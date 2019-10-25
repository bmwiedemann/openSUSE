#
# spec file for package plank
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


%global __provides_exclude_from ^%{_libdir}/.*/docklets/.*\\.so$
%define soname	libplank
%define sover 1
Name:           plank
Version:        0.11.89
Release:        0
Summary:        Trivial dock
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://launchpad.net/plank
Source0:        https://launchpad.net/%{name}/1.0/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        https://launchpad.net/%{name}/1.0/%{version}/+download/%{name}-%{version}.tar.xz.asc
Source3:        %{name}.keyring
BuildRequires:  autoconf >= 2.65
BuildRequires:  automake >= 1.11
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool >= 2
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4) >= 0.4
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.34
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.2.92
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes) >= 5.0
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
Requires:       bamf-daemon >= 0.2.92
Recommends:     %{name}-docklets
Recommends:     %{name}-lang

%description
Plank is a trivial dock.

It is a library which can be extended to create other
dock programs with more advanced features.

%package -n %{soname}%{sover}
Summary:        Library for the Plank dock
Group:          System/Libraries

%description -n %{soname}%{sover}
Plank is a trivial dock.
It is, however, a library which can be extended to create other
dock programs with more advanced features.

%package docklets
Summary:        A collection of docklets for the Plank dock
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description docklets
This package contains a collection of docklets: clippy, clock, cpumonitor,
desktop, trash and etc.

%package devel
Summary:        Development files for the Plank dock
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
The libxnoise development package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking application which will use libplank.

%lang_package

%prep
%setup -q

%build
[ ! -e configure ] && NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-static \
  --disable-apport
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r %{name} Utility DesktopUtility
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS COPYRIGHT HACKING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_libdir}/%{name}

%files -n %{soname}%{sover}
%{_libdir}/lib%{name}.so.*

%files docklets
%{_libdir}/%{name}/docklets/

%files lang -f %{name}.lang

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/vala/

%changelog
