#
# spec file for package librepo
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2021 Neal Gompa <ngompa13@gmail.com>.
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


%ifarch %{arm} aarch64 riscv64
# Don't run tests on ARM and RISC-V for now. There are problems
# with performance on the builders and often these time out.
%bcond_with tests
%else
%bcond_without tests
%endif

# zchunk is only available in Leap 15.1 and newer
%if 0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550
%bcond_without zchunk
%else
%bcond_with zchunk
%endif

%define major 0
%define libname %{name}%{major}
%define devname %{name}-devel

Name:           librepo
Version:        1.15.1
Release:        0
Summary:        Repodata downloading library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++

URL:            https://github.com/rpm-software-management/librepo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.52.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= 0.9.11
%endif
BuildRequires:  python-rpm-macros

# prevent provides from nonstandard paths:
%global __provides_exclude ^(%{python3_sitearch}/.*\\.so)$

%description
A library providing C and Python (libcURL like) API for downloading repository
metadata.

%package -n %{libname}
Summary:        Repodata downloading library
Group:          System/Libraries

%description -n %{libname}
A library providing C and Python (libcURL like) API for downloading repository
metadata.

%package -n %{devname}
Summary:        Header files for the Repodata downloading library
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package provides the development files for %{name}.

%package -n python3-librepo
Summary:        Python 3 bindings for the librepo library
Group:          Development/Libraries/Python
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-Flask
BuildRequires:  python3-gpg
BuildRequires:  python3-requests
%endif
BuildRequires:  python3-Sphinx
BuildRequires:  python3-xattr
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# There is no more Python 2 subpackage
Obsoletes:      python2-librepo < 1.9.3

%description -n python3-librepo
This package provides the Python 3 bindings for the librepo library.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DPYTHON_DESIRED:str=3 %{!?with_zchunk:-DWITH_ZCHUNK=OFF}
%make_build

%check
%if %{with tests}
pushd ./build
make ARGS="-V" test
make clean
popd
%endif

%install
pushd ./build
%make_install
popd

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license COPYING
%{_libdir}/librepo.so.%{major}

%files -n %{devname}
%{_libdir}/librepo.so
%{_libdir}/pkgconfig/librepo.pc
%{_includedir}/librepo/

%files -n python3-librepo
%{python3_sitearch}/librepo

%changelog
