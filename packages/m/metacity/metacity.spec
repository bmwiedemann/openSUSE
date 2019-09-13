#
# spec file for package metacity
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define soname  libmetacity
%define sover   1
%define _version 3.30
Name:           metacity
Version:        3.30.1
Release:        0
Summary:        Window Manager for the MATE and GNOME Flashback desktops
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Url:            https://wiki.gnome.org/Projects/Metacity
Source:         https://download.gnome.org/sources/metacity/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE metacity-lower-autotools.patch -- Lower the requirements on autotools.
Patch0:         metacity-lower-autotools.patch
# PATCH-FEATURE-OPENSUSE metacity-gtk-3.20.patch -- Restore GTK+ 3.20 support.
Patch1:         metacity-gtk-3.20.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  zenity
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.3.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite) >= 0.2
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender) >= 0.0
Requires:       zenity
Recommends:     %{name}-lang
Provides:       windowmanager
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
BuildRequires:  pkgconfig(vulkan)
%endif

%description
Metacity is a small window manager, using GTK+ to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

%lang_package

%package -n %{soname}%{sover}
Summary:        Window Manager for the MATE Desktop -- Library to render themes
Group:          System/Libraries

%description -n %{soname}%{sover}
Metacity is a small window manager, using GTK+ to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains a library to render themes.

%package tools
Summary:        Window Manager for the MATE Desktop -- Tools
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description tools
Metacity is a small window manager, using GTK+ to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains tools related to metacity, including an
utility to test themes and a small application to test window
managers.

%package devel
Summary:        Window Manager for the MATE Desktop -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
Metacity is a small window manager, using GTK+ to do everything.
It is developed mainly for the MATE and GNOME Flashback desktops.

This package contains all necessary include files and libraries
needed to develop applications that require libmetacity.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure\
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file metacity
%find_lang %{name} %{?no_lang_C}

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS rationales.txt README
%{_bindir}/metacity
%{_bindir}/metacity-message
%{_datadir}/applications/metacity.desktop
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
%{_bindir}/metacity-window-demo
%dir %{_datadir}/metacity
%dir %{_datadir}/metacity/icons
%{_datadir}/metacity/icons/metacity-window-demo.png
%{_mandir}/man1/metacity-theme-viewer.1%{?ext_man}
%{_mandir}/man1/metacity-window-demo.1%{?ext_man}

%files devel
%{_includedir}/metacity/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/libmetacity.pc

%changelog
