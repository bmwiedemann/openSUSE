#
# spec file for package chrome-gnome-shell
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


Name:           chrome-gnome-shell
Version:        10.1
Release:        0
Summary:        GNOME Shell integration for Chrome Extension compatible browsers
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source:         http://download.gnome.org/sources/chrome-gnome-shell/10.1/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  jq
BuildRequires:  p7zip-full
BuildRequires:  python3-base
Requires:       python3-requests
# Auto-install when the user uses GNOME Shell and any of the (known) supported browsers
Supplements:    packageand(gnome-shell:MozillaFirefox)
Supplements:    packageand(gnome-shell:chromium)
Supplements:    packageand(gnome-shell:google-chrome-stable)
Supplements:    packageand(gnome-shell:opera)

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and other
Browser Extension, Chrome Extension or WebExtensions capable browsers) and native
host messaging connector that provides integration with GNOME Shell and the
corresponding extensions repository https://extensions.gnome.org.

%prep
%setup -q

%build
%cmake -DPYTHON_EXECUTABLE=$(which python3)
make %{?_smp_mflags}

%install
%cmake_install

%files
%license LICENSE
%doc README.md NEWS
%config %{_sysconfdir}/chromium/
%config %{_sysconfdir}/opt/chrome/
%{_bindir}/chrome-gnome-shell
%{python3_sitelib}/chrome_gnome_shell-0.0.0-*egg-info
%{_libdir}/mozilla/
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_datadir}/icons/gnome/

%changelog
