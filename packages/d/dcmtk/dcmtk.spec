#
# spec file for package dcmtk
#
# Copyright (c) 2024 SUSE LLC
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


%define abiversion 19
Name:           dcmtk
Version:        3.6.9
Release:        0
Summary:        DICOM Toolkit
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://dicom.offis.de/dcmtk.php.en
Source0:        https://dicom.offis.de/download/dcmtk/dcmtk369/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dcmtk-fix-DCMTKTargets.cmake.patch -- Do not track executables to be able to use dcmtk-devel without dcmtk package
Patch0:         dcmtk-fix-DCMTKTargets.cmake.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Added-check-to-make-sure-HighBit-BitsAllocated.patch
Patch2:         0001-Replaced-call-of-delete-by-delete.patch
Patch3:         0001-Fixed-issue-rendering-invalid-monochrome-image.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kf5-filesystem
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)

%description
DCMTK is a collection of libraries and applications implementing large
parts the DICOM standard.

%package devel
Summary:        Development files for dcmtk
Requires:       libdcmtk%{abiversion} = %{version}
Requires:       tcpd-devel
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libopenjp2)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(libxml-2.0)

%description devel
This package provides development libraries and headers needed to build
software using dcmtk.

%package -n libdcmtk%{abiversion}
Summary:        DICOM Toolkit
Provides:       libdcmtk3_6 = %{version}
Obsoletes:      libdcmtk3_6 < %{version}

%description -n libdcmtk%{abiversion}
DCMTK is a collection of libraries and applications implementing large
parts the DICOM standard.

%prep
%autosetup -p1

%build
%{cmake_kf5 -d build -- \
 -DBUILD_SHARED_LIBS=ON \
 -DDCMTK_WITH_XML=ON \
 -DDCMTK_WITH_OPENSSL=ON \
 -DDCMTK_WITH_SNDFILE=ON \
 -DDCMTK_WITH_ZLIB=ON \
 -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}}

%cmake_build

%install
%kf5_makeinstall -C build

# Remove zero-length file (fix rpmlint warning)
rm %{buildroot}%{_datadir}/dcmtk-%{version}/wlistdb/OFFIS/lockfile

# Move doc files from /usr/share/doc/dcmtk-<version> to /usr/share/doc/packages/dcmtk/
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_docdir}/dcmtk

# Install README file to documentation
install -pm 0644 README %{buildroot}%{_docdir}/dcmtk/

%fdupes %{buildroot}

%check
%ctest

%ldconfig_scriptlets -n libdcmtk%{abiversion}

%files
%license COPYRIGHT
%doc CREDITS FAQ README
%doc %{_docdir}/dcmtk/
%dir %{_sysconfdir}/dcmtk-%{version}
%config(noreplace) %{_sysconfdir}/dcmtk-%{version}/*.cfg
%{_bindir}/*
%{_datadir}/dcmtk-%{version}/
%{_mandir}/man1/*

%files devel
%{_includedir}/dcmtk/
%{_libdir}/*.so
%{_libdir}/cmake/dcmtk/
%{_libdir}/pkgconfig/dcmtk.pc

%files -n libdcmtk%{abiversion}
%license COPYRIGHT
%{_libdir}/*.so.%{abiversion}
%{_libdir}/*.so.%{abiversion}.3.6*

%changelog
