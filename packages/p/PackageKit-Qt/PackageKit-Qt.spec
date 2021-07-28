#
# spec file for package PackageKit-Qt
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


%define pkqt   packagekitqt5
%define major 1
Name:           PackageKit-Qt
Version:        1.0.2
Release:        0
Summary:        Simple software installation management software
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://github.com/hughsie/PackageKit-Qt
Source:         https://github.com/hughsie/PackageKit-Qt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM boo#1103678
Patch4:         0001-Fix-PackageKit-not-emitting-network-state-changed-signal.patch
BuildRequires:  PackageKit-devel >= %{version}
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)

%description
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package -n lib%{pkqt}-%{major}
Summary:        Simple software installation management software
Group:          System/Libraries

%description -n lib%{pkqt}-%{major}
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package -n %{pkqt}-devel
Summary:        Simple software installation management software
Group:          Development/Libraries/C and C++
Requires:       lib%{pkqt}-%{major} = %{version}
# PackageKit-Qt used to be Qt4 based until 0.9.6; then it turned into a Qt5 package (no more Qt4 support)
# For this reason, we now have to obsolete the former 2nd spec file names
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
Provides:       %{name}5-devel = %{version}
Obsoletes:      %{name}5-devel < %{version}

%description -n %{pkqt}-devel
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%prep
%setup -q
%autopatch -p1

%build
mkdir build
cd build
# FIXME: you should use %%cmake macros
cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  ..
%make_build

%install
cd build
%make_install

%post -n lib%{pkqt}-%{major} -p /sbin/ldconfig
%postun -n lib%{pkqt}-%{major} -p /sbin/ldconfig

%files -n lib%{pkqt}-%{major}
%license COPYING
%doc NEWS AUTHORS README.md
%{_libdir}/libpackagekitqt5.so.*

%files -n %{pkqt}-devel
%doc TODO MAINTAINERS
%{_libdir}/libpackagekitqt5.so
%{_libdir}/cmake/packagekitqt5/
%{_libdir}/pkgconfig/packagekitqt5.pc
%{_includedir}/packagekitqt5/

%changelog
