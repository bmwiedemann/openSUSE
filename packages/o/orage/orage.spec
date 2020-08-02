#
# spec file for package orage
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           orage
Version:        4.12.1
Release:        0
Summary:        Time-managing Application for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Office/Organizers
Url:            http://www.xfce.org/projects#applications
Source:         http://archive.xfce.org/src/apps/orage/4.12/%{name}-%{version}.tar.bz2
Source1:        README.SUSE
# PATCH-FIX-UPSTREAM orage-use-docdir.patch gber@opensuse.org -- Use docdir correctly
Patch0:         orage-use-docdir.patch
# PATCH-FIX-UPSTREAM 0001-fix-build-with-libical-version-3.patch -- fix build with libical3, bxo#13997
Patch1:         0001-fix-build-with-libical-version-3.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libxfce4ui-1)
BuildRequires:  pkgconfig(popt)
Requires:       exo-tools
Requires:       xfce4-panel
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-lang = %{version}
# use /usr/bin/play to play notification sounds
Recommends:     sox
Provides:       xfcalendar = %{version}
Obsoletes:      xfcalendar < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Orage is a fast and easy to use graphical calendar for the Xfce desktop
environment. It uses the portable ical format and includes common calendar
features like repeating appointments and multiple alarming possibilities. Orage
does not have group calendar features and can only be used for single user.

%package        doc
Summary:        Documentation for orage
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This package contains the documentation for orage.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} .
sed -i 's:^Icon=clock:Icon=xfcalendar:' globaltime/globaltime.desktop.in

%build
xdt-autogen
# workaround broken libical headers
export CFLAGS="%{optflags} -I%{_includedir}/libical"
%configure --docdir=%{_datadir}/xfce4/orage/html
make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/liborageclock.la

install -D -p -m 644 icons/48x48/xfcalendar.png \
    %{buildroot}%{_datadir}/pixmaps/xfcalendar.png

%suse_update_desktop_file -r xfcalendar X-XFCE Office Calendar GTK
%suse_update_desktop_file -r globaltime X-XFCE Utility Clock GTK
%suse_update_desktop_file xfce-xfcalendar-settings

%fdupes %{buildroot}%{_datadir}

%find_lang %{name} %{?no_lang_C}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS NEWS README.SUSE
%{_bindir}/orage
%{_bindir}/globaltime
%{_bindir}/tz_convert
%doc %{_mandir}/man1/globaltime.1*
%doc %{_mandir}/man1/orage.1*
%doc %{_mandir}/man1/tz_convert.1*
%dir %{_datadir}/%{name}
%{_datadir}/orage/sounds/
%{_datadir}/applications/*desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/pixmaps/xfcalendar.png
%{_datadir}/dbus-1/services/org.xfce.*
%{_datadir}/xfce4/panel/plugins/xfce4-orageclock-plugin.desktop
%{_libdir}/xfce4/panel/plugins/liborageclock.so

%files doc
%defattr(-,root,root)
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/orage
%doc %{_datadir}/xfce4/orage/html/

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
