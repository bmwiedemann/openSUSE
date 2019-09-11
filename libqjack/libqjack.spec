#
# spec file for package libqjack
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define sover       0
%define _reldate    20170112
Name:           libqjack
Version:        0.0+%{_reldate}
Release:        0
Summary:        Connect to the Jack Sound Server with Qt
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://bitbucket.org/asiniscalchi/qjack
## https://bitbucket.org/asiniscalchi/qjack.git
Source:         qjack-%{_reldate}.tar.bz2
Patch1:         qjack-soname-lib.patch
# PATCH-FIX-UPSTREAM qjack-Qt511.patch
Patch2:         qjack-Qt511.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 4.5
BuildRequires:  glibc-devel
BuildRequires:  jack-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QJack makes you connect with the Jack soundserver system with Qt.

%package -n libqjack%{sover}
Summary:        Connect to the Jack Sound Server with Qt
Group:          System/Libraries

%description -n libqjack%{sover}
QJack makes you connect with the Jack soundserver system with Qt.

%package -n libqjack-devel
Summary:        Connect to the Jack Sound Server with Qt
Group:          Development/Libraries/C and C++
Requires:       jack-devel
Requires:       libqjack%{sover} = %{version}
Requires:       pkgconfig(Qt5Core)

%description -n libqjack-devel
QJack makes you connect with the Jack soundserver system with Qt.

%prep
%setup -q -n qjack-%{_reldate}
%patch1 -p1
%patch2 -p1

%build
install -d build
pushd build
cmake \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
    -DLIB="%{_lib}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
	    ..
make %{?_smp_mflags}
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%post   -n libqjack%{sover} -p /sbin/ldconfig
%postun -n libqjack%{sover} -p /sbin/ldconfig

%files -n libqjack%{sover}
%defattr(-,root,root)
%doc README
%{_libdir}/libqjack.so.%{sover}
%{_libdir}/libqjack.so.%{sover}.*

%files -n libqjack-devel
%defattr(-,root,root)
%{_includedir}/qjack
%{_libdir}/libqjack.so

%changelog
