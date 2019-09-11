#
# spec file for package nuntius
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


Name:           nuntius
Version:        0.2.0
Release:        0
Summary:        Get notifications from the phone or tablet
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://github.com/holylobster/nuntius-linux
Source:         https://github.com/holylobster/nuntius-linux/releases/download/v%{version}/nuntius-%{version}.tar.xz
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.50.1
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.23.3
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.16.2
BuildRequires:  pkgconfig(libqrencode) >= 3.1
Recommends:     %{name}-lang

%description
Nuntius is a daemon that connects to another Nuntius app running on
a phone or a tablet and proxies the notifications using Bluetooth.

%lang_package

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/*nuntius.desktop Utility PDA
%find_lang nuntius

%check
make check %{?_smp_mflags}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/nuntius
%dir %{_datadir}/appdata/
%{_datadir}/appdata/*nuntius.appdata.xml
%{_datadir}/applications/*nuntius.desktop
# Own dirs so we do not need to BuildRequire dbus-1 for this
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/*nuntius.service
%{_datadir}/icons/hicolor/*/apps/nuntius.png
%{_sysconfdir}/xdg/autostart/*nuntius.desktop

%files lang -f %{name}.lang

%changelog
