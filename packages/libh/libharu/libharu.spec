#
# spec file for package libharu
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


%define relver 2_3_0
Name:           libharu
Version:        2.3.0
Release:        0
%define lname	libhpdf%{relver}
Summary:        Library for generating PDF files
License:        Zlib
Group:          Productivity/Office/Other
Url:            http://libharu.org
Source0:        https://github.com/libharu/libharu/archive/RELEASE_%{relver}.tar.gz
# PATCH-FIX-UPSTREAM libharu-link-libm.patch gh#libharu/libharu#158 badshah400@opensuse.org -- Add libm to linker argument to fix build failures
Patch0:         libharu-link-libm.patch
# PATCH-FIX-UPSTREAM libharu-cmake.patch badshah400@opensuse.org -- Fix installation locations when using cmake-based build; patch taken from Fedora
Patch1:         libharu-cmake.patch
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package -n %lname
Summary:        Library for generating PDF files
# used wrong shlib packaging name..
Group:          System/Libraries

%description -n %lname
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
%setup -q -n %{name}-RELEASE_%{relver}
%patch0 -p1
%patch1 -p1
# fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' README

%build
%cmake -DLIBHPDF_STATIC=NO
%make_jobs

%install
%cmake_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc README
%{_libdir}/libhpdf.so.%{version}

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libhpdf.so
%{_datadir}/%{name}/

%changelog
