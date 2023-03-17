#
# spec file for package geotiff
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


%define sover   5
%define libname lib%{name}%{sover}
Name:           geotiff
Version:        1.7.1
Release:        0
Summary:        Library to handle georeferenced TIFF
License:        MIT AND SUSE-Public-Domain
Group:          Productivity/Scientific/Other
URL:            https://github.com/OSGeo/libgeotiff
Source0:        https://github.com/OSGeo/libgeotiff/releases/download/%{version}/libgeotiff-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(proj) >= 6.0
BuildRequires:  pkgconfig(zlib)

%description
This library is designed to permit the extraction and parsing of the
"GeoTIFF" Key directories, as well as definition and installation of
GeoTIFF keys in new files.

%package devel
Summary:        GeoTIFF header files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(proj) >= 6.0
Provides:       lib%{name}-devel = %{version}

%description devel
Header files for GeoTIFF library.

This library is designed to permit the extraction and parsing of the
"GeoTIFF" Key directories, as well as definition and installation of
GeoTIFF keys in new files.

%package -n %{libname}
Summary:        Shared libraries for GeoTIFF library
Group:          System/Libraries

%description -n %{libname}
Shared libraries for GeoTIFF library.

This library is designed to permit the extraction and parsing of the
"GeoTIFF" Key directories, as well as definition and installation of
GeoTIFF keys in new files.

%prep
%autosetup -n lib%{name}-%{version}

%build
export CFLAGS="%{optflags} $CFLAGS -g -fstack-protector -fno-strict-aliasing -D _BSD_SOURCE"
export CXXFLAGS="%{optflags} $CXXFLAGS -g -fstack-protector -fno-strict-aliasing"
%configure \
	--prefix=%{_prefix} \
	--includedir=%{_includedir}/lib%{name} \
	--with-proj \
	--with-jpeg \
	--with-zip \
	--with-pic \
	--enable-static=no \
	--enable-debug=yes
%make_build

%install
%make_install

# install pkgconfig file
cat > libgeotiff.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/lib%{name}

Name:           %{libname}
Version:        %{version}
Description: GeoTIFF file format library
Libs: -L%{_libdir} -l%{name}
Cflags: -I%{_includedir}/lib%{name}
EOF

install -Dpm 0644 lib%{name}.pc \
  %{buildroot}%{_libdir}/pkgconfig/lib%{name}.pc
# do not ship la files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE COPYING
%doc ChangeLog README NEWS
%{_bindir}/geotifcp
%{_bindir}/listgeo
%{_bindir}/applygeo
%{_mandir}/man1/listgeo.1%{?ext_man}
%{_mandir}/man1/applygeo.1%{?ext_man}
%{_mandir}/man1/geotifcp.1%{?ext_man}

%files -n %{libname}
%license LICENSE COPYING
%doc ChangeLog README NEWS
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%defattr(0644,root,root,0755)
%license LICENSE COPYING
%doc ChangeLog README NEWS
%dir %{_includedir}/lib%{name}
%{_includedir}/lib%{name}/*.h
%{_includedir}/lib%{name}/*.inc
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
