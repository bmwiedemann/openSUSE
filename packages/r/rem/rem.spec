#
# spec file for package rem
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

%global sover   0
%global libname lib%{name}%{sover}
Name:           rem
Version:        0.6.0
Release:        0
Summary:        Audio and Video processing media library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.creytiv.com/rem.html
Source:         http://www.creytiv.com/pub/rem-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  re-devel

%description
Librem is a generic library for real-time audio
and video processing.

Features:
 * Audio buffering, mixing, codecs and resampling
 * Video mixing, rescaling and pixel format conversion

%package -n %{libname}
Summary:        Audio and Video processing media library
Group:          System/Libraries

%description -n %{libname}
Librem is a generic library for real-time audio
and video processing.

Features:
 * Audio buffering, mixing, codecs and resampling
 * Video mixing, rescaling and pixel format conversion

%package devel
Summary:        Librem development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Librem is a generic library for real-time audio
and video processing.

Features:
 * Audio buffering, mixing, codecs and resampling
 * Video mixing, rescaling and pixel format conversion

This subpackage contains libraries and header files for developing
applications that want to make use of librem.

%prep
%setup -q
sed -e 's|@$(CC)|$(CC)|g' \
    -e 's|@$(LD)|$(LD)|g' \
    -e 's|@$(AR)|$(AR)|g' \
    -e 's|@rm -rf|rm -rf|g' -i Makefile

%build
%make_build \
    RELEASE=1 \
    EXTRA_CFLAGS="%optflags" \
    EXTRA_LFLAGS="-Wl,-soname,librem.so.0" \
    LIB_SUFFIX=".so.0"

%install
make DESTDIR=%{buildroot} LIBDIR=%{_libdir} LIB_SUFFIX=".so.0" install
ln -s %{_libdir}/librem.so.0 %{buildroot}%{_libdir}/librem.so
rm %{buildroot}/%{_libdir}/librem.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license docs/COPYING
%doc README.md
%{_libdir}/librem.so.%{sover}*

%files devel
%{_includedir}/rem
%{_libdir}/librem.so
%{_libdir}/pkgconfig/librem.pc

%changelog
