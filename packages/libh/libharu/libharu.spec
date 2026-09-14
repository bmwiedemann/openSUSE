#
# spec file for package libharu
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define relver 2_4
%define lname   libhpdf%{relver}
Name:           libharu
Version:        2.4.6
Release:        0
Summary:        Library for generating PDF files
License:        Zlib
URL:            https://libharu.org
Source0:        https://github.com/libharu/libharu/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
libHaru is a library for generating PDF files.
It supports the following features:
- Generating PDF files with lines, text, images.
- Outline, text annotation, link annotation.
- Compressing document with deflate-decode.
- Embedding PNG, JPEG images.
- Embedding Type1 font and TrueType font.
- Creating encrypted PDF files.
- Using various character sets (ISO8859-1~16, MSCP1250~8, KOI8-R).
- CJK fonts and encodings.

%package -n %{lname}
Summary:        Library for generating PDF files

%description -n %{lname}
libHaru is a library for generating PDF files.
It supports the following features:
- Generating PDF files with lines, text, images.
- Outline, text annotation, link annotation.
- Compressing document with deflate-decode.
- Embedding PNG, JPEG images.
- Embedding Type1 font and TrueType font.
- Creating encrypted PDF files.
- Using various character sets (ISO8859-1~16, MSCP1250~8, KOI8-R).
- CJK fonts and encodings.

%package        devel
Summary:        Development files for libharu
Requires:       %{lname} = %{version}
Requires:       libpng-devel
Requires:       zlib-devel
Conflicts:      libhpdf2_4_2

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  %{nil}
%cmake_build

%install
%cmake_install
# Upstream 2.4.5+ installs README/CHANGES/bindings to the docdir
# (was %{_datadir}/libharu), owned by the devel package below.

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README.md
%{_libdir}/libhpdf.so.*

%files devel
%{_libdir}/libhpdf.so
%{_includedir}/*.h
%{_docdir}/%{name}/

%changelog
