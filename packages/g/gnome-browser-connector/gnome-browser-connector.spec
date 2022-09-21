#
# spec file for package gnome-browser-connector
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


Name:           gnome-browser-connector
Version:        42.1
Release:        0
Summary:        GNOME Shell integration for Chrome Extension compatible browsers
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://wiki.gnome.org/action/show/Projects/GnomeShellIntegration
Source:         https://download.gnome.org/sources/%{name}/42/%{name}-%{version}.tar.xz

BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  python3-gobject
Provides:       chrome-gnome-shell = %{version}
Obsoletes:      chrome-gnome-shell < %{version}
# Auto-install when the user uses GNOME Shell and any of the (known) supported browsers
Supplements:    (gnome-shell and MozillaFirefox)
Supplements:    (gnome-shell and chromium)
Supplements:    (gnome-shell and google-chrome-stable)
Supplements:    (gnome-shell and opera)

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and other
Browser Extension, Chrome Extension or WebExtensions capable browsers) and native
host messaging connector that provides integration with GNOME Shell and the
corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md NEWS
%config %{_sysconfdir}/chromium/
%config %{_sysconfdir}/opt/chrome/
%{_bindir}/gnome-browser-connector
%{_bindir}/gnome-browser-connector-host
%{python3_sitelib}/gnome_browser_connector/
%{_libdir}/mozilla/
%{_datadir}/applications/org.gnome.BrowserConnector.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.gnome.BrowserConnector.service
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
