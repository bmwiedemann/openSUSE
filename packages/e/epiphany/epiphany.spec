#
# spec file for package epiphany
#
# Copyright (c) 2024 SUSE LLC
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


Name:           epiphany
Version:        46.2
Release:        0
Summary:        GNOME Web Browser
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://wiki.gnome.org/Apps/Web
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo) >= 1.2
BuildRequires:  pkgconfig(gck-2)
BuildRequires:  pkgconfig(gcr-4) >= 3.9.0
BuildRequires:  pkgconfig(gdk-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.74.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12.0
BuildRequires:  pkgconfig(gtk4-unix-print)
BuildRequires:  pkgconfig(hogweed) >= 3.2
BuildRequires:  pkgconfig(icu-uc) >= 4.6
BuildRequires:  pkgconfig(iso-codes) >= 0.35
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.beta
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsecret-1) >= 0.19.0
BuildRequires:  pkgconfig(libsoup-3.0) >= 2.99.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.12
BuildRequires:  pkgconfig(libxslt) >= 1.1.7
BuildRequires:  pkgconfig(nettle) >= 3.4
BuildRequires:  pkgconfig(sqlite3) >= 3.22
BuildRequires:  pkgconfig(webkitgtk-6.0) >= 2.43.4
BuildRequires:  pkgconfig(webkitgtk-web-process-extension-6.0) >= 2.43.4
Requires:       %{name}-branding = %{version}
Requires:       iso-codes
Recommends:     ca-certificates
Recommends:     gnome-keyring
Recommends:     gstreamer-plugins-rs

%description
Epiphany is a Web browser for the GNOME Desktop. Its principles are
simplicity and standards compliance.

%package branding-upstream
Summary:        GNOME Web Browser -- Upstream default bookmarks and user agent string
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-upstream
Epiphany is a Web Browser for the GNOME Desktop. Its principles are
simplicity and standards compliance.

This package provides the upstream default bookmarks and user agent
string.

%package -n gnome-shell-search-provider-epiphany
Summary:        Epiphany Search Provider for GNOME Shell
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-epiphany
Epiphany is a Web browser for the GNOME Desktop.

This package contains a search provider to enable GNOME Shell to get
search results from Web (epiphany)

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D developer_mode=false \
	-D unit_tests=disabled \
	-D granite=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc CONTRIBUTING.md NEWS README.md TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/epiphany
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Epiphany.appdata.xml
%{_datadir}/applications/org.gnome.Epiphany.desktop
%exclude %{_datadir}/epiphany/default-bookmarks.rdf
%{_datadir}/epiphany/
%{_datadir}/glib-2.0/schemas/org.gnome.Epiphany.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.epiphany.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Epiphany*
%{_mandir}/man1/epiphany.1%{ext_man}
%dir %{_libdir}/epiphany
%dir %{_libdir}/epiphany/web-process-extensions
%{_libdir}/epiphany/web-process-extensions/libephywebprocessextension.so
%{_libdir}/epiphany/web-process-extensions/libephywebextension.so
%{_libdir}/epiphany/libephymain.so
%{_libdir}/epiphany/libephymisc.so
%{_libdir}/epiphany/libephysync.so
%dir %{_libexecdir}/epiphany
%{_libexecdir}/epiphany/ephy-profile-migrator
%{_libexecdir}/epiphany-webapp-provider
%{_datadir}/dbus-1/services/org.gnome.Epiphany.WebAppProvider.service

%files branding-upstream
%{_datadir}/epiphany/default-bookmarks.rdf

%files -n gnome-shell-search-provider-epiphany
%{_datadir}/dbus-1/services/org.gnome.Epiphany.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Epiphany.SearchProvider.ini
%{_libexecdir}/epiphany-search-provider

%files lang -f %{name}.lang

%changelog
