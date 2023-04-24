#
# spec file for package ebook-tools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ebook-tools
Version:        0.2.2
Release:        0
Summary:        A library for reading ebook files
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/ebook-tools/
Source:         %{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         ebook-tools-64bit-installation.diff
Patch2:         ebook-tools-visibility-hidden.patch
# PATCH-FIX-OPENSUSE - fix https://sourceforge.net/p/ebook-tools/bugs/8/
Patch3:         0001-Avoid-crash-on-toc.ncx-navPoint-without-navLabel.patch
# PATCH-FIX-OPENSUSE
Patch4:         0002-Avoid-crash-on-spine-itemref-without-idref.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)

%description
ebook-tools provides some tools to handle ebook files

%package -n libepub0
Summary:        A library for reading ebook files
Group:          Development/Libraries/C and C++

%description -n libepub0
libepub library is needed for okular to support ebook format.

%package -n libepub-devel
Summary:        Header files for libepub library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libepub0 = %{version}

%description -n libepub-devel
Header files for the libepub library

%prep
%setup -q
%patch1 -p1
%patch2
%patch3 -p1
%patch4 -p1

%build
%cmake

%cmake_build

%install
%cmake_install
nm -C -D %{buildroot}%{_libdir}/libepub.so.*

%post -n libepub0 -p /sbin/ldconfig
%postun -n libepub0 -p /sbin/ldconfig

%files
%{_bindir}/einfo
%{_bindir}/lit2epub

%files -n libepub0
%license LICENSE
%{_libdir}/libepub.so.*

%files -n libepub-devel
%{_includedir}/epub.h
%{_includedir}/epub_version.h
%{_includedir}/epub_shared.h
%{_libdir}/libepub.so

%changelog
