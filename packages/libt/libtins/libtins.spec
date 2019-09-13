#
# spec file for package libtins
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  3
Name:           libtins
Version:        3.5
Release:        0
Summary:        C++ library for manipulating raw network packets
License:        BSD-2-Clause
Group:          Productivity/Networking/Other
Url:            http://libtins.github.io/
Source0:        https://github.com/mfontanini/libtins/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM build.patch avvissu@yandex.ru-- Place the package file in LIB_INSTALL_DIR/cmake
Patch0:         libtins-3.5_build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package     -n %{name}%{soname}
Summary:        C++ library for manipulating raw network packets
Group:          System/Libraries

%description -n %{name}%{soname}
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for tins
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       libpcap-devel

%description    devel
This package contains header files, and libraries needed to develop
application that use libtins.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DLIBTINS_ENABLE_CXX11=1

%install
%make_install -C build

%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%doc CHANGES.md LICENSE README.md THANKS
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/tins
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%{_libdir}/cmake/tins

%changelog
