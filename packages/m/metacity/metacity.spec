#
# spec file for package metacity
#
# Copyright (c) 2023 SUSE LLC
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


%define soname  libmetacity
%define sover   3
%define _version 3.46
Name:           metacity
Version:        3.46.1
Release:        0
Summary:        Window Manager for the MATE and GNOME Flashback desktops
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://wiki.gnome.org/Projects/Metacity
Source:         https://download.gnome.org/sources/metacity/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  zenity
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.3.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite) >= 0.2
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender) >= 0.0
BuildRequires:  pkgconfig(xres)
Requires:       zenity
Recommends:     %{name}-lang
Provides:       windowmanager
%glib2_gsettings_schema_requires

%description
Metacity is a window manager using GTK to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

%lang_package

%package -n %{soname}%{sover}
Summary:        Theme rendering library for the MATE Desktop Window Manager
Group:          System/Libraries

%description -n %{soname}%{sover}
Metacity is a window manager using GTK to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains a library to render themes.

%package tools
Summary:        Tools for the MATE Desktop Window Manager
Requires:       %{name} = %{version}

%description tools
Metacity is a window manager using GTK to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains tools related to metacity, including an
utility to test themes and a small application to test window
managers.

%package devel
Summary:        Header files for the MATE Desktop Window Manager
Group:          Development/Libraries/X11
Requires:       %{soname}%{sover} = %{version}

%description devel
Metacity is a window manager using GTK to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains all necessary include files and libraries
needed to develop applications that require libmetacity.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file metacity
%find_lang %{name} %{?no_lang_C}

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS rationales.txt README
%{_bindir}/metacity
%{_bindir}/metacity-message
%{_datadir}/applications/metacity.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.metacity.theme.gschema.xml
%dir %{_datadir}/gnome-control-center/
%dir %{_datadir}/gnome-control-center/keybindings/
%{_datadir}/gnome-control-center/keybindings/50-metacity-*.xml
%{_mandir}/man1/metacity.1%{?ext_man}
%{_mandir}/man1/metacity-message.1%{?ext_man}

%files lang -f %{name}.lang

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files tools
%{_bindir}/metacity-theme-viewer
%{_mandir}/man1/metacity-theme-viewer.1%{?ext_man}

%files devel
%{_includedir}/metacity/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/libmetacity.pc

%changelog
