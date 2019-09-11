#
# spec file for package libwmf
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


%define lname	libwmf-0_2-7
Name:           libwmf
Version:        0.2.8.4
Release:        0
Summary:        Utilities for Displaying and Converting Metafile Images
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
Url:            http://wvWare.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/wvware/%{name}/%{version}/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         libwmf-0.2.8.4-ia64.patch
Patch1:         libwmf-0.2.8.4-fix.patch
Patch2:         libwmf-0.2.8.4-config.patch
Patch3:         libwmf-0.2.8.4-overflow-CVE-2006-3376.patch
Patch4:         libwmf-0.2.8.4-gd_libpng.patch
Patch5:         libwmf-0.2.8.4-bnc495842.patch
Patch6:         libwmf-0.2.8.4-CVE-2015-0848.patch
Patch7:         libwmf-0.2.8.4-badrle.patch
Patch8:         libwmf-0.2.8.4-CVE-2015-4696.patch
Patch9:         libwmf-0.2.8.4-CVE-2015-4695.patch
Patch10:        reproducible.patch
Patch11:        use-pkg-config-for-freetype.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gd-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
Provides:       mswordvw:%{_bindir}/wmftopng
Provides:       wv:%{_bindir}/wmftopng
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Provides:       mswordvd:%{_libexecdir}/libwmf.a
Provides:       wv-devel:%{_libexecdir}/libwmf.a

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
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
# Patch11 modifies configure.ac
autoreconf -fi
%configure --disable-static --prefix=%{_prefix} $RPM_ARCH-suse-linux --enable-magick --libdir=%{_libdir}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_includedir}/libwmf
make DESTDIR=%{buildroot} \
     wmfdocdir=%{_defaultdocdir}/libwmf \
     wmfonedocdir=%{_defaultdocdir}/libwmf/caolan \
     install
find %{buildroot} -type f -name "*.la" -delete -print
cp AUTHORS COPYING CREDITS ChangeLog README TODO %{buildroot}/%{_defaultdocdir}/libwmf

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files tools
%defattr(-,root,root)
%{_bindir}/libwmf-fontmap
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2gd
#/usr/bin/wmf2magick
#/usr/bin/wmf2plot
%{_bindir}/wmf2svg
%{_bindir}/wmf2x
#
#
%{_datadir}/libwmf
#
%dir %{_defaultdocdir}/libwmf
%doc %{_defaultdocdir}/libwmf/AUTHORS
%doc %{_defaultdocdir}/libwmf/COPYING
%doc %{_defaultdocdir}/libwmf/CREDITS
%doc %{_defaultdocdir}/libwmf/ChangeLog
%doc %{_defaultdocdir}/libwmf/README
%doc %{_defaultdocdir}/libwmf/TODO

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libwmf*-0.2.so.7*

%files gnome
%defattr(-,root,root)
%dir %{_libdir}/gtk-*/*/loaders
%{_libdir}/gtk-*/*/loaders/*.so

%files devel
%defattr(-,root,root)
%{_bindir}/libwmf-config
%{_includedir}/libwmf
%{_libdir}/libwmf*.so
%dir %{_libdir}/gtk-*/*/loaders
#
%doc %{_defaultdocdir}/libwmf/*.html
%doc %{_defaultdocdir}/libwmf/*.png
%doc %{_defaultdocdir}/libwmf/*.gif
%doc %{_defaultdocdir}/libwmf/caolan
%doc %{_defaultdocdir}/libwmf/html

%changelog
