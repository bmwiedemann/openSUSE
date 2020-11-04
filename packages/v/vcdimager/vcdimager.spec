#
# spec file for package vcdimager
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sonum 0
Name:           vcdimager
Version:        2.0.1
Release:        0
Summary:        Video CD (VCD) authoring software
# Alternative URL with SCM https://github.com/rocky/vcdimager
License:        GPL-2.0-only
Group:          Productivity/Multimedia/CD/Record
URL:            http://www.vcdimager.org/
Source:         https://ftp.gnu.org/gnu/vcdimager/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/vcdimager/%{name}-%{version}.tar.gz.sig
Source2:        baselibs.conf
Patch1:         sector_private.patch
BuildRequires:  fdupes
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcdio) >= 2.0.0
BuildRequires:  pkgconfig(libiso9660) >= 2.0.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.3.8
BuildRequires:  pkgconfig(popt)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU VCDImager is a full-featured mastering suite for authoring,
disassembling and analyzing Video CDs and Super Video CDs.

%package -n libvcdinfo%{sonum}
Summary:        Video CD (VCD) authoring software
Group:          System/Libraries

%description -n libvcdinfo%{sonum}
GNU VCDImager is a full-featured mastering suite for authoring,
disassembling and analyzing Video CDs and Super Video CDs.
This is the core library

%package devel
Summary:        Video CD (VCD) authoring software
Group:          Development/Languages/C and C++
Requires:       libvcdinfo%{sonum} = %{version}-%{release}

%description devel
GNU VCDImager is a full-featured mastering suite for authoring,
disassembling and analyzing Video CDs and Super Video CDs.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS) -D_GNU_SOURCE"
%configure \
  --disable-silent-rules \
  --enable-shared \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_mandir}

# Does not work with paranoia available
#%%check
#make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post -n libvcdinfo%{sonum} -p /sbin/ldconfig
%postun -n libvcdinfo%{sonum} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README THANKS
%{_bindir}/*
%{_infodir}/*.info%{?ext_info}
%{_mandir}/man?/*%{ext_man}

%files -n libvcdinfo%{sonum}
%license COPYING
%{_libdir}/libvcdinfo.so.0*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
