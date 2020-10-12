#
# spec file for package kamera
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
Name:           kamera
Version:        20.08.2
Release:        0
Summary:        Digital camera support for KDE applications
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  libgphoto2-devel
BuildRequires:  oxygen-icon-theme-large
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package allows any KDE application to access and manipulate pictures on a digital camera.

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
    %{kf5_find_htmldocs}
  %endif

%package -n kio_kamera
Summary:        KDE I/O Slave for Cameras
License:        GPL-2.0-or-later
Group:          Hardware/Camera
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n kio_kamera
This package contains a KIO slave to access digital cameras.

%post -n kio_kamera -p /sbin/ldconfig
%postun -n kio_kamera -p /sbin/ldconfig

%files -n kio_kamera
%license COPYING*
%doc README
%dir %{_kf5_htmldir}/en/kcontrol
%dir %{_kf5_sharedir}/solid/
%dir %{_kf5_sharedir}/solid/actions/
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/kamera/
%{_kf5_appstreamdir}/org.kde.kamera.metainfo.xml
%{_kf5_plugindir}/kcm_kamera.so
%{_kf5_plugindir}/kio_kamera.so
%{_kf5_servicesdir}/camera.protocol
%{_kf5_servicesdir}/kamera.desktop
%{_kf5_sharedir}/solid/actions/solid_camera.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
