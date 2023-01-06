#
# spec file for package plasma-browser-integration
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


%define kf5_version 5.98.0
%define qt5_version 5.15.0
%bcond_with browser_extension
%bcond_without released
Name:           plasma-browser-integration
Version:        5.26.5
Release:        0
Summary:        Helper for the KDE Plasma Browser Integration
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            https://cgit.kde.org/plasma-browser-integration.git
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-browser-integration-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-browser-integration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5FileMetaData) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Purpose) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(LibTaskManager)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
Recommends:     %{name}-lang
Supplements:    packageand(plasma5-workspace:MozillaFirefox)
Supplements:    packageand(plasma5-workspace:chromium)
Supplements:    packageand(plasma5-workspace:GoogleChrome)
Supplements:    packageand(plasma5-workspace:opera)
Supplements:    packageand(plasma5-workspace:vivaldi)

%description
This package contains a helper binary necessary for the WebExtension to
work.

%package extension
Summary:        WebExtension for KDE Plamsa Browser Integration
Group:          Productivity/Networking/Web/Utilities
Requires:       %{name} = %{version}

%description extension
This package contains a WebExtension to integrate the browser better into
KDE Plasma.

%lang_package

%prep
%setup -q

%build
%if %{with browser_extension}
%cmake_kf5 -d build -- -DINSTALL_CHROME_MANIFEST=1
%else
%cmake_kf5 -d build -- -DINSTALL_CHROME_MANIFEST=0
%endif

%cmake_build

%install
%kf5_makeinstall -C build
if [ "%{_libdir}" != "%{_prefix}/lib" ]; then
	# Move mozilla native messaging file to correct location
	mv %{buildroot}%{_prefix}/lib/mozilla %{buildroot}%{_libdir}
fi
  %if %{with released}
    %find_lang %{name} --all-name
  %endif

%files
%license COPYING*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kded
%dir %{_kf5_sharedir}/krunner
%dir %{_libdir}/mozilla
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/edge
%{_kf5_bindir}/plasma-browser-integration-host
%{_kf5_plugindir}/kf5/kded/browserintegrationreminder.so
%{_libdir}/mozilla/native-messaging-hosts
%{_sysconfdir}/chromium/native-messaging-hosts
%{_sysconfdir}/opt/chrome/native-messaging-hosts
%{_sysconfdir}/opt/edge/native-messaging-hosts
%{_kf5_sharedir}/krunner/dbusplugins
%{_kf5_applicationsdir}/org.kde.plasma.browser_integration.host.desktop

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

%if %{with released}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
