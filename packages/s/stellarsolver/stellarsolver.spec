#
# spec file for package stellarsolver
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 2
%define min_sover 7

Name:           stellarsolver
Version:        2.7
Release:        0
Summary:        Astrometric Solver
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/rlancaste/stellarsolver
Source0:        https://github.com/rlancaste/stellarsolver/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(wcslib)

%description
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor).

%package -n stellarbatchsolver
Summary:        Batch images solver based on stellarsolver

%description  -n stellarbatchsolver
Tool that one could use to automatically solve, extract, and export a large number of images.
This program is primarily meant for data reduction, but could also be used as a test for the library.

%package -n libstellarsolver6-%{sover}
Summary:        Astrometric Solver runtime library
Group:          System/Libraries

%description  -n libstellarsolver6-%{sover}
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor), runtime library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libstellarsolver6-%{sover} = %{version}

%description devel
Development headers and libraries for %{name}.

%lang_package

%prep
%autosetup -p1

sed -i 's/Version=1.4/Version=1.0/' stellarbatchsolver/com.github.rlancaste.stellarbatchsolver.desktop

%build
%cmake_qt6 \
  -DUSE_QT5=OFF \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DBUILD_BATCH_SOLVER=ON
%qt6_build

%install
%qt6_install

%ldconfig_scriptlets -n libstellarsolver6-%{sover}

%files -n stellarbatchsolver
%{_bindir}/StellarBatchSolver
%{_datadir}/applications/com.github.rlancaste.stellarbatchsolver.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128/
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/64x64/
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/128x128/apps/StellarBatchSolverIcon.png
%{_datadir}/icons/hicolor/16x16/apps/StellarBatchSolverIcon.png
%{_datadir}/icons/hicolor/32x32/apps/StellarBatchSolverIcon.png
%{_datadir}/icons/hicolor/48x48/apps/StellarBatchSolverIcon.png
%{_datadir}/icons/hicolor/64x64/apps/StellarBatchSolverIcon.png

%files -n libstellarsolver6-%{sover}
%license LICENSE
%{_libdir}/libstellarsolver6.so.%{sover}
%{_libdir}/libstellarsolver6.so.%{sover}.%{min_sover}

%files devel
%license LICENSE
%{_includedir}/libstellarsolver/
%{_libdir}/cmake/StellarSolver/
%{_libdir}/libstellarsolver6.so
%{_libdir}/pkgconfig/stellarsolver.pc

%changelog
