#
# spec file for package miniupnpc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define soname 21
Name:           miniupnpc
Version:        2.3.3
Release:        0
Summary:        Universal Plug'n'Play (UPnP) Client
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            http://miniupnp.free.fr/
Source:         http://miniupnp.free.fr/files/miniupnpc-%{version}.tar.gz
Source2:        http://miniupnp.free.fr/files/miniupnpc-%{version}.tar.gz.sig
Source3:        http://miniupnp.free.fr/A31ACAAF.asc#/%{name}.keyring
Source99:       baselibs.conf
# PATCH-FIX-SUSE: do not hardcode kernel version in headers
Patch0:         miniupnpc-kernelversion.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
# same "defaults" for all distributions, used in %%files below
%define python_files() -n python3-%{**}
%define python_sitearch %{python3_sitearch}
%endif

%description
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.

%package -n libminiupnpc%{soname}
Summary:        Universal Plug'n'Play (UPnP) Client Library
Group:          System/Libraries

%description -n libminiupnpc%{soname}
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.

%package -n libminiupnpc-devel
Summary:        Universal Plug'n'Play (UPnP) Client Library
Group:          Development/Libraries/C and C++
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%description -n libminiupnpc-devel
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.

%if 0%{?python_subpackage_only}
%package -n python-miniupnpc
Summary:        Universal Plug'n'Play (UPnP) Client Module for Python
Group:          Development/Libraries/Python
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%description -n python-miniupnpc
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.

%else

%package -n python3-miniupnpc
Summary:        Universal Plug'n'Play (UPnP) Client Module for Python
Group:          Development/Libraries/Python
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%description -n python3-miniupnpc
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.
%endif

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%cmake \
  -DUPNPC_BUILD_STATIC=OFF \
  -DUPNPC_BUILD_SHARED=ON \
  -DUPNPC_BUILD_SAMPLE=ON
cd ..
mv build build_cmake
%pyproject_wheel
mv build build_python

%install
mv build_cmake build
%cmake_install
mv build build_cmake
mv build_python build

%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

mv %{buildroot}%{_bindir}/external-ip.sh %{buildroot}%{_bindir}/external-ip
chmod +x %{buildroot}%{_bindir}/external-ip
mv %{buildroot}%{_bindir}/upnp-listdevices-shared %{buildroot}%{_bindir}/upnp-listdevices
mv %{buildroot}%{_bindir}/upnpc-shared %{buildroot}%{_bindir}/upnpc

%ldconfig_scriptlets -n libminiupnpc%{soname}

%check
mv build build_python
mv build_cmake build
%ctest

%files
%{_bindir}/upnpc
%{_bindir}/external-ip
%{_bindir}/upnp-listdevices
%{_mandir}/man3/miniupnpc.3%{?ext_man}

%files -n libminiupnpc%{soname}
%doc Changelog.txt README
%license LICENSE
%{_libdir}/libminiupnpc.so.%{soname}
%{_libdir}/libminiupnpc.so.%{version}

%files -n libminiupnpc-devel
%{_includedir}/miniupnpc/
%{_libdir}/libminiupnpc.so
%{_libdir}/pkgconfig/miniupnpc.pc
%{_libdir}/cmake/miniupnpc

%files %{python_files miniupnpc}
%doc Changelog.txt README
%license LICENSE
%{python_sitearch}/miniupnpc*

%changelog
