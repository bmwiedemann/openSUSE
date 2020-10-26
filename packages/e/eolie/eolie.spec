#
# spec file for package eolie
#
# Copyright (c) 2020 SUSE LLC
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


# Filter out unwanted Requires
%global __requires_exclude typelib\\(Unity\\)

Name:           eolie
Version:        0.9.100
Release:        0
Summary:        Web browser for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://wiki.gnome.org/Apps/Eolie
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-cairo
Requires:       python3-dateutil
Requires:       python3-gobject
Recommends:     python3-PyFxA
Recommends:     python3-beautifulsoup4
Recommends:     python3-cryptography
Recommends:     python3-pycrypto
Recommends:     python3-requests-hawk
BuildArch:      noarch

%description
Eolie is a Web browser for the GNOME Desktop. It provides:
* Firefox sync support
* Secret password store
* A modern UI

%package -n gnome-shell-search-provider-eolie
Summary:        Eolie Search Provider for GNOME Shell
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-eolie
This package contains a search provider to enable GNOME Shell to get
search results from the Eolie Web browser.

%lang_package

%prep
%autosetup
# Don't use env interpreter so that the rpm dependency detection works
sed -i 's;/usr/bin/env python3;/usr/bin/python3;' eolie.in search-provider/eolie-sp.in

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Eolie.appdata.xml
%{_datadir}/applications/org.gnome.Eolie.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Eolie.gschema.xml
%{_datadir}/icons/hicolor/*/*/org.gnome.Eolie*
%{_datadir}/%{name}
%{python3_sitelib}/%{name}

%files -n gnome-shell-search-provider-eolie
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/dbus-1/services/org.gnome.Eolie.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Eolie.SearchProvider.ini
%{_libexecdir}/%{name}-sp

%files lang -f %{name}.lang

%changelog
