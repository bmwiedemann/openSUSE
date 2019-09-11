#
# spec file for package kpmcore
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global sover 7
%bcond_without lang
Name:           kpmcore
Version:        3.3.0
Release:        0
Summary:        KDE Partition Manager core library
License:        GPL-3.0-only
Group:          Productivity/Office/Other
Url:            https://projects.kde.org/projects/extragear/sysadmin/kpmcore
Source:         http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libatasmart-devel
BuildRequires:  libblkid-devel
BuildRequires:  parted-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.7.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       libkpmcore%{sover} = %{version}

%description
Library for managing partitions. Common code for KDE Partition Manager and other projects.

%package devel
Summary:        Development package for KDE Partition Manager core library
Group:          Development/Languages/C and C++
Requires:       libkpmcore%{sover} = %{version}

%description devel
Library for managing partitions. Common code for KDE Partition Manager and other projects.

Development package for kpmcore.

%package -n libkpmcore%{sover}
Summary:        KDE Partition Manager core library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libkpmcore%{sover}
Library for managing partitions. Common code for KDE Partition Manager and other projects.

Main kpmcore library.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang kpmcore
  %endif

%post -n libkpmcore%{sover} -p /sbin/ldconfig
%postun -n libkpmcore%{sover} -p /sbin/ldconfig

%files
%license COPYING.GPL3
%{_kf5_servicetypesdir}/*desktop
%{_kf5_plugindir}/*.so
%{_kf5_servicesdir}/*desktop

%files -n libkpmcore%{sover}
%license COPYING.GPL3
%{_libdir}/libkpmcore.so.*

%files devel
%{_libdir}/cmake/KPMcore/
%{_includedir}/kpmcore/
%{_libdir}/libkpmcore.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
