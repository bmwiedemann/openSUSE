#
# spec file for package kdiagram
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


%bcond_without lang
Name:           kdiagram
Version:        2.6.1
Release:        0
Summary:        Powerful libraries (KChart, KGantt) for creating business diagrams
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-linguist-devel >= 5.6.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.6.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{summary}

%package -n libKChart2
Summary:        KChart library for kdiagram
Group:          System/Libraries
Recommends:     libkchart-lang = %{version}

%description -n libKChart2
This package contains the KChart libraries from the kdiagram package.

%package -n libKGantt2
Summary:        Gantt chart implementation for kdiagram
Group:          System/Libraries
Recommends:     libkgantt-lang = %{version}

%description -n libKGantt2
This package contains the KGantt libraries from the kdiagram package.

%package -n libkgantt-lang
Summary:        Translation for the KGantt library
Group:          System/Localization
Requires:       libKGantt2 = %{version}
Provides:       libkgantt-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:libKGantt2)
BuildArch:      noarch

%description -n libkgantt-lang
Translatons for the KGantt library

%package -n libkchart-lang
Summary:        Translation for the KChart library
Group:          System/Localization
Requires:       libKChart2 = %{version}
Provides:       libkchart-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:libKChart2)
BuildArch:      noarch

%description -n libkchart-lang
Translatons for the KChart library


%package devel
Summary:        Development package for the KDiagram libraries
Group:          System/Libraries/KDE
Requires:       libKChart2 = %{version}
Requires:       libKGantt2 = %{version}
Requires:       pkgconfig(Qt5Core) >= 5.2.0
Requires:       pkgconfig(Qt5Svg) >= 5.2.0
Requires:       pkgconfig(Qt5Widgets) >= 5.2.0

%description devel
Development package for the KDiagram libraries

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang kgantt_qt --with-qt --without-mo --all-name
  %find_lang kchart_qt --with-qt --without-mo --all-name

%post -n libKChart2 -p /sbin/ldconfig
%postun -n libKChart2 -p /sbin/ldconfig
%post -n libKGantt2 -p /sbin/ldconfig
%postun -n libKGantt2 -p /sbin/ldconfig

%files -n libKChart2
%defattr(-,root,root)
%{_libdir}/libKChart.so.*

%files -n libKGantt2
%defattr(-,root,root)
%{_libdir}/libKGantt.so.*

%files -n libkchart-lang -f kchart_qt.lang
%defattr(-,root,root)
%exclude %{_datadir}/locale/*/LC_MESSAGES/kgantt_qt.qm

%files -n libkgantt-lang -f kgantt_qt.lang
%defattr(-,root,root)
%exclude %{_datadir}/locale/*/LC_MESSAGES/kchart_qt.qm

%files devel
%defattr(-,root,root)
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
