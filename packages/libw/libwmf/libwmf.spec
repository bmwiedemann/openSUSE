#
# spec file for package libwmf
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define lname	libwmf-0_2-7
Name:           libwmf
Version:        0.2.13
Release:        0
Summary:        Utilities for Displaying and Converting Metafile Images
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/caolanm/libwmf
Source:         https://github.com/caolanm/libwmf/archive/v%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         libwmf-0.2.8.4-fix.patch
Patch4:         libwmf-0.2.8.4-gd_libpng.patch
Patch5:         libwmf-0.2.8.4-bnc495842.patch
BuildRequires:  gd-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
Provides:       mswordvw:%{_bindir}/wmftopng
Provides:       wv:%{_bindir}/wmftopng

%description
This library interprets metafile images and can either display them
using the X Window System or convert them to standard formats such as
PNG, JPEG, PS, EPS, and more.

%package tools
Summary:        Utilities for Displaying and Converting Metafile Images
# Prov/Obs added on 2011-11-22 (post openSUSE 12.1)
Group:          Productivity/Graphics/Other
Provides:       libwmf = %{version}-%{release}
Provides:       wmf-utils = %{version}-%{release}
Obsoletes:      libwmf < %{version}-%{release}
Obsoletes:      wmf-utils < %{version}-%{release}

%description tools
These utilities read metafile images and can either display them
using the X Window System or convert them to standard formats such as
PNG, JPEG, PS, EPS, and more.

%package -n %{lname}
Summary:        Library for reading Metafile Images
Group:          System/Libraries

%description -n %{lname}
This library reads metafile images.

%package devel
Summary:        Static libraries, header files and documentation for libwmf
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libwmf-gnome = %{version}
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(zlib)
Provides:       mswordvd:%{_prefix}/lib/libwmf.a
Provides:       wv-devel:%{_prefix}/lib/libwmf.a

%description devel
The libwmf-devel package contains the header files and static libraries
necessary for developing programs using libwmf.

%package gnome
Summary:        GNOME plugin for displaying and Converting Metafile Images
Group:          System/Libraries

%description gnome
This library interprets metafile images and can either display them
using the X Window System or convert them to standard formats such as
PNG, JPEG, PS, EPS, and more.

%prep
%setup -q
%autopatch -p0

%build
%configure \
    --disable-static \
    --enable-magick \
    $RPM_ARCH-suse-linux
%make_build

%install
%make_install wmfdocdir=%{_defaultdocdir}/libwmf \
     wmfonedocdir=%{_defaultdocdir}/libwmf/caolan
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files tools
%license COPYING
%doc AUTHORS CREDITS README TODO
%{_bindir}/libwmf-fontmap
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2gd
%{_bindir}/wmf2svg
%{_bindir}/wmf2x
%{_datadir}/libwmf

%files -n %{lname}
%{_libdir}/libwmf*-0.2.so.7*

%files gnome
%{_libdir}/gdk-pixbuf-*/*/loaders/*.so

%files devel
%doc doc/caolan
%doc doc/html
%doc doc/*.{html,png,gif}
%{_bindir}/libwmf-config
%{_includedir}/libwmf
%{_libdir}/libwmf*.so
%{_libdir}/pkgconfig/libwmf.pc

%changelog
