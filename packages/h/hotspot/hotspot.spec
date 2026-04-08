#
# spec file for package hotspot
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           hotspot
Version:        1.6.0
Release:        0
Summary:        Perf GUI for performance analysis
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/KDAB/hotspot
Source:         hotspot-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  glibc-devel-static
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig

BuildRequires:  cmake(KDDockWidgets-qt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KGraphViewerPart)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(libdebuginfod)
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(qcustomplot-qt6)
%endif

Provides:       bundled(hotspot-PrefixTickLabels)
Provides:       bundled(hotspot-perfparser)

Requires:       binutils
Requires:       perf
Requires:       pkexec

%description
Hotspot is a standalone GUI for performance data with an UI like KCachegrind
around Linux perf.

%prep
%autosetup

%build
%cmake_kf6 -DQT6_BUILD=TRUE
%kf6_build

%install
%kf6_install

%files
%license LICENSE.GPL.txt
%doc README.md
%{_kf6_applicationsdir}/com.kdab.hotspot.desktop
%{_kf6_appstreamdir}/com.kdab.Hotspot.appdata.xml
%{_datadir}/mime/packages/com.kdab.hotspot.xml
%{_kf6_bindir}/hotspot
%{_libexecdir}/hotspot-perfparser
%{_kf6_iconsdir}/hicolor/*/*/hotspot.png
%{_kf6_notificationsdir}/hotspot.notifyrc

%changelog
