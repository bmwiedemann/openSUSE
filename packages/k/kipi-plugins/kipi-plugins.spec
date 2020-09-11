#
# spec file for package kipi-plugins
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


%bcond_without lang
Name:           kipi-plugins
Version:        20.08.1
Release:        0
Summary:        KDE Plug-Ins for Image Manipulation
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libmediawiki-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kipi)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
Recommends:     %{name}-lang
Obsoletes:      kipi-plugins-acquireimage < %{version}
Obsoletes:      kipi-plugins-geolocation < %{version}
Obsoletes:      kipi-plugins5 < %{version}
Provides:       kipi-plugins5 = %{version}
Obsoletes:      kipi-plugin-icons < %{version}
Provides:       kipi-plugin-icons = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
A set of plug-ins for the KDE KIPI interface, used by some KDE imaging
applications.

%lang_package

%prep
%setup -q

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/g" common/libkipiplugins/tools/kpversion.h.cmake.in

# Workaround for kde#369517 - vkontakte installs translations even if not built
rm -f po/*/kipiplugin_vkontakte.po

%build
%cmake_kf5 -d build
%cmake_build VERBOSE=1

%install
%kf5_makeinstall -C build

# Not needed, the package doesn't actually provide any shared libraries
rm -f %{buildroot}%{_kf5_libdir}/libKF5kipiplugins.so

%if %{with lang}
%find_lang kipiplugins %{name}.lang

for i in dropbox facebook flashexport flickr googleservices imageshack imgur jalbum kmlexport mediawiki piwigo printimages rajce remotestorage sendimages smug yandexfotki
do
  %find_lang kipiplugin_$i %{name}.lang
done
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/24x24/apps
%{_kf5_applicationsdir}/kipiplugins.desktop
%{_kf5_appstreamdir}/org.kde.kipi_plugins.metainfo.xml
%{_kf5_iconsdir}/hicolor/*/apps/kipi-*.*
%{_kf5_kxmlguidir}/kipi/
%{_kf5_libdir}/libKF5kipiplugins.so*
%{_kf5_plugindir}/kipiplugin_*.so
%{_kf5_sharedir}/kipiplugin_*/
%{_kf5_servicesdir}/kipiplugin_*.desktop

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
