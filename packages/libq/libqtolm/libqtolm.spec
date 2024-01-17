#
# spec file for package libQtOlm0_1
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

%define libname libQtOlm3_0

Name:           libqtolm
Version:        3.0.1
Release:        0
Summary:        Qt wrapper for libolm
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://gitlab.com/b0/libqtolm
Source0:        https://gitlab.com/b0/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  olm-devel >= 3.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5Network)
#Requires:

%description
This is a Qt wrapper for libolm.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}
Summary:        Qt wrapper for libolm
Group:          Development/Libraries/C and C++

%description -n %{libname}
This is a Qt wrapper for libolm.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%license LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/QtOlm
%{_libdir}/pkgconfig/QtOlm.pc

%changelog
