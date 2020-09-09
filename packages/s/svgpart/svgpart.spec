#
# spec file for package svgpart
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           svgpart
Version:        20.08.1
Release:        0
Summary:        SVG viewer component
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://projects.kde.org/projects/kde/kdegraphics/svgpart
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
An SVG viewer component for KDE (KPart).

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/svgpart.so
%{_kf5_servicesdir}/svgpart.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
