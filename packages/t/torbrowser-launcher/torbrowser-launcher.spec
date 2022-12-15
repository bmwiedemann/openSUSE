#
# spec file for package torbrowser-launcher
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


Name:           torbrowser-launcher
Version:        0.3.6
Release:        0
Summary:        Tool for launching and easy-updates of Tor Browser
License:        MIT
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/micahflee/torbrowser-launcher
Source0:        https://github.com/micahflee/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  apparmor-abstractions
BuildRequires:  gpg2
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PySocks
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-gpg
BuildRequires:  python3-packaging
BuildRequires:  python3-qt5
BuildRequires:  update-desktop-files
Requires:       gpg2
Requires:       hicolor-icon-theme
Requires:       python3-Parsley
Requires:       python3-PySocks
Requires:       python3-distro
Requires:       python3-gpg
Requires:       python3-packaging
Requires:       python3-qt5
Requires:       python3-requests
Requires:       xmessage
BuildArch:      noarch

%description
Tor Browser Launcher is intended to make Tor Browser easier to
install and use for GNU/Linux users. You install
torbrowser-launcher from your distribution's package manager and
it handles everything else:
  - Downloads and installs the most recent version of Tor Browser
    in your language and for your computer's architecture, or
    launches Tor Browser if it's already installed (Tor Browser
    will automatically update itself)
  - Certificate pins to https://www.torproject.org, so it doesn't
    rely on certificate authorities
  - Verifies Tor Browser's signature for you, to ensure the
    version you downloaded was cryptographically signed by Tor
    developers and was not tampered with
  - Adds "Tor Browser" and "Tor Browser Launcher Settings"
    application launcher to your desktop environment's menu
  - Apparmor profile to limit effect of Tor network compromise
  - Optionally plays a modem sound when you open Tor Browser
    (because Tor is so slow).

%package -n torbrowser-apparmor-profile
Summary:        Apparmor profile for Tor Browser
License:        BSD-3-Clause
Group:          Productivity/Security
Requires:       apparmor-utils

%description -n torbrowser-apparmor-profile
This package provides the apparmor profiles to safeguard against
a Tor network compromise.

%lang_package

%prep
%autosetup -p1

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/torbrowser.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/torbrowser-settings.desktop

%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%if 0%{?suse_version} <= 1315
%dir %{_datadir}/metainfo
%endif
%{_datadir}/metainfo/torbrowser.appdata.xml
%{_datadir}/icons/hicolor/*/apps/torbrowser*.png
%{_datadir}/%{name}/
%{python3_sitelib}/torbrowser_launcher-%{version}-py%{py3_ver}.egg-info
%{python3_sitelib}/torbrowser_launcher/

%files -n torbrowser-apparmor-profile
%license apparmor/license.txt
%config %{_sysconfdir}/apparmor.d/torbrowser.*
%config %{_sysconfdir}/apparmor.d/local/torbrowser.*
%config %{_sysconfdir}/apparmor.d/tunables/torbrowser

%files lang -f %{name}.lang

%changelog
