#
# spec file for package KEALib
#
# Copyright (c) 2023 SUSE LLC
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


%define soversion 1_5
%define sourcename kealib
%bcond_with gdal_plugin
Name:           KEALib
Version:        1.5.0
Release:        0
Summary:        An implementation of the GDAL data model
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.KEALib.org/
Source0:        https://github.com/ubarsc/kealib/releases/download/%{sourcename}-%{version}/%{sourcename}-%{version}.tar.gz
Patch0:         0001-fix-shebang-interpreter.patch
BuildRequires:  cmake >= 2.8.10
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel
%if %{with gdal_plugin}
BuildRequires:  gdal-devel
%endif

%description
KEALib provides an implementation of the GDAL data model. The format
supports raster attribute tables, image pyramids, meta-data and
built-in statistics while also handling large files and compression
throughout.

Based on the HDF5 standard, it also provides a base from which other
formats can be derived and is a choice for long term data archiving.
An independent software library (libkea) provides access to the KEA
image format and a GDAL driver allowing KEA images to be used from
any GDAL supported software.

%package devel
Summary:        Header files for KEALib
Group:          Development/Languages/C and C++
Requires:       libkea%{soversion} = %{version}
Provides:       libkea%{soversion}-devel
Provides:       libkea-devel

%description devel
KEALib provides an implementation of the GDAL data model.

Development Libraries for KEALib.

%package -n libkea%{soversion}
Summary:        An implementation of the GDAL data model
Group:          System/Libraries

%description -n libkea%{soversion}
KEALib provides an implementation of the GDAL data model.

%package -n gdal-plugin-kealib
Summary:        KEA plugin for GDAL
Group:          System/Libraries

%description -n gdal-plugin-kealib
KEALib plugin for GDAL.

%prep
%autosetup -n %{sourcename}-%{version} -p1

%build
%cmake \
  -DGDAL_INCLUDE_DIR:STRING=%{_includedir}/gdal \
  -DGDAL_LIB_PATH:STRING=%{_libdir} \
  -DHDF5_INCLUDE_DIR:STRING=%{_includedir} \
  -DHDF5_LIB_PATH:STRING=%{_libdir} \
%if %{with gdal_plugin}
  -DLIBKEA_WITH_GDAL:BOOL=ON
%else
  -DLIBKEA_WITH_GDAL:BOOL=OFF
%endif

cp ../build/include/libkea/kea-config.h ../include/libkea/kea-config.h
%cmake_build

%install
%cmake_install

%if %{__isa_bits} == 64
mv %{buildroot}%{_prefix}/lib %{buildroot}/%{_libdir}
%endif

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
%ctest

%post -n libkea%{soversion} -p /sbin/ldconfig

%postun	-n libkea%{soversion} -p /sbin/ldconfig

%files devel
%{_bindir}/kea-config
%dir %{_includedir}/libkea
%{_includedir}/libkea/KEAAttributeTable.h
%{_includedir}/libkea/KEAAttributeTableFile.h
%{_includedir}/libkea/KEAAttributeTableInMem.h
%{_includedir}/libkea/KEACommon.h
%{_includedir}/libkea/KEAException.h
%{_includedir}/libkea/KEAImageIO.h
%{_includedir}/libkea/kea-config.h
%{_includedir}/libkea/kea_export.h

%{_libdir}/libkea.so

%files -n libkea%{soversion}
%{_libdir}/libkea.so.*

%if %{with gdal_plugin}
%files -n gdal-plugin-kealib
%dir %{_libdir}/gdalplugins
%{_libdir}/gdalplugins/gdal_KEA.so
%endif

%changelog
