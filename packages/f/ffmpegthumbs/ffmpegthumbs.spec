#
# spec file for package ffmpegthumbs
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
Name:           ffmpegthumbs
Version:        20.08.2
Release:        0
Summary:        FFmpeg-based thumbnail creator for video files
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
FFmpeg-based thumbnail creator for video files.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%dir %{_kf5_configkcfgdir}
%{_kf5_appstreamdir}/org.kde.ffmpegthumbs.metainfo.xml
%{_kf5_configkcfgdir}/ffmpegthumbnailersettings5.kcfg
%{_kf5_plugindir}/
%{_kf5_servicesdir}/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING
%endif

%changelog
