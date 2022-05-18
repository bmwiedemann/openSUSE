#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "playdv"
%bcond_without playdv
%define tools_description playdv sample application
%define psuffix -playdv
%else
%bcond_with playdv
%define tools_description encodedv, dubdv and dvconnect tools
%endif
%define sname libdv

Name:           libdv%{?psuffix}
Version:        1.0.0
Release:        0
Summary:        The Quasar DV Codec
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://libdv.sourceforge.net/
Source:         http://sourceforge.net/projects/libdv/files/libdv/%{version}/%{sname}-%{version}.tar.gz
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
BuildRequires:  libtool
BuildRequires:  libv4l-devel >= 0.8.4
BuildRequires:  pkg-config
BuildRequires:  popt-devel
%if %{with playdv}
BuildRequires:  gtk2-devel
BuildRequires:  libXv-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  pkgconfig(sdl)
%endif

%description
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

This package contains the %{tools_description}.

%package -n libdv4
Summary:        The Quasar DV Codec
Group:          Development/Libraries/Other

%description -n libdv4
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

%package devel
Summary:        The Quasar DV codec
Group:          Development/Libraries/Other
Requires:       libdv4 = %{version}

%description devel
The Quasar DV codec (libdv) is a software codec for DV video, the
encoding format used by most digital camcorders, typically those that
support the IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was
developed according to the official standards for DV video: IEC 61834
and SMPTE 314M.

%prep
%autosetup -p1 -n %{sname}-%{version}

%build
mkdir m4
%if %{without playdv}
# Dummy macro for ignored SDL, autoreconf fails otherwise
echo "AC_DEFUN([AM_PATH_SDL], [true])" >> m4/dummy_sdl.m4
%endif

autoreconf -fiv
export CFLAGS="${RPM_OPT_FLAGS/O2/O3} -fomit-frame-pointer -fPIC -DPIC"
export LDFLAGS="-pie"
%configure \
	--disable-static \
%if %{with playdv}
	--enable-sdl \
%else
	--disable-sdl \
	--disable-gtk \
%endif
        %{nil}
make %{?_smp_mflags}

%install
%if "%{flavor}" == "playdv"
%make_install -C playdv
%else
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%endif

%post -n libdv4 -p /sbin/ldconfig

%postun -n libdv4 -p /sbin/ldconfig

%files
%{_bindir}/*
%doc %{_mandir}/man1/*.1.gz

%if "%{flavor}" != "playdv"
%files -n libdv4
%{_libdir}/libdv.so.*

%files devel
%{_includedir}/libdv
%{_libdir}/libdv.so
%{_libdir}/pkgconfig/libdv.pc
%endif

%changelog
