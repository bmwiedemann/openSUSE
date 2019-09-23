#
# spec file for package alkimia
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


%define sonum 7
Name:           alkimia
Version:        7.0.2
Release:        0
Summary:        Library with common classes and functionality used by finance applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://kmymoney.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  gmp-devel
BuildRequires:  cmake(Qt5Core) >= 5.2.0
BuildRequires:  cmake(Qt5DBus) >= 5.2.0
BuildRequires:  cmake(Qt5Test) >= 5.2.0

%description
libalkimia is a library with common classes and functionality used by finance
applications.

%package -n libalkimia5-%{sonum}
Summary:        Library with common classes and functionality used by finance applications
Group:          System/Libraries

%description -n libalkimia5-%{sonum}
libalkimia is a library for Qt5 with common classes and functionality used by finance
applications.

%package -n libalkimia5-devel
Summary:        Development Files for libalkimia
Group:          Development/Languages/C and C++
Requires:       libalkimia5-%{sonum} = %{version}

%description -n libalkimia5-devel
The development files for libalkimia.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%post -n libalkimia5-%{sonum} -p /sbin/ldconfig
%postun -n libalkimia5-%{sonum} -p /sbin/ldconfig

%files -n libalkimia5-devel
%license COPYING.LIB
%dir %{_includedir}/alkimia/
%{_includedir}/alkimia/Qt5
%{_kf5_cmakedir}/LibAlkimia5-*/
%{_kf5_libdir}/libalkimia5.so
%{_libdir}/pkgconfig/libalkimia5.pc

%files -n libalkimia5-%{sonum}
%license COPYING.LIB
%doc README.md
%{_kf5_libdir}/libalkimia5.so.%{sonum}*

%changelog
