#
# spec file for package libimagequant
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


%define sover   0
%define libname %{name}%{sover}
Name:           libimagequant
Version:        2.18.0
Release:        0
Summary:        Palette quantization library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://pngquant.org/lib/
Source0:        https://github.com/ImageOptim/libimagequant/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lcms2)

%description
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%package -n %{libname}
Summary:        Palette quantization library
Group:          System/Libraries

%description -n %{libname}
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%package devel
Summary:        Development files for libimagequant
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description devel
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%prep
%setup -q

%build
# This is not an autoconf configure, but the script simply ignores parameters it does not know
%configure \
%ifnarch %ix86 x86_64
    --disable-sse \
%endif
    --with-openmp
make %{?_smp_mflags}

%install
%make_install

# work around --disable-static not working
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -print -delete

%post   -n libimagequant0 -p /sbin/ldconfig
%postun -n libimagequant0 -p /sbin/ldconfig

%files -n libimagequant0
%doc README.md CHANGELOG
%license COPYRIGHT
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/imagequant.pc

%changelog
