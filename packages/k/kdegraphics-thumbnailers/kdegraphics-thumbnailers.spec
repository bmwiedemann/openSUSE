#
# spec file for package kdegraphics-thumbnailers
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
Name:           kdegraphics-thumbnailers
Version:        20.08.1
Release:        0
Summary:        Graphics file thumbnail generators
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5KDcraw)
BuildRequires:  cmake(KF5KExiv2)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Gui) >= 5.2.0
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package allows KDE applications to show thumbnails
and previews of graphics files.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license COPYING*
%{_kf5_appstreamdir}/org.kde.kdegraphics-thumbnailers.metainfo.xml
%{_kf5_servicesdir}/
%{_kf5_plugindir}/

%changelog
