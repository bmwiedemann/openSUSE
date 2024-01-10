#
# spec file for package zipios
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver  2
Name:           zipios
Version:        2.3.2
Release:        0
Summary:        C++ Library for Reading and Writing Zip Files
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/Zipios/Zipios
Source0:        https://github.com/Zipios/Zipios/archive/refs/tags/%{version}.tar.gz#/zipios-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE zipios-docpath.patch aloisio@gmx.com -- use correct package path
Patch0:         zipios-docpath.patch
# PATCH-FIX-UPSTREAM
Patch1:         https://github.com/Zipios/Zipios/commit/60b8c7bf79e6a4458e4c0d78f5fb14a81f4feac7.patch#/fix_cstdint_include.patch
BuildRequires:  cmake >= 3.10.2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz-gd
BuildRequires:  gcc-c++
BuildRequires:  cmake(Catch2)
BuildRequires:  pkgconfig(zlib)

%description
Zipios is a java.util.zip-like C++ library for reading and writing Zip files.
Access to individual entries is provided through standard C++ iostreams. A
simple read-only virtual file system that mounts regular directories and zip
files is also provided.

%package devel
Summary:        Zipios Header Files
Group:          Development/Libraries/C and C++
Requires:       libzipios%{so_ver} = %{version}
Requires:       pkgconfig(zlib)
Suggests:       %{name}-devel-doc

%description devel
Header files for zipios development.

%package devel-doc
Summary:        Zipios API documentation
Group:          Documentation/HTML
# Package split
Provides:       %{name}-devel:%{_defaultdocdir}/zipios
Conflicts:      %{name}-devel < 2.2.6
BuildArch:      noarch

%description devel-doc
API documentation for zipios.

%package -n libzipios%{so_ver}
Summary:        C++ Library for Reading and Writing Zip Files
Group:          System/Libraries

%description -n libzipios%{so_ver}
Zipios is a java.util.zip-like C++ library for reading and writing Zip files.
Access to individual entries is provided through standard C++ iostreams. A
simple read-only virtual file system that mounts regular directories and zip
files is also provided.

%prep
%autosetup -p1 -n Zipios-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
# Remove the fairly pointless metainfo for a library
rm %{buildroot}%{_datadir}/metainfo/zipios.metainfo.xml

%fdupes %{buildroot}%{_defaultdocdir}

%post -n libzipios%{so_ver} -p /sbin/ldconfig
%postun -n libzipios%{so_ver} -p /sbin/ldconfig

%files devel
%license COPYING
%doc AUTHORS NEWS README.md TODO.md
%{_bindir}/appendzip
%{_bindir}/dosdatetime
%{_bindir}/zcrc32
%{_bindir}/zipdir
%{_bindir}/zipios
%{_datadir}/cmake/ZipIos
%{_includedir}/zipios
%{_libdir}/libzipios.so
%{_mandir}/man3/%{name}*.3%{?ext_man}

%files devel-doc
%doc %{_defaultdocdir}/zipios

%files -n libzipios%{so_ver}
%{_libdir}/libzipios.so.*

%changelog
