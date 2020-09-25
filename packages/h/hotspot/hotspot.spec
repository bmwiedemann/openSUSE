#
# spec file for package hotspot
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           hotspot
Version:        1.3.0
Release:        0
Summary:        Perf GUI for performance analysis
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Url:            https://github.com/KDAB/hotspot
Source:         https://github.com/KDAB/hotspot/releases/download/v%{version}/hotspot-v%{version}.tar.gz
BuildRequires:  glibc-devel-static
BuildRequires:  threadweaver-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  solid-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  threadweaver-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  libelf-devel
BuildRequires:  libdw-devel
Requires:       perf

%description
Hotspot is a standalone GUI for performance data with an UI like KCachegrind
around Linux perf.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake_kf5 -d build

%install
%cmake_install

%files
%license LICENSE.GPL.txt
%doc README.md
%{_kf5_bindir}/hotspot
%{_kf5_libdir}/libexec/hotspot-perfparser
%{_kf5_libdir}/libexec/elevate_perf_privileges.sh
%{_kf5_iconsdir}/hicolor/*/*/hotspot.png


%changelog
