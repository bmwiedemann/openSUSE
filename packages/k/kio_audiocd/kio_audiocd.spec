#
# spec file for package kio_audiocd
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


%define rname audiocd-kio
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kio_audiocd
Version:        22.12.1
Release:        0
Summary:        KDE I/O Slave for Audio CDs
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  libvorbis-devel
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5CompactDisc)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(Phonon4Qt5)

%description
This package contains an KIO slave to access audio CDs.

%package devel
Summary:        Development package for kio_audiocd
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description devel
This package contains the development files for the audiocd kio slave

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/audiocd/
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/audiocd/
%dir %{_kf5_sharedir}/konqsidebartng
%dir %{_kf5_sharedir}/konqsidebartng/virtual_folders
%dir %{_kf5_sharedir}/konqsidebartng/virtual_folders/services
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%{_kf5_appstreamdir}/org.kde.kio_audiocd.metainfo.xml
%{_kf5_configkcfgdir}/audiocd_*_encoder.kcfg
%{_kf5_debugdir}/kio_audiocd.categories
%{_kf5_debugdir}/kio_audiocd.renamecategories
%{_kf5_libdir}/libaudiocdplugins.so.*
%{_kf5_plugindir}/kcm_audiocd.so
%{_kf5_plugindir}/kf5/kio/audiocd.so
%{_kf5_plugindir}/libaudiocd_encoder_*.so
%{_kf5_servicesdir}/audiocd.desktop
%{_kf5_sharedir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_kf5_sharedir}/solid/actions/solid_audiocd.desktop

%files devel
%{_includedir}/audiocdencoder.h
%{_includedir}/audiocdplugins_export.h
%{_kf5_libdir}/libaudiocdplugins.so

%files lang -f %{name}.lang

%changelog
