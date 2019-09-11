#
# spec file for package potrace
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


Name:           potrace
Version:        1.15
Release:        0
Summary:        Utility for Tracing a Bitmap to Scalable Outline Image
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Url:            http://potrace.sourceforge.net/
Source:         http://potrace.sourceforge.net/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  zlib-devel
Provides:       bitmap_tracing

%description
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.  The input is a bitmap (PBM, PGM,
PPM, or BMP), and the default output is one of several vector file
formats.  A typical use is to create EPS files from scanned data, such
as company or university logos, handwritten notes, etc. The resulting
image is not "jaggy" like a bitmap, but smooth. It can then be rendered
at any resolution.

%package -n libpotrace0
Summary:        Library for Tracing a Bitmap to Scalable Outline Image
Group:          System/Libraries

%description -n libpotrace0
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.  The input is a bitmap (PBM, PGM,
PPM, or BMP), and the default output is one of several vector file
formats.  A typical use is to create EPS files from scanned data, such
as company or university logos, handwritten notes, etc. The resulting
image is not "jaggy" like a bitmap, but smooth. It can then be rendered
at any resolution.

%package devel
Summary:        Library Development Files for Tracing a Bitmap to Scalable Outline Image
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
Potrace is a utility for tracing a bitmap, which means, transforming a
bitmap into a smooth, scalable image.  The input is a bitmap (PBM, PGM,
PPM, or BMP), and the default output is one of several vector file
formats.  A typical use is to create EPS files from scanned data, such
as company or university logos, handwritten notes, etc. The resulting
image is not "jaggy" like a bitmap, but smooth. It can then be rendered
at any resolution.

%prep
%setup -q

%build
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat-security
export CFLAGS="%{optflags} %{warn_flags} -fPIE"
export LDFLAGS="-pie"
%ifarch s390x
# clang on s390x does not support -fstack-protector from the default optflags
# (undefined reference to `__stack_chk_guard')
export CFLAGS="${CFLAGS/-fstack-protector /}"
%endif
# clang does not support that yet...
export CFLAGS="${CFLAGS/-fstack-clash-protection /}"
%configure\
	--docdir=%{_docdir}/%{name}\
	--with-libpotrace\
	--disable-static
make %{?_smp_mflags}

%install
%if 0%{?suse_version} > 1110
%make_install
%else
%make_install
%endif
cp -a AUTHORS ChangeLog COPYING NEWS README %{buildroot}%{_docdir}/%{name}/
rm %{buildroot}%{_libdir}/*.*a

%post -n libpotrace0 -p /sbin/ldconfig
%postun -n libpotrace0 -p /sbin/ldconfig

%files
%{_bindir}/*
%doc %{_docdir}/%{name}
%{_mandir}/man?/*%{ext_man}

%files -n libpotrace0
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
