#
# spec file for package rnp
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           rnp
Version:        0.18.1
Release:        0
Summary:        OpenPGP implementation fully compliant with RFC 4880
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.rnpgp.com/
Source:         https://github.com/rnpgp/rnp/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source2:        https://github.com/rnpgp/rnp/releases/download/v%{version}/%{name}-v%{version}.tar.gz.asc
Source3:        https://www.rnpgp.org/openpgp_keys/31AF5A24D861EFCB7CB79A1924900CE0AEFB5417-50DA59D5B9134FA2DB1EB20CFB829AB5D0FE017F.asc#/%{name}.keyring
Patch0:         rnp-v0.18.0-skip-test_encryption_x25519.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.18
BuildRequires:  gpg2 >= 2.2
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(json-c) >= 0.11
BuildRequires:  pkgconfig(sexpp) >= 0.8.7
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(asciidoctor)
%if (0%{?suse_version} >= 1600) || (0%{?sle_version} >= 150700 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(botan-3) >= 3.0.0
%else
BuildRequires:  pkgconfig(botan-2) >= 2.14.0
%endif
%if 0%{?sle_version} >= 150700 && 0%{?is_opensuse}
BuildRequires:  gcc12-c++
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
%autosetup -p1 -n %{name}-v%{version}
rm -rf src/libsexp

%build
%if 0%{?sle_version} >= 150700 && 0%{?is_opensuse}
export CC=gcc-12
export CXX=g++-12
%endif
%cmake \
	-DDOWNLOAD_GTEST:BOOL=OFF \
	-DBUILD_TESTING:BOOL=ON \
	-DSYSTEM_LIBSEXPP:BOOL=ON \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n librnp%{soname}

%files
%license LICENSE*
%{_bindir}/rnp
%{_bindir}/rnpkeys
%{_mandir}/man1/*.1%{?ext_man}

%files -n librnp%{soname}
%license LICENSE*
%{_libdir}/*.so.%{soname}{,.*}

%files devel
%license LICENSE*
%doc CHANGELOG.md README.adoc
%{_includedir}/rnp
%{_libdir}/cmake/rnp
%{_libdir}/librnp.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
