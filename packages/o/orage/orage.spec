#
# spec file for package orage
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


Name:           orage
Version:        4.16.0
Release:        0
Summary:        Time-managing Application for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://docs.xfce.org/panel-plugins/orage/start
Source:         http://archive.xfce.org/src/apps/orage/4.16/%{name}-%{version}.tar.bz2
Source1:        README.SUSE
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.52.0
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(popt)
Requires:       exo-tools
Requires:       xfce4-panel
Recommends:     %{name}-lang = %{version}-%{release}
# use /usr/bin/play to play notification sounds
Recommends:     sox
Provides:       orage-doc = %{version}-%{release}
Provides:       xfcalendar = %{version}-%{release}
Obsoletes:      orage-doc <= %{version}-%{release}
Obsoletes:      xfcalendar < %{version}-%{release}

%description
Orage is a fast and easy to use graphical calendar for the Xfce desktop
environment. It uses the portable ical format and includes common calendar
features like repeating appointments and multiple alarming possibilities. Orage
does not have group calendar features and can only be used for single user.

%lang_package

%prep
%autosetup
cp %{SOURCE1} .

%build
%configure
%make_build

%install
%make_install

%suse_update_desktop_file -r org.xfce.orage.globaltime X-XFCE Utility Clock GTK

%fdupes %{buildroot}%{_datadir}

%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README.md AUTHORS NEWS README.SUSE
%{_bindir}/globaltime
%{_bindir}/orage
%dir %{_datadir}/%{name}
%{_datadir}/orage/sounds/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/*

%files lang -f %{name}.lang

%changelog
