#
# spec file for package kdegraphics-thumbnailers
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdegraphics-thumbnailers
Version:        24.05.1
Release:        0
Summary:        Graphics file thumbnail generators
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
This package allows KDE applications to show thumbnails
and previews of graphics files.

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%files
%license COPYING*
%{_kf6_appstreamdir}/org.kde.kdegraphics-thumbnailers.metainfo.xml
%{_kf6_plugindir}/kf6/thumbcreator/

%changelog
