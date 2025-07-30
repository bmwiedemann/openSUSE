#
# spec file for package librepo
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020-2021 Neal Gompa <ngompa13@gmail.com>.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define major 0
%define libname %{name}%{major}
%define devname %{name}-devel
# prevent provides from nonstandard paths:
%global __provides_exclude ^(%{python3_sitearch}/.*\\.so)$
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
Name:           librepo
Version:        1.20.0
Release:        0
Summary:        Repodata downloading library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/rpm-software-management/librepo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.52.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
%if %{with zchunk}
BuildRequires:  pkgconfig(zck) >= 0.9.11
%endif

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
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-xattr
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# There is no more Python 2 subpackage
Obsoletes:      python2-librepo < 1.9.3
%if %{with tests}
BuildRequires:  python3-Flask
BuildRequires:  python3-gpg
BuildRequires:  python3-requests
%endif

%description -n python3-librepo
This package provides the Python 3 bindings for the librepo library.

%prep
%autosetup -p1

%build
%cmake \
	-DPYTHON_DESIRED:str=3 \
	%{!?with_zchunk:-DWITH_ZCHUNK=OFF} \
	%{nil}
%cmake_build

%check
%if %{with tests}
%ctest
%endif

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc README.md
%{_libdir}/librepo.so.%{major}

%files -n %{devname}
%license COPYING
%{_libdir}/librepo.so
%{_libdir}/pkgconfig/librepo.pc
%{_includedir}/librepo/

%files -n python3-librepo
%license COPYING
%{python3_sitearch}/librepo

%changelog
