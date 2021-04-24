#
# spec file for package mobipocket
#
# Copyright (c) 2021 SUSE LLC
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


%define rname kdegraphics-mobipocket
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           mobipocket
Version:        21.04.0
Release:        0
Summary:        E-book plugin and library
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)

%description
Mobipocket E-book support for Okular.

%package devel
Summary:        E-book plugin and library
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description devel
Mobipocket E-book plugin and library.

This package provides development files for mobipocket
library

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_kf5_appstreamdir}/org.kde.kdegraphics-mobipocket.metainfo.xml
%{_kf5_libdir}/libqmobipocket.so.*
%{_kf5_plugindir}/mobithumbnail.so
%{_kf5_servicesdir}/mobithumbnail.desktop

%files devel
%license COPYING
%{_includedir}/qmobipocket/
%{_kf5_cmakedir}/QMobipocket/
%{_kf5_libdir}/libqmobipocket.so

%changelog
