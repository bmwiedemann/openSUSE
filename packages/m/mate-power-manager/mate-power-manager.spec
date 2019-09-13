#
# spec file for package mate-power-manager
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


%define _version 1.22
Name:           mate-power-manager
Version:        1.22.1
Release:        0
Summary:        MATE Desktop UPower policy management
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE mate-power-manager-gtk-3.20.patch -- Restore GLib 2.48 and GTK+ 3.20 support.
Patch0:         mate-power-manager-gtk-3.20.patch
BuildRequires:  fdupes
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr) >= 1.3.0
BuildRequires:  pkgconfig(xrender)
Requires:       upower
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
MATE Power Manager is a MATE session daemon that acts as a policy
agent on top of UPower, which requires fairly new versions of the
kernel and udev. MATE Power Manager listens for system events and
responds with user-configurable actions.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_libexecdir}/%{name}/
%{_datadir}/applications/mate-power-preferences.desktop
%{_datadir}/applications/mate-power-statistics.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mate-panel/
%{_datadir}/mate-power-manager/
%{_datadir}/polkit-1/
%{_mandir}/man?/*.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
