#
# spec file for package rnp
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soname 0
%bcond_with rnp_tests
Name:           rnp
Version:        0.15.2
Release:        0
Summary:        OpenPGP implementation fully compliant with RFC 4880
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.rnpgp.com/
Source:         https://github.com/rnpgp/rnp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
# https://github.com/rnpgp/rnp/issues/1579
BuildRequires:  git
BuildRequires:  gpg2 >= 2.2
BuildRequires:  pkgconfig
BuildRequires:  cmake(json-c) >= 0.11
BuildRequires:  pkgconfig(botan-2) >= 2.14.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(asciidoctor)
%if %{with rnp_tests}
BuildRequires:  gtest
%endif

%description
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.

%package -n librnp%{soname}
Summary:        OpenPGP implementation as a C++ library fully compliant with RFC 4880

%description -n librnp%{soname}
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.
librnp is the library used by RNP for all OpenPGP functions, useful for
developers to build against, different from GPGME.

%package devel
Summary:        Development files for RNP
Requires:       librnp%{soname} = %{version}

%description devel
RNP is a set of OpenPGP (RFC4880) tools, an alternative to GnuPG.
This package contains the files needed to build against librnp.

%prep
%setup -q

%build
%cmake \
	-DBUILD_SHARED_LIBS=on \
	-DDOWNLOAD_GTEST=off \
	-DDOWNLOAD_RUBYRNP=off \
%if %{with rnp_tests}
	-DBUILD_TESTING=on \
%else
	-DBUILD_TESTING=off \
%endif

%cmake_build

%install
%cmake_install

%check
%if %{with rnp_tests}
%ctest
%endif

%post -n librnp%{soname} -p /sbin/ldconfig
%postun -n librnp%{soname} -p /sbin/ldconfig

%files
%license LICENSE*
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files -n librnp%{soname}
%license LICENSE*
%{_libdir}/*.so.0*

%files devel
%license LICENSE*
%doc CHANGELOG.md README.adoc
%{_includedir}/*
%{_libdir}/cmake/rnp
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
