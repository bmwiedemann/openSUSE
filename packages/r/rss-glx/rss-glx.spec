#
# spec file for package rss-glx
#
# Copyright (c) 2021 SUSE LLC
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


Name:           rss-glx
Version:        0.9.1
Release:        0
Summary:        Really Slick Screensavers Port to GLX
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Amusements/Toys/Screensavers
URL:            http://rss-glx.sourceforge.net/
Source0:         http://prdownloads.sourceforge.net/rss-glx/rss-glx_%{version}.tar.bz2
Source1:         README.SUSE
# PATCH-FIX-OPENSUSE
Patch0:         rss-glx-optflags.patch
# patch should go upstream, but there is TODO: source files include
# magick/MagickCore.h and wand/MagickWand.h. This works for us for
# both ImageMagick-6 and ImageMagick-7 because we package wand/ and
# magick/ symlinks of ImageMagick include dir, but files should
# include MagickCore/MagickCore.h and MagickWand/MagickWand.h for
# ImageMagick-7 instead; the upstream seem to be dead anyway though
Patch1:         rss-glx-ImageMagick7.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-GCC-11.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  gcc-c++
# directory ownership
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  openal-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xscreensaver
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(glu)

%description
Cool collection of 3D screensavers. Linux port of Really Slick Screensavers -
Web's most visually exciting collection of original, open-source screensavers.


%prep
%setup -q -n %{name}_%{version}
%patch -P 0
%patch -P 1 -p1
%patch -P 2 -p1

%build
autoreconf -fiv
%configure --disable-static \
  --enable-shared \
  --with-pic \
  --with-configdir=%{_sysconfdir}/xscreensaver \
  --program-prefix=""
cp %{SOURCE1} .

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
#no -devel files here..
rm -rvf %{buildroot}%{_libdir}/*.so

# FIX boo#901450
mkdir -pv %{buildroot}%{_libexecdir}/xscreensaver
pushd %{buildroot}%{_bindir}
for i in `ls` ; do
  mv -vf %{buildroot}%{_bindir}/${i} %{buildroot}%{_libexecdir}/xscreensaver
done
popd
rm -rvf %{buildroot}%{_bindir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%config %{_sysconfdir}/xscreensaver/*
%{_libdir}/lib*
%{_mandir}/*/*%{ext_man}
%dir %{_libexecdir}/xscreensaver
%{_libexecdir}/xscreensaver/*
%doc README*

%changelog
