#
# spec file for package mate-system-monitor
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
Name:           mate-system-monitor
Version:        1.22.1
Release:        0
Summary:        MATE Desktop system monitor
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE mate-system-monitor-xdgsu.patch sor.alexei@meowr.ru -- Use xdg-su instead of gksu.
Patch0:         mate-system-monitor-xdgsu.patch
# PATCH-FEATURE-OPENSUSE mate-system-monitor-gtk-3.20.patch -- Restore GLib 2.48 and GTK+ 3.20 support.
Patch1:         mate-system-monitor-gtk-3.20.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.20
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       polkit
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Process viewer and system resource monitor for the MATE. This
package allows you to graphically view and manipulate the running
processes on your system. It also provides an overview of available
resources such as CPU and memory.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --disable-scrollkeeper              \
  --libexecdir=%{_libexecdir}/%{name} \
  --enable-systemd
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_libexecdir}/mate-system-monitor/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/polkit-1/actions/*%{name}.policy
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
