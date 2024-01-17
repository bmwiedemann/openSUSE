#
# spec file for package smilutils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           smilutils
Version:        0.3.2+cvs20070731
Release:        0
Summary:        Tools for converting and editing digital video (DV) data
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.kinodv.org/article/view/70/1/7
Source0:        %{name}-%{version}.tar.bz2
Patch0:         abuild.diff
# PATCH-FIX-UPSTREAM smilutils-gcc4.3.patch vuntz@opensuse.org -- Taken from Debian and Mandriva, fix build with gcc 4.3
Patch1:         smilutils-gcc4.3.patch
# PATCH-FIX-UPSTREAM smilutils-gcc4.4.patch vuntz@opensuse.org -- Taken from Mandriva, fix build with gcc 4.4
Patch2:         smilutils-gcc4.4.patch
BuildRequires:  SDL-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libdv)
BuildRequires:  pkgconfig(libquicktime)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)

%description
These tools can be used to convert DV to image streams, avi or mov
files and back, duplicate or drop frames and to convert kino projects
to DV, raw audio and raw yuv video

More details can be found using "man smilutils" and at:
http://users.pandora.be/acp/kino/smilutils.html

%prep
%autosetup -n %{name} -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fcommon"
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/image2raw
%{_bindir}/ppm2raw
%{_bindir}/ppm2webcam
%{_bindir}/ppmeffectv
%{_bindir}/ppmfilter
%{_bindir}/raw2dv
%{_bindir}/raw2image
%{_bindir}/raw2webcam
%{_bindir}/raw2yuv
%{_bindir}/rawmultiply
%{_bindir}/rawplay
%{_bindir}/smil2raw
%{_bindir}/smil2wav
%{_bindir}/smil2yuv
%{_bindir}/tga2raw
%{_bindir}/xwd2raw
%{_libdir}/kino
%{_mandir}/man1/image2raw.1%{?ext_man}
%{_mandir}/man1/ppm2raw.1%{?ext_man}
%{_mandir}/man1/ppm2webcam.1%{?ext_man}
%{_mandir}/man1/raw2dv.1%{?ext_man}
%{_mandir}/man1/raw2image.1%{?ext_man}
%{_mandir}/man1/raw2webcam.1%{?ext_man}
%{_mandir}/man1/raw2yuv.1%{?ext_man}
%{_mandir}/man1/rawmultiply.1%{?ext_man}
%{_mandir}/man1/rawplay.1%{?ext_man}
%{_mandir}/man1/smil2raw.1%{?ext_man}
%{_mandir}/man1/smil2wav.1%{?ext_man}
%{_mandir}/man1/smil2yuv.1%{?ext_man}
%{_mandir}/man1/smilutils.1%{?ext_man}
%{_mandir}/man1/xwd2raw.1%{?ext_man}

%changelog
