#
# spec file for package qimageblitz
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


%define soname_qt5 libqimageblitz5
%define sover_qt5 1
%if 0%{?suse_version} <= 1500
%bcond_without qt4
%define soname_qt4 libqimageblitz
%define sover_qt4 4
%else
%bcond_with qt4
%endif
Name:           qimageblitz
Version:        0.0.6+svn1515099
Release:        0
Summary:        Graphical effect and filter library for Qt
License:        BSD-2-Clause
Group:          System/Libraries
URL:            https://websvn.kde.org/trunk/kdesupport/qimageblitz
Source0:        %{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE qimageblitz-qt5-fix-soname.patch sor.alexei@meowr.ru -- Change the soname for Qt5 to fix a conflict with Qt4.
Patch0:         qimageblitz-qt5-fix-soname.patch
# PATCH-FIX-UPSTREAM
Patch1:         remove-ansi-option.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
%if %{with qt4}
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
%endif

%description
qimageblitz is a graphical effect and filter library for Qt that
contains many improvements over KDE 3.x's kdefx library including
bugfixes, memory and speed improvements, and MMX/SSE support.

%if %{with qt4}
%package -n %{soname_qt4}%{sover_qt4}
Summary:        Graphical effect and filter library for Qt4
Group:          System/Libraries

%description -n %{soname_qt4}%{sover_qt4}
libqimageblitz is a graphical effect and filter library for Qt4
that contains many improvements over KDE 3.x's kdefx library
including bugfixes, memory and speed improvements, and MMX/SSE
support.
%endif

%package -n %{soname_qt5}-%{sover_qt5}
Summary:        Graphical effect and filter library for Qt5
Group:          System/Libraries

%description -n %{soname_qt5}-%{sover_qt5}
libqimageblitz5 is a graphical effect and filter library for Qt5
that contains many improvements over KDE 3.x's kdefx library
including bugfixes, memory and speed improvements, and MMX/SSE
support.

%if %{with qt4}
%package -n %{soname_qt4}-devel
Summary:        Development files for libqimageblitz4
Group:          Development/Libraries/C and C++
Requires:       %{soname_qt4}%{sover_qt4} = %{version}

%description -n %{soname_qt4}-devel
This package contains development files for libqimageblitz.
%endif

%package -n %{soname_qt5}-devel
Summary:        Development files for libqimageblitz5
Group:          Development/Libraries/C and C++
Requires:       %{soname_qt5}-%{sover_qt5} = %{version}

%description -n %{soname_qt5}-devel
This package contains development files for libqimageblitz5.

%prep
%autosetup -p1

%build
WORKDIR="$PWD"
%define __builddir build-qt5
%cmake -DQT4_BUILD=OFF
make %{?_smp_mflags} V=1

%if %{with qt4}
cd "$WORKDIR"
%define __builddir build-qt4
%cmake -DQT4_BUILD=ON
make %{?_smp_mflags} V=1
%endif

%install
WORKDIR="$PWD"
%define __builddir build-qt5
%cmake_install

%if %{with qt4}
cd "$WORKDIR"
%define __builddir build-qt4
%cmake_install
%endif

%if %{with qt4}
%post -n %{soname_qt4}%{sover_qt4} -p /sbin/ldconfig

%postun -n %{soname_qt4}%{sover_qt4} -p /sbin/ldconfig
%endif

%post -n %{soname_qt5}-%{sover_qt5} -p /sbin/ldconfig

%postun -n %{soname_qt5}-%{sover_qt5} -p /sbin/ldconfig

%if %{with qt4}
%files -n %{soname_qt4}%{sover_qt4}
%if 0%{?suse_version} == 1500
%license COPYING
%else
%doc COPYING
%endif
%doc Changelog README.*
%{_libdir}/%{soname_qt4}.so.%{sover_qt4}*
%endif

%files -n %{soname_qt5}-%{sover_qt5}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc Changelog README.*
%{_libdir}/%{soname_qt5}.so.%{sover_qt5}*

%if %{with qt4}
%files -n %{soname_qt4}-devel
%{_includedir}/qimageblitz/
%{_bindir}/blitztest
%{_libdir}/%{soname_qt4}.so
%{_libdir}/pkgconfig/qimageblitz.pc
%endif

%files -n %{soname_qt5}-devel
%{_includedir}/qimageblitz5/
%{_bindir}/blitztest5
%{_libdir}/%{soname_qt5}.so
%{_libdir}/pkgconfig/qimageblitz5.pc

%changelog
