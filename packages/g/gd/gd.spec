#
# spec file for package gd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define prjname libgd
%define lname libgd3
Name:           gd
Version:        2.2.5
Release:        0
Summary:        A Drawing Library for Programs That Use PNG and JPEG Output
License:        MIT
Group:          System/Libraries
Url:            https://libgd.github.io/
Source:         https://github.com/libgd/libgd/releases/download/%{name}-%{version}/%{prjname}-%{version}.tar.xz
Source1:        baselibs.conf
# might be upstreamed, but could be suse specific also (/usr/share/fonts/Type1 font dir)
Patch1:         gd-fontpath.patch
# could be upstreamed, but not in this form (need ac check for attribute format printf, etc.)
Patch2:         gd-format.patch
# could be upstreamed
Patch3:         gd-aliasing.patch
Patch4:         gd-CVE-2018-5711.patch
Patch5:         libgd-config.patch
Patch6:         gd-CVE-2018-1000222.patch
Patch7:         gd-CVE-2019-6978.patch
Patch8:         gd-CVE-2019-6977.patch
# CVE-2019-11038 [bsc#1140118]
Patch9:         gd-CVE-2019-11038.patch
# needed for tests
BuildRequires:  dejavu
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(xpm)
Provides:       gdlib = %{version}
Obsoletes:      gdlib < %{version}

%description
Gd allows your code to quickly draw images complete with lines, arcs,
text, and multiple colors. It supports cut and paste from other images
and flood fills. It outputs PNG, JPEG, and WBMP (for wireless devices)
and is supported by PHP.

%package -n %{lname}
Summary:        A Drawing Library for Programs That Use PNG and JPEG Output
# change order while installing a split library
Group:          System/Libraries
Obsoletes:      gd < 2.2.3
Conflicts:      gd < 2.2.3

%description -n %{lname}
Gd allows your code to quickly draw images complete with lines, arcs,
text, and multiple colors. It supports cut and paste from other images
and flood fills. It outputs PNG, JPEG, and WBMP (for wireless devices)
and is supported by PHP.

%package devel
Summary:        Drawing Library for Programs with PNG and JPEG Output
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
gd allows code to quickly draw images complete with lines, arcs, text,
multiple colors, cut and paste from other images, and flood fills. gd
writes out the result as a PNG or JPEG file. This is particularly
useful in World Wide Web applications, where PNG and JPEG are two of
the formats accepted for inline images by most browsers.

%prep
%setup -q -n %{prjname}-%{version}
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
chmod 644 COPYING

%build
# ADDITIONAL CFLAGS ARE NEEDED TO FIX TEST FAILURES IN CASE OF i586, BUT HARMLESS TO APPLY GENERALLY FOR ALL ix86
%ifarch %{ix86}
export CFLAGS="%{optflags} -msse -mfpmath=sse"
%else
%ifnarch x86_64
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
%endif

# without-x -- useless switch which just mangles cflags
%configure \
	--disable-silent-rules \
	--disable-werror \
	--without-liq \
	--without-x \
	--with-fontconfig \
	--with-freetype \
	--with-jpeg \
	--with-png \
	--with-xpm \
	--with-webp \
	--with-zlib \
	--disable-static
make %{?_smp_mflags}

%check
%if !0%{?sle_version} || 0%{?sle_version} < 150000
# on SLE15 we have --with-arch-32=x86_64 so the test actually
# passes boo#1053825
%ifarch %{ix86}
# See https://github.com/libgd/libgd/issues/359
XFAIL_TESTS="gdimagegrayscale/basic $XFAIL_TESTS"
%endif
%endif
export XFAIL_TESTS
make check %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc COPYING
%{_bindir}/annotate
%{_bindir}/bdftogd
%{_bindir}/gd2copypal
%{_bindir}/gd2togif
%{_bindir}/gd2topng
%{_bindir}/gdcmpgif
%{_bindir}/gdparttopng
%{_bindir}/gdtopng
%{_bindir}/giftogd2
%{_bindir}/pngtogd
%{_bindir}/pngtogd2
%{_bindir}/webpng

%files -n %{lname}
%doc COPYING
%{_libdir}/*.so.*

%files devel
%doc COPYING
%{_bindir}/gdlib-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gdlib.pc

%changelog
