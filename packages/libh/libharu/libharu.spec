#
# spec file for package libharu
#
# Copyright (c) 2022 SUSE LLC
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


%define relver 2_4_2
%define lname	libhpdf%{relver}
Name:           libharu
Version:        2.4.2
Release:        0
Summary:        Library for generating PDF files
License:        Zlib
Group:          Productivity/Office/Other
URL:            http://libharu.org
Source0:        https://github.com/libharu/libharu/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
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
# used wrong shlib packaging name..
Group:          System/Libraries

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
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libpng-devel
Requires:       zlib-devel

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
%cmake -DLIBHPDF_STATIC=NO
%make_jobs

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc README.md
%{_libdir}/libhpdf.so

%files devel
%{_includedir}/*.h
%{_datadir}/%{name}/

%changelog
