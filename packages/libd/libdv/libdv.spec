#
# spec file for package libdv
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libdv
Version:        1.0.0
Release:        0
Summary:        The Quasar DV Codec
License:        GPL-2.0+
Group:          Development/Libraries/Other
Url:            http://libdv.sourceforge.net/
Source:         http://sourceforge.net/projects/libdv/files/libdv/%{version}/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM libdv-gtk2.patch vuntz@opensuse.org -- Patch from debian, to use GTK+ 2.x
Patch1:         libdv-gtk2.patch
Patch2:         libdv.omit-excessive-warnings.patch
Patch3:         libdv.non_x86-reorder_block.patch
Patch4:         libdv-filesizecheck.patch
Patch5:         libdv-1.0.0-textrels-selinux.patch
Patch6:         libdv-v4l-2.6.38.patch
Patch7:         libdv-fix-no-add-needed.patch
Patch8:         libdv-endian.patch
Patch9:         libdv-visibility.patch
BuildRequires:  SDL-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXv-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1210
BuildRequires:  libv4l-devel >= 0.8.4
%endif
# bug437293
%ifarch ppc64
Obsoletes:      libdv-64bit
%endif

%description
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

There are two sample applications included with libdv: playdv and
encode.

%package -n libdv4
Summary:        The Quasar DV Codec
Group:          Development/Libraries/Other
# bug437293
%ifarch ppc64
Obsoletes:      libdv-64bit
%endif
#

%description -n libdv4
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

There are two sample applications included with libdv: playdv and
encode.

%package devel
Summary:        The Quasar DV codec
Group:          Development/Libraries/Other
Requires:       libdv4 = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      libdv-devel-64bit
%endif
#

%description devel
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

There are two sample applications included with libdv: playdv and
encode.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%if 0%{?suse_version} >= 1210
%patch6 -p1
%endif
%patch7
%patch8 -p1
%patch9 -p1

%build
mkdir m4
autoreconf -fiv
CFLAGS="${RPM_OPT_FLAGS/O2/O3} -fomit-frame-pointer -fPIC -DPIC" \
%configure \
	--disable-static \
	--with-pic \
	--enable-sdl
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdv4 -p /sbin/ldconfig

%postun -n libdv4 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%doc %{_mandir}/man1/*.1.gz

%files -n libdv4
%defattr(-,root,root)
%{_libdir}/libdv.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/libdv
%{_libdir}/libdv.so
%{_libdir}/pkgconfig/libdv.pc

%changelog
