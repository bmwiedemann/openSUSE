#
# spec file for package miniupnpc
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define soname 17
%bcond_without python2
Name:           miniupnpc
Version:        2.2.4
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
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
# same "defaults" for all distributions, used in %files below
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

%package -n python2-miniupnpc
Summary:        Universal Plug'n'Play (UPnP) Client Module for Python
Group:          Development/Libraries/Python
Requires:       libminiupnpc%{soname} = %{version}-%{release}

%description -n python2-miniupnpc
The MiniUPnP project offers software which supports the UPnP Internet Gateway
Device (IGD) specifications.

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
%make_build \
     CC="gcc" BUILD=$PWD/build \
     OPTFLAGS="%{optflags}" \
     PYTHON="python3"

%python_build

%install
%make_install INSTALLDIRLIB=%{_libdir} LIBDIR=%{_lib}

%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# Remove static libs
rm -f %{buildroot}%{_libdir}/*.a
# The man page should be non executable
chmod -x %{buildroot}%{_mandir}/man3/miniupnpc.3.gz

%post   -n libminiupnpc%{soname} -p /sbin/ldconfig
%postun -n libminiupnpc%{soname} -p /sbin/ldconfig

%files
%{_bindir}/upnpc
%{_bindir}/external-ip
%{_mandir}/man3/miniupnpc.3%{?ext_man}

%files -n libminiupnpc%{soname}
%doc Changelog.txt README
%license LICENSE
%{_libdir}/libminiupnpc.so.%{soname}

%files -n libminiupnpc-devel
%{_includedir}/miniupnpc/
%{_libdir}/libminiupnpc.so
%{_libdir}/pkgconfig/miniupnpc.pc

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-miniupnpc
%doc Changelog.txt README
%license LICENSE
%{python2_sitearch}/miniupnpc*
%endif

%files %{python_files miniupnpc}
%doc Changelog.txt README
%license LICENSE
%{python_sitearch}/miniupnpc*

%changelog
