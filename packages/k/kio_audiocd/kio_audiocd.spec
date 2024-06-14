#
# spec file for package kio_audiocd
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


%define rname audiocd-kio
%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kio_audiocd
Version:        24.05.1
Release:        0
Summary:        KDE I/O Slave for Audio CDs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cdparanoia-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KCddb6)
BuildRequires:  cmake(KCompactDisc6)
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(vorbis)

%description
This package contains an KIO slave to access audio CDs.

%package devel
Summary:        Development package for kio_audiocd
License:        LGPL-2.1-or-later
Requires:       kio_audiocd = %{version}

%description devel
This package contains the development files for the audiocd kio slave

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf6_htmldir}/en/kioslave5/
%{_kf6_applicationsdir}/kcm_audiocd.desktop
%{_kf6_appstreamdir}/org.kde.kio_audiocd.metainfo.xml
%{_kf6_configkcfgdir}/audiocd_*_encoder.kcfg
%{_kf6_debugdir}/kio_audiocd.categories
%{_kf6_debugdir}/kio_audiocd.renamecategories
%{_kf6_libdir}/libaudiocdplugins.so.*
%{_kf6_plugindir}/kf6/kio/audiocd.so
%{_kf6_plugindir}/libaudiocd_encoder_*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_audiocd.so
%dir %{_kf6_sharedir}/konqsidebartng
%dir %{_kf6_sharedir}/konqsidebartng/virtual_folders
%dir %{_kf6_sharedir}/konqsidebartng/virtual_folders/services
%{_kf6_sharedir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/solid_audiocd.desktop

%files devel
%{_includedir}/audiocdplugins/
%{_kf6_libdir}/libaudiocdplugins.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol/
%exclude %{_kf6_htmldir}/en/kioslave5/

%changelog
