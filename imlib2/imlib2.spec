#
# spec file for package imlib2
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define lname	libImlib2-1
Name:           imlib2
Version:        1.5.1
Release:        0
Summary:        Image handling and conversion library
License:        BSD-3-Clause
Group:          Development/Libraries/X11
Url:            http://sourceforge.net/projects/enlightenment/
Source:         http://downloads.sourceforge.net/project/enlightenment/imlib2-src/%{version}/%{name}-%{version}.tar.bz2
Patch1:         imlib2-bswap.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bzip2)
Recommends:     imlib2-loaders
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%package -n %{lname}
Summary:        Image handling and conversion library
Group:          System/Libraries

%description -n %{lname}
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%package devel
Summary:        Imlib 2 - development libraries
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}
Requires:       xorg-x11-libX11-devel

%description devel
These are the development headers and library for imlib2.

%package filters
Summary:        Imlib 2 - plugin filters
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}

%description filters
This package has the basic set of plugin filters that come with Imlib2.

%package loaders
Summary:        Imlib 2 - image loaders
Group:          Development/Libraries/X11
Provides:       imlib2-loader_argb
Provides:       imlib2-loader_bmp
Provides:       imlib2-loader_bz2
Provides:       imlib2-loader_gif
Provides:       imlib2-loader_jpeg
Provides:       imlib2-loader_png
Provides:       imlib2-loader_pnm
Provides:       imlib2-loader_tga
Provides:       imlib2-loader_tiff
Provides:       imlib2-loader_xpm
Provides:       imlib2-loader_zlib

%description loaders
This package contains the imlib2 image loaders for: argb, bmp, gif,
jpeg, png, pnm, tga, tiff, xpm

%prep
%setup -q
%patch1

%build
autoreconf -fiv
%configure \
%ifarch %ix86
	--enable-mmx \
%else
	--disable-mmx \
%endif
%ifarch x86_64
	--enable-amd64 \
%endif
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--enable-shared \
	--enable-visibility-hiding \
	--disable-static
make %{?_smp_mflags} V=1

%install
%make_install
pushd %{buildroot}%{_bindir}/
 for i in *imlib2-config ; do
  test "$i" != "imlib2-config" || continue
  ln -s $i imlib2-config
 done
popd
find %{buildroot} -type f -name "*.la" -delete -print
#Heads up ! clean up  madness here..
sed -i -e 's@-lfreetype@@g' -e 's@-lz@@g' -e 's@-lXext@@g' -e 's@-ldl@@g' -e 's@-lm@@g' %{buildroot}%{_bindir}/imlib2-config

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc AUTHORS README COPYING doc/index.html
%doc doc/imlib2.gif doc/blank.gif
%{_bindir}/imlib2_bumpmap
%{_bindir}/imlib2_colorspace
%{_bindir}/imlib2_conv
%{_bindir}/imlib2_poly
%{_bindir}/imlib2_show
%{_bindir}/imlib2_test
%{_bindir}/imlib2_view
%{_bindir}/imlib2_grab
%attr(755,root,root) %dir %{_datadir}/imlib2
%{_datadir}/imlib2/*

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libImlib2.so.1*

%files devel
%defattr(-,root,root,0755)
%{_libdir}/pkgconfig/imlib2.pc
%{_includedir}/*
%{_libdir}/lib*.so
%{_bindir}/imlib2-config

%files filters
%defattr(-,root,root)
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/filters

%files loaders
%defattr(-,root,root)
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/loaders

%changelog
