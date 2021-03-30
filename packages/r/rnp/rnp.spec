#
# spec file for package rnp
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soname 0-0
Name:           rnp
Version:        0.14.0
Release:        0
Summary:        OpenPGP implementation fully compliant with RFC 4880
License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0
URL:            https://www.rnpgp.com/
Source:         https://github.com/rnpgp/rnp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        https://raw.githubusercontent.com/riboseinc/cmake-versioning/c78a0be/version.cmake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(json-c) >= 0.11
BuildRequires:  pkgconfig(botan-2) >= 2.14.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

%description
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.

%package -n librnp-%{soname}
Summary:        OpenPGP implementation as a C++ library fully compliant with RFC 4880

%description -n librnp-%{soname}
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.
librnp is the library used by RNP for all OpenPGP functions, useful for
developers to build against, different from GPGME.

%package devel
Summary:        Development files for RNP
Requires:       librnp-%{soname} = %{version}

%description devel
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.
This package contains the files needed to build against librnp.

%prep
%setup -q
# for determine_version
cp %{SOURCE2} cmake/

%build
%cmake \
	-DBUILD_SHARED_LIBS=on \
	-DBUILD_TESTING=off
%cmake_build

%install
%cmake_install
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man3
install -m0644 src/rnp/rnp.1 %{buildroot}%{_mandir}/man1/rnp.1
install -m0644 src/rnpkeys/rnpkeys.1 %{buildroot}%{_mandir}/man1/rnpkeys.1
install -m0644 src/lib/librnp.3 %{buildroot}%{_mandir}/man3/librnp.3

%post -n librnp-%{soname} -p /sbin/ldconfig
%postun -n librnp-%{soname} -p /sbin/ldconfig

%files
%license LICENSE*
%{_bindir}/*
%{_mandir}/man1/*

%files -n librnp-%{soname}
%license LICENSE*
%{_libdir}/*.so.0*

%files devel
%license LICENSE*
%doc CHANGELOG.md README.adoc
%{_includedir}/*
%{_libdir}/cmake/rnp
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%changelog
