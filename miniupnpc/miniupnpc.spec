#
# spec file for package miniupnpc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define soname 17
%bcond_without python2
Name:           miniupnpc
Version:        2.1
Release:        0
Summary:        Universal Plug'n'Play (UPnP) Client
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            http://miniupnp.free.fr/
Source:         http://miniupnp.free.fr/files/miniupnpc-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-SUSE: do not hardcode kernel version in headers
Patch0:         miniupnpc-kernelversion.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libminiupnpc%{soname} = %{version}-%{release}

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

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} \
     CC="gcc" \
     OPTFLAGS="%{optflags}" \
     PYTHON="python"

%python_build

%install
%make_install INSTALLDIRLIB=%{_libdir}

%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
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

%if %{with python2}
%files -n python2-miniupnpc
%doc Changelog.txt README
%license LICENSE
%{python2_sitearch}/
%endif

%files -n python3-miniupnpc
%doc Changelog.txt README
%license LICENSE
%{python3_sitearch}/

%changelog
