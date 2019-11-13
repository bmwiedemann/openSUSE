#
# spec file for package kipi-plugins
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


%bcond_without lang
Name:           kipi-plugins
Version:        19.08.3
Release:        0
Summary:        KDE Plug-Ins for Image Manipulation
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkipi-devel >= 16.04.0
BuildRequires:  libmediawiki-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
Recommends:     %{name}-lang
Obsoletes:      kipi-plugins-acquireimage < %{version}
Obsoletes:      kipi-plugins-geolocation < %{version}
Obsoletes:      kipi-plugins5 < %{version}
Provides:       kipi-plugins5 = %{version}
Obsoletes:      kipi-plugin-icons < %{version}
Provides:       kipi-plugin-icons = %{version}

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
%make_jobs VERBOSE=1

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
