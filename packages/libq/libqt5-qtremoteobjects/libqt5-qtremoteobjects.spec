#
# spec file for package libqt5-qtremoteobjects
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


%define qt5_snapshot 0
%define libname libQt5RemoteObjects5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtremoteobjects-everywhere-src-5.15.1
Name:           libqt5-qtremoteobjects
Version:        5.15.1
Release:        0
Summary:        Qt 5 RemoteObjects Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Url:            http://qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  xz
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
processes or computers.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 RemoteObjects Library
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n %{libname}
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
processes or computers.

%package tools
Summary:        Qt 5 RemoteObjects Tools
Group:          Development/Tools/Debuggers
License:        GPL-3.0-with-Qt-Company-Qt-exception-1.1

%description tools
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
processes or computers.

This package contains REPC, a compiler for Qt RemoteObjects API definition files.

%package devel
Summary:        Development files for the Qt5 RemoteObjects library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}

%description devel
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
processes or computers.

You need this package if you want to compile programs with QtRemoteObjects.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 RemoteObjects library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtremoteobjects that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 remoteobjects examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtremoteobjects module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/*.la

# put all the binaries to %%_bindir and symlink them back to %%_qt5_bindir
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
  mv $i ../../../bin/
  ln -s ../../../bin/$i .
done
popd

%files -n %{libname}
%license LICENSE*
%{_libqt5_libdir}/libQt5RemoteObjects.so.*

%files tools
%license LICENSE*
%{_bindir}/repc
%{_libqt5_bindir}/repc

%files private-headers-devel
%license LICENSE*
%{_libqt5_includedir}/QtRemoteObjects/%{so_version}

%files devel
%license LICENSE*
%exclude %{_libqt5_includedir}/QtRemoteObjects/%{so_version}
%{_libqt5_archdatadir}/mkspecs/features/*.prf
%{_libqt5_archdatadir}/mkspecs/features/*.pri
%{_libqt5_archdatadir}/mkspecs/modules/*.pri
%{_libqt5_includedir}/QtRemoteObjects/
%{_libqt5_includedir}/QtRepParser/
%{_libqt5_libdir}/cmake/Qt5RemoteObjects/
%{_libqt5_libdir}/cmake/Qt5RepParser/
%{_libqt5_libdir}/libQt5RemoteObjects.prl
%{_libqt5_libdir}/libQt5RemoteObjects.so
%{_libqt5_libdir}/libQt5RepParser.prl
%{_libqt5_libdir}/pkgconfig/Qt5RemoteObjects.pc
%{_libqt5_libdir}/pkgconfig/Qt5RepParser.pc

%files examples
%{_libqt5_examplesdir}/

%changelog
