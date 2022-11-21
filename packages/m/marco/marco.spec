#
# spec file for package marco
#
# Copyright (c) 2022 SUSE LLC
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


%define soname  libmarco-private
%define sover   2
%define _version 1.26

Name:           marco
Version:        1.26.1
Release:        0
Summary:        MATE window manager
License:        GPL-2.0-or-later
URL:            https://mate-desktop.org/
Group:          System/GUI/Other
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE marco-glib-2.54.patch -- Restore GLib 2.54 support.
Patch0:         %{name}-glib-2.54.patch
BuildRequires:  fdupes
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  zenity
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xres)
Requires:       zenity
Recommends:     %{name}-lang
Provides:       windowmanager
# mate-window-manager was last used in openSUSE 13.1.
Provides:       mate-window-manager = %{version}
Obsoletes:      mate-window-manager < %{version}
Obsoletes:      mate-window-manager-lang < %{version}
%glib2_gsettings_schema_requires

%description
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package -n %{soname}%{sover}
Summary:        MATE window manager shared libraries

%description -n %{soname}%{sover}
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package themes
Summary:        MATE window manager themes
# mate-window-manager-themes was last used in openSUSE 13.1.
Provides:       mate-window-manager-themes = %{version}
Obsoletes:      mate-window-manager-themes < %{version}
BuildArch:      noarch

%description themes
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%package devel
Summary:        MATE window manager development files
Requires:       %{soname}%{sover} = %{version}
Group:          Development/Libraries/X11
# mate-window-manager-devel was last used in openSUSE 13.1.
Provides:       mate-window-manager-devel = %{version}
Obsoletes:      mate-window-manager-devel < %{version}

%description devel
Marco is a small window manager, using GTK+ to do everything. It is
developed mainly for the MATE Desktop.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-static                    \
  --disable-scrollkeeper              \
  --disable-schemas-install
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{buildroot}%{_datadir}/mate/wm-properties/%{name}-wm.desktop
%fdupes %{buildroot}%{_datadir}/themes/

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}*
%dir %{_datadir}/mate/
%{_datadir}/mate/wm-properties/
%{_datadir}/%{name}/
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/*/*/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*.?%{?ext_man}

%files lang -f %{name}.lang
%exclude %{_datadir}/help/*

%files -n %{soname}%{sover}
%{_libdir}/*.so.%{sover}*
# Marco requires libmarco-private0 and mate-control-center requires
# it too; make libmarco-private0 own /usr/share/mate-control-center
# to avoid conflicts between packages.
%dir %{_datadir}/mate-control-center/
%dir %{_datadir}/mate-control-center/keybindings/

%files themes
%{_datadir}/themes/Atlanta/
%{_datadir}/themes/ClearlooksRe/
%{_datadir}/themes/Dopple-Left/
%{_datadir}/themes/Dopple/
%{_datadir}/themes/DustBlue/
%{_datadir}/themes/eOS/
%{_datadir}/themes/Esco/
%{_datadir}/themes/Gorilla/
%{_datadir}/themes/Motif/
%{_datadir}/themes/Raleigh/
%{_datadir}/themes/Spidey-Left/
%{_datadir}/themes/Spidey/
%{_datadir}/themes/Splint-Left/
%{_datadir}/themes/Splint/
%{_datadir}/themes/WinMe/

%files devel
%{_includedir}/%{name}-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmarco-private.pc

%changelog
