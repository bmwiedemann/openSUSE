#
# spec file for package libdxfrw
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Asterios Dramis <asterios.dramis@gmail.com>.
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


%define so_ver 0

Name:           libdxfrw
Version:        0.6.3+git.20190501
Release:        0
Summary:        Library to read and write DXF files
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/LibreCAD/libdxfrw/
Source0:        %{name}-%{version}.tar.xz
Patch0:         0001-cmake-use-GNUInstallDirs.patch
Patch1:         0002-cmake-set-library-VERSIONs.patch
Patch2:         0003-cmake-add-one-for-dwg2dxf.patch
Patch3:         0004-cmake-generate-and-install-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
libdxfrw is a free C++ library to read and write DXF files in both formats,
ascii and binary form.

%package devel
Summary:        Development files for libdxfrw
Group:          Development/Libraries/C and C++
Requires:       libdxfrw%{so_ver} = %{version}

%description devel
This package includes development files for libdxfrw.

%package tools
Summary:        Tools based on libdxfrw
Group:          Productivity/Graphics/CAD

%description tools
This package includes tools based on libdxfrw.

%package -n libdxfrw%{so_ver}
Summary:        Library to read and write DXF files
Group:          System/Libraries

%description -n libdxfrw%{so_ver}
libdxfrw is a free C++ library to read and write DXF files in both formats,
ascii and binary form.

%prep
%setup -q
%autopatch -p1

%build
%define __builder ninja
%cmake
%make_jobs

%install
%cmake_install

%post -n libdxfrw%{so_ver} -p /sbin/ldconfig

%postun -n libdxfrw%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_includedir}/libdxfrw0/
%{_libdir}/pkgconfig/libdxfrw0.pc
%{_libdir}/libdxfrw.so

%files tools
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/dwg2dxf
%{_mandir}/man1/dwg2dxf.1.gz

%files -n libdxfrw%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libdxfrw.so.%{so_ver}*

%changelog
