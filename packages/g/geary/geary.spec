#
# spec file for package geary
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


Name:           geary
Version:        3.34.1
Release:        0
Summary:        An email reader for the GNOME desktop
License:        LGPL-2.1-or-later AND CC-BY-3.0 AND BSD-2-Clause
Group:          Productivity/Networking/Email/Clients
URL:            https://wiki.gnome.org/Apps/Geary
Source0:        https://download.gnome.org/sources/geary/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xml2po
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(enchant-2) >= 2.1
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gcr-3) >= 3.10.1
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.17
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(javascriptcoregtk-4.0) >= 2.10.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra) >= 0.28
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.9
BuildRequires:  pkgconfig(libsecret-1) >= 0.11
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(sqlite3) >= 3.7.4
BuildRequires:  pkgconfig(vapigen) >= 0.22.1
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.10.0
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0) >= 2.10.0
Recommends:     %{name}-lang

%description
Geary is a email reader for GNOME.

Its interface is based on conversations, so entire discussion
may be read without having to navigate between messages.

%lang_package

%prep
%autosetup -p1

%build
%meson \
    -Dtnef-support=false \
    %{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.Geary
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING COPYING.icons COPYING.snowball
%doc README NEWS THANKS AUTHORS
%{_datadir}/help/C/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/web-extensions
%{_libdir}/%{name}/web-extensions/libgeary-web-process.so
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Geary.appdata.xml
%{_datadir}/applications/org.gnome.Geary.desktop
%{_datadir}/applications/geary-autostart.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/glib-2.0/schemas/org.gnome.Geary.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Geary.service

%files lang -f %{name}.lang

%changelog
