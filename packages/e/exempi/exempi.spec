#
# spec file for package exempi
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


%define sonum 8
Name:           exempi
Version:        2.6.2
Release:        0
Summary:        XMP support library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://libopenraw.freedesktop.org/exempi/
Source0:        https://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Source1:        https://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libboost_test-devel
BuildRequires:  libexpat-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
Exempi is a library for XMP parsing and I/O. XMP is a kind of
metadata for images and PDF.

%package -n libexempi%{sonum}
Summary:        XMP support library
Group:          System/Libraries

%description -n libexempi%{sonum}
Exempi is a library for XMP parsing and I/O. XMP (Extensible Metadata
Platform) facilitates embedding metadata in files using a subset of
RDF. Most notably, XMP supports embedding metadata in PDF and many
image formats.

%package tools
Summary:        Tools from Exempi, an XMP support library
Group:          Productivity/Graphics/Other

%description tools
Exempi is a library for XMP parsing and I/O. XMP is a kind of
metadata for images and PDF.

This subpackage contains utilities from the Exempi project.

%package -n libexempi-devel
Summary:        Development files for the Exempi XMP support library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libexempi%{sonum} = %{version}

%description -n libexempi-devel
Exempi is a library for XMP metadata parsing and doing I/O with it.

This subpackage contains the header files for building applications
with Exempi.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%check
%if ! 0%{?qemu_user_space_build}
%make_build check
%endif

%post -n libexempi%{sonum} -p /sbin/ldconfig
%postun -n libexempi%{sonum} -p /sbin/ldconfig

%files -n libexempi%{sonum}
%license COPYING
%doc README.md NEWS
%{_libdir}/lib*.so.*

%files tools
%license COPYING
%{_bindir}/exempi
%{_mandir}/man1/exempi.1%{?ext_man}

%files -n libexempi-devel
%license COPYING
%{_libdir}/lib*.so
%{_includedir}/exempi-2.0
%{_libdir}/pkgconfig/*.pc

%changelog
