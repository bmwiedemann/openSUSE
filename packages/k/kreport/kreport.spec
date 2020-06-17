#
# spec file for package kreport
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 4
Name:           kreport
Version:        3.2.0
Release:        0
Summary:        Framework for creation and generation of reports
License:        LGPL-2.0-only
Group:          Productivity/Office/Other
URL:            https://community.kde.org/KReport
Source0:        https://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-kexi-build-with-GCC-10.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kproperty-devel
BuildRequires:  python-base
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang

%description
A framework for creation and generation of reports in multiple formats

%package -n libKReport3-%{sover}
Summary:        The library for the Report Creation and generation Framework
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKReport3-%{sover}
The main library for the Report creation and generation framework

%package devel
Summary:        Development package for KReport
Group:          Development/Libraries/KDE
Requires:       kproperty-devel
Requires:       libKReport3-%{sover} = %{version}

%description devel
Development package for the Report Creation and Generation framework

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang %{name} %{name}.lang --all-name --with-qt

  # The pkgconfig files contain incorrect stuff
  rm -f %{buildroot}%{_libdir}/pkgconfig/KReport3.pc

%post -n libKReport3-%{sover} -p /sbin/ldconfig
%postun -n libKReport3-%{sover} -p /sbin/ldconfig

%files -n libKReport3-%{sover}
%license COPYING.LIB
%{_libdir}/libKReport3.so.*

%files
%{_datadir}/kreport3/
%{_kf5_servicetypesdir}/kreport_elementplugin.desktop
%{_kf5_plugindir}/kreport3/

%files devel
%license COPYING*
%{_includedir}/KReport3/
%{_libdir}/cmake/KReport3/
%{_libdir}/libKReport3.so
#%%{_libdir}/pkgconfig/KReport3.pc
%{_kf5_mkspecsdir}/qt_KReport3.pri

%files lang -f %{name}.lang

%changelog
