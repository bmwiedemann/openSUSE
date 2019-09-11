#
# spec file for package openjpeg
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver 1
Name:           openjpeg
Version:        1.5.2
Release:        0
Summary:        An open-source JPEG 2000 codec
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
Url:            http://www.openjpeg.org/
Source0:        http://downloads.sourceforge.net/%{name}.mirror/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM openjpeg-1.5.1-cmake_libdir.patch asterios.dramis@gmail.com -- Fix libopenjpeg.pc symlink (taken from Fedora)
Patch0:         openjpeg-1.5.1-cmake_libdir.patch
# PATCH-FIX-OPENSUSE openjpeg-1.5.1-soname.patch asterios.dramis@gmail.com -- Revert soname bump compared to 1.5.0 release (for now, remove patch in 2.0 release) (taken from Fedora)
# See "http://code.google.com/p/openjpeg/source/browse/tags/version.1.5.1/CMakeLists.txt". The change was introduced in 1.5.1 but soname can remain the same between 1.5.0 and 1.5.1 versions.
Patch1:         openjpeg-1.5.1-soname.patch
# PATCH-FIX-UPSTREAM openjpeg-bsc999817-cve2016-7445-null-deref.patch CVE-2016-7445 bsc#999817 hpj@suse.com -- Fix null pointer dereference in convert.c
Patch2:         openjpeg-bsc999817-cve2016-7445-null-deref.patch
# PATCH-FIX-UPSTREAM openjpeg-fast-math.patch only compile and not link with fast-math bsc#1059440
Patch3:         openjpeg-fast-math.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)

%description
OpenJPEG library is an open-source JPEG 2000 codec written in C. It has been
developed in order to promote the use of JPEG 2000, the new still-image
compression standard from the Joint Photographic Experts Group (JPEG).

%package devel
Summary:        Development files for the OpenJPEG library
Group:          Development/Libraries/C and C++
Requires:       libopenjpeg%{so_ver} = %{version}

%description devel
This package contains header files and libraries needed for developing programs
using the OpenJPEG library.

%package -n libopenjpeg%{so_ver}
Summary:        An open-source JPEG 2000 codec
Group:          System/Libraries

%description -n libopenjpeg%{so_ver}
OpenJPEG library is an open-source JPEG 2000 codec written in C. It has been
developed in order to promote the use of JPEG 2000, the new still-image
compression standard from the Joint Photographic Experts Group (JPEG).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/Doxyfile.dox.cmake.in

%build
%cmake \
	-DOPENJPEG_INSTALL_LIB_DIR:PATH=%{_lib} \
	-DOPENJPEG_INSTALL_DOC_DIR=%{_docdir}/%{name} \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_BUILD_TYPE=release \
	-DBUILD_DOC=ON \
	-DUSE_SYSTEM_GETOPT=ON \
	-DBUILD_THIRDPARTY=OFF
make %{?_smp_mflags}

%install
%cmake_install

# Install devel docs manually in order to fix rpmlint warning "files-duplicate"
cp -a build/doc/html/ %{buildroot}%{_docdir}/%{name}-devel/

# Compatibility symlink
ln -s openjpeg-1.5/openjpeg.h %{buildroot}%{_includedir}/openjpeg.h

%fdupes -s %{buildroot}

%post -n libopenjpeg%{so_ver} -p /sbin/ldconfig
%postun -n libopenjpeg%{so_ver} -p /sbin/ldconfig

%files
%doc AUTHORS CHANGES LICENSE NEWS README THANKS
%{_bindir}/image_to_j2k
%{_bindir}/j2k_dump
%{_bindir}/j2k_to_image
%{_mandir}/man1/image_to_j2k.1%{ext_man}
%{_mandir}/man1/j2k_dump.1%{ext_man}
%{_mandir}/man1/j2k_to_image.1%{ext_man}

%files devel
%doc %{_docdir}/%{name}-devel/
%{_includedir}/openjpeg-1.5/
%{_includedir}/openjpeg.h
%{_libdir}/pkgconfig/libopenjpeg.pc
%{_libdir}/pkgconfig/libopenjpeg1.pc
%{_libdir}/openjpeg-1.5/
%{_libdir}/libopenjpeg.so
%{_mandir}/man3/libopenjpeg.3%{ext_man}

%files -n libopenjpeg%{so_ver}
%{_libdir}/libopenjpeg.so.%{version}
%{_libdir}/libopenjpeg.so.%{so_ver}*

%changelog
