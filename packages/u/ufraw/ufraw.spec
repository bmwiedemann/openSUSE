#
# spec file for package ufraw
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} < 1599
# Leap 15.X do have GIMP2...
%bcond_without gimpui
# gimptool-2.0 --gimpplugindir
%define _gimpplugindir %(gimptool-2.0 --gimpplugindir)
%else
# ...but 16.0 and upwards (incl. TW) do not
%bcond_with gimpui
%endif

Name:           ufraw
Version:        0.22
Release:        0
Summary:        Application to read and manipulate raw images from digital cameras
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://ufraw.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/ufraw/ufraw/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch0:         %{name}-desktop.patch
Patch1:         %{name}-boundary.patch
Patch2:         %{name}-glibc210.patch
Patch3:         narrowing-conversion.patch
Patch4:         ufraw-gcc7.patch
Patch5:         ufraw-0.22-jpeg9.patch
Patch6:         ufraw-0.22-exiv2-0.27.patch
Patch7:         01_no-gimp-remote.patch
Patch8:         02_CVE-2015-8366.patch
Patch9:         04_fix-abs-gcc-7.patch
Patch10:        05_CVE-2018-19655.patch
Patch11:        06_lensfun_destroy_cleanup.patch
Patch12:        Fix-build-with-GCC9.patch
Patch13:        ufraw-fix-c++.patch
# PATCH-FIX-FREEBSD: ufraw-0.22-exiv2-0.28.patch https://cgit.freebsd.org/ports/diff/graphics/ufraw/files/patch-ufraw__exiv2.cc?id=0e4d3e69d22d89c1e0972f90bab859473c3935ca
Patch14:        ufraw-0.22-exiv2-0.28.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(exiv2) >= 0.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.12
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun) >= 0.2.5
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libtiff-4)
%if %{with gimpui}
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gimpui-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkimageview) >= 1.6
%endif

%description
ufraw is "The Unidentified Flying Raw". It is an application to read and
manipulate raw images from digital cameras. It takes care of the color
management, handles the Nikon curve formats and has an editor for the tone
curves. For batch processing of images, the command line can be used.

%if %{with gimpui}
%package -n gimp-ufraw
Summary:        Raw photo loader plugin for The GIMP
Group:          Productivity/Graphics/Other
Suggests:       dcraw-gnome
Enhances:       gimp-2.0
Obsoletes:      rawphoto < %{version}
Obsoletes:      ufraw-gimp < %{version}
Provides:       gimp-2.0-dcraw-plugin
Provides:       rawphoto = %{version}
Provides:       ufraw-gimp = %{version}
%if %{?gimp_api_version:1}0
Requires:       gimp(abi) = %{gimp_abi_version}
Requires:       gimp(api) = %{gimp_api_version}
%else
%requires_eq    gimp
%endif

%description -n gimp-ufraw
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used as a GIMP plug-in. It reads raw images using
Dave Coffin's raw conversion utility DCRaw, and it supports basic color
management using Little CMS, allowing the user to apply color profiles.

%endif

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
  export CFLAGS="-m64 %{optflags}"
%else
  export CFLAGS="%{optflags}"
%endif
export CXXFLAGS="$CFLAGS"
autoreconf -fi
%configure \
	--enable-contrast \
	--enable-dst-correction \
  --with-gtk=%{?with_gimpui:yes}%{!?with_gimpui:no}
%make_build

%install
%make_install
%find_lang %{name}
%if %{with gimpui}
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
%else
rm %{buildroot}%{_datadir}/pixmaps/*
%endif

%files lang -f %{name}.lang

%files
%license COPYING
%doc MANIFEST README TODO
%{_bindir}/ufraw-batch
%{_mandir}/man?/*
%if %{with gimpui}
%{_bindir}/ufraw
%{_datadir}/pixmaps/ufraw.png
%{_datadir}/applications/*.desktop
%endif

%if %{with gimpui}
%files -n gimp-ufraw
%dir %{_libdir}/gimp/
%dir %{_libdir}/gimp/2.0
%{_gimpplugindir}/plug-ins/
%endif

%changelog
