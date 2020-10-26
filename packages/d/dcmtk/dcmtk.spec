#
# spec file for package dcmtk
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libdcmtk3_6
%define abiversion 15
Name:           dcmtk
Version:        3.6.5
Release:        0
Summary:        DICOM Toolkit
License:        BSD-3-Clause AND Apache-2.0
Group:          Productivity/Scientific/Other
URL:            https://dicom.offis.de/dcmtk.php.en
Source0:        ftp://dicom.offis.de/pub/dicom/offis/software/dcmtk/release/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dcmtk-fix-DCMTKTargets.cmake.patch -- Do not track executables to be able to use dcmtk-devel without dcmtk package
Patch0:         dcmtk-fix-DCMTKTargets.cmake.patch
# PATCH-FIX-OPENSUSE 0001-Link-charls-statically.patch -- avoid file conflict with CharLS-devel
Patch1:         0001-Link-charls-statically.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
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
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       tcpd-devel

%description devel
This package provides development libraries and headers needed to build
software using dcmtk.

%package -n %{libname}
Summary:        DICOM Toolkit
Group:          System/Libraries

%description -n %{libname}
DCMTK is a collection of libraries and applications implementing large
parts the DICOM standard.

%prep
%autosetup -p1

%build
%cmake \
 -DINSTALL_DOCDIR=%{_docdir}/dcmtk \
 -DINSTALL_HTMDIR=%{_docdir}/dcmtk/html \
 -DBUILD_SHARED_LIBS=ON \
 -DDCMTK_WITH_XML=ON \
 -DDCMTK_WITH_OPENSSL=ON \
 -DDCMTK_WITH_SNDFILE=ON \
 -DDCMTK_WITH_ZLIB=ON

%cmake_build

%install
%cmake_install

# Remove zero-length file (fix rpmlint warning)
rm -f %{buildroot}%{_datadir}/dcmtk/wlistdb/OFFIS/lockfile

# Move configuration files from /usr/etc to /etc/
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}

# Move doc files from /usr/share/doc/dcmtk to /usr/share/doc/packages/dcmtk/
mkdir %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}

# Install README file to documentation
install -pm 0644 README %{buildroot}%{_docdir}/dcmtk/

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc CREDITS FAQ README
%config(noreplace) %{_sysconfdir}/dcmtk/*.cfg
%dir %{_sysconfdir}/dcmtk
%doc %{_docdir}/dcmtk/
%{_bindir}/*
%{_datadir}/dcmtk/
%{_mandir}/man1/*

%files devel
%license COPYRIGHT
%{_includedir}/dcmtk/
%{_libdir}/*.so
%{_libdir}/cmake/dcmtk/

%files -n %{libname}
%license COPYRIGHT
%{_libdir}/*.so.%{abiversion}
%{_libdir}/*.so.%{abiversion}.3.6*

%changelog
