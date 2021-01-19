#
# spec file for package kdiagram
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


%bcond_without lang
Name:           kdiagram
Version:        2.8.0
Release:        0
Summary:        Powerful libraries (KChart, KGantt) for creating business diagrams
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-linguist-devel >= 5.12.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.12.0
BuildRequires:  cmake(Qt5Svg) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0

%description
%{summary}

%package -n libKChart2
Summary:        KChart library for kdiagram
Group:          System/Libraries
Recommends:     libkchart-lang = %{version}
Provides:       libkchart = %{version}

%description -n libKChart2
This package contains the KChart libraries from the kdiagram package.

%package -n libKGantt2
Summary:        Gantt chart implementation for kdiagram
Group:          System/Libraries
Recommends:     libkgantt-lang = %{version}
Provides:       libkgantt = %{version}

%description -n libKGantt2
This package contains the KGantt libraries from the kdiagram package.

%lang_package -n libkgantt

%lang_package -n libkchart

%package devel
Summary:        Development package for the KDiagram libraries
Group:          System/Libraries/KDE
Requires:       libKChart2 = %{version}
Requires:       libKGantt2 = %{version}
Requires:       cmake(Qt5Core) >= 5.12.0
Requires:       cmake(Qt5PrintSupport) >= 5.12.0
Requires:       cmake(Qt5Svg) >= 5.12.0
Requires:       cmake(Qt5Widgets) >= 5.12.0

%description devel
Development package for the KDiagram libraries

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang kgantt --with-qt --without-mo
  %find_lang kchart --with-qt --without-mo
%endif

%post -n libKChart2 -p /sbin/ldconfig
%postun -n libKChart2 -p /sbin/ldconfig
%post -n libKGantt2 -p /sbin/ldconfig
%postun -n libKGantt2 -p /sbin/ldconfig

%files -n libKChart2
%license LICENSE.GPL.txt
%{_libdir}/libKChart.so.*

%files -n libKGantt2
%license LICENSE.GPL.txt
%{_libdir}/libKGantt.so.*

%if %{with lang}
%files -n libkchart-lang -f kchart.lang
%license LICENSE.GPL.txt

%files -n libkgantt-lang -f kgantt.lang
%license LICENSE.GPL.txt
%endif

%files devel
%license LICENSE.GPL.txt
%{_includedir}/KChart/
%{_includedir}/kchart_version.h
%{_includedir}/KGantt/
%{_includedir}/kgantt_version.h
%{_libdir}/libKChart.so
%{_libdir}/libKGantt.so
%{_libdir}/qt5/mkspecs/modules/qt_KChart.pri
%{_libdir}/qt5/mkspecs/modules/qt_KGantt.pri
%{_libdir}/cmake/KChart/
%{_libdir}/cmake/KGantt/

%changelog
