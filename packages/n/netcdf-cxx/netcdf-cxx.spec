#
# spec file for package netcdf-cxx
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define soname 4

Name:           netcdf-cxx
Version:        4.2
Release:        0
Summary:        Old C++ library for the Unidata network Common Data Form
License:        NetCDF
Group:          System/Libraries
Url:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-cxx-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(netcdf)
Requires(post): info
Requires(preun):info

%description
NetCDF (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.
This package provides the old C++ API. It's not recommended for new projects,
but it still works.

%package -n libnetcdf_c++%{soname}
Summary:        Old C++ library for for the Unidata network Common Data Form
Group:          System/Libraries
Provides:       libnetcdf%{soname}:%{_libdir}/libnetcdf_c++.so.%{soname}

%description -n libnetcdf_c++%{soname}
NetCDF (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.
This package provides the old C++ API. It's not recommended for new projects,
but it still works.

%package -n libnetcdf_c++-devel
Summary:        Development files for netcdf_c++
Group:          Development/Libraries/C and C++
Requires:       libnetcdf_c++%{soname} = %{version}
Provides:       libnetcdf-devel:%{_libdir}/libnetcdf_c++.so

%description -n libnetcdf_c++-devel
This package contains the netcdf_c++ header files and shared devel libs.
It's not recommended for new projects, but it still works.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libnetcdf_c++.la

%check
make check

%post -n libnetcdf_c++-devel
%install_info --info-dir=%{_infodir} %{_infodir}/netcdf-cxx.info.*

%preun -n libnetcdf_c++-devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/netcdf-cxx.info.*

%post -n libnetcdf_c++%{soname} -p /sbin/ldconfig

%postun -n libnetcdf_c++%{soname} -p /sbin/ldconfig

%files -n libnetcdf_c++%{soname}
%defattr(0644,root,root,0755)
%doc COPYRIGHT
%{_libdir}/libnetcdf_c++.so.%{soname}*

%files -n libnetcdf_c++-devel
%defattr(0644,root,root,0755)
%{_includedir}/*
%{_libdir}/libnetcdf_c++.so
%{_infodir}/netcdf-cxx.info*

%changelog
