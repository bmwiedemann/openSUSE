#
# spec file for package libtins
#
# Copyright (c) 2022 SUSE LLC
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


%define libname  libtins4_4
Name:           libtins
Version:        4.4
Release:        0
Summary:        C++ library for manipulating raw network packets
License:        BSD-2-Clause
Group:          Productivity/Networking/Other
URL:            https://libtins.github.io/
Source0:        https://github.com/mfontanini/%{name}/archive/v%{version}.tar.gz
Patch0:         libtins-4.2_build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)

%description
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package     -n %{libname}
Summary:        C++ library for manipulating raw network packets
Group:          System/Libraries

%description -n %{libname}
The library provides a C++ interface for creating tools which
need to send, receive and manipulate specially crafted packets.

%package        devel
Summary:        Development files for tins
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc CHANGES.md README.md THANKS
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/tins
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%{_libdir}/cmake/libtins

%changelog
