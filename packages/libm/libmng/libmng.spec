#
# spec file for package libmng
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


%define lname	libmng2
Name:           libmng
Version:        2.0.3
Release:        0
Summary:        Library for Support of MNG and JNG Formats
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://www.libmng.com/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}-devel/%{version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch0:         libmng-1.0.9-dont-leak-zlib-streams.diff
BuildRequires:  cmake
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  man
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%{?suse_build_hwcaps_libs}

%description
This library can handle MNG and JNG formats that contain animated
pictures. These formats should replace the GIF format.

%package -n %{lname}
Summary:        Library for Support of MNG and JNG Formats
Group:          System/Libraries

%description -n %{lname}
This library can handle MNG and JNG formats that contain animated
pictures. These formats should replace the GIF format.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libjpeg-devel
Requires:       liblcms2-devel
Requires:       zlib-devel

%description devel
This library can handle MNG and JNG formats which contain animated
pictures. These formats should replace the GIF format.

This package contains the static library and the header files.

%prep
%autosetup -p0

%build
# This is not zlib licensed and unused, just as a caution, bnc#744320
rm -rf contrib

%cmake \
      -DCMAKE_SKIP_RPATH=ON \
      -DMNG_INSTALL_DOC_DIR=%{_docdir}/%{name} \
      -DBUILD_MAN=ON \
      -DBUILD_STATIC_LIBS=OFF ..
%cmake_build

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README doc/doc.readme doc/libmng.txt
%{_libdir}/libmng.so.*

%files devel
%{_includedir}/*.h
%{_mandir}/*/*
%doc %{_docdir}/libmng/
%{_libdir}/pkgconfig/libmng.pc
%{_libdir}/libmng.so
%{_datadir}/mng-2.0/

%changelog
