#
# spec file for package plasma6-browser-integration
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-browser-integration

%bcond_with browser_extension
%bcond_without released

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           plasma6-browser-integration
Version:        6.1.1
Release:        0
Summary:        Helper for the KDE Plasma Browser Integration
License:        GPL-3.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Supplements:    (plasma6-workspace and GoogleChrome)
Supplements:    (plasma6-workspace and MozillaFirefox)
Supplements:    (plasma6-workspace and chromium)
Supplements:    (plasma6-workspace and opera)
Supplements:    (plasma6-workspace and vivaldi)
Provides:       plasma-browser-integration = %{version}
Obsoletes:      plasma-browser-integration < %{version}
Obsoletes:      plasma-browser-integration-lang < %{version}

%description
This package contains a helper binary necessary for the WebExtension to
work.

%package extension
Summary:        WebExtension for KDE Plamsa Browser Integration
Requires:       %{name} = %{version}
Provides:       plasma-browser-integration-extension = %{version}
Obsoletes:      plasma-browser-integration-extension < %{version}

%description extension
This package contains a WebExtension to integrate the browser better into
KDE Plasma.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%if %{with browser_extension}
  -DINSTALL_CHROME_MANIFEST:BOOL=TRUE
%else
  -DINSTALL_CHROME_MANIFEST:BOOL=FALSE
%endif

%kf6_build

%install
%kf6_install

if [ "%{_lib}" != "lib" ]; then
  # Move mozilla native messaging file to correct location
  mv %{buildroot}%{_prefix}/lib/mozilla %{buildroot}%{_libdir}
fi

%find_lang %{name} --all-name

%files
%license COPYING*
%{_kf6_bindir}/plasma-browser-integration-host
%{_kf6_plugindir}/kf6/kded/browserintegrationreminder.so
%dir %{_libdir}/mozilla
%{_libdir}/mozilla/native-messaging-hosts/
%dir %{_sysconfdir}/chromium
%{_sysconfdir}/chromium/native-messaging-hosts/
%dir %{_sysconfdir}/opt/chrome
%{_sysconfdir}/opt/chrome/native-messaging-hosts/
%dir %{_sysconfdir}/opt/edge
%{_sysconfdir}/opt/edge/native-messaging-hosts/
%dir %{_kf6_sharedir}/krunner/dbusplugins
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_kf6_applicationsdir}/org.kde.plasma.browser_integration.host.desktop

%if %{with browser_extension}
%files extension
%license COPYING*
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%{_datadir}/chromium/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%{_datadir}/google-chrome/extensions/cimiefiiaegbelhefglklhhakcgmhkai.json
%endif

%files lang -f %{name}.lang

%changelog
