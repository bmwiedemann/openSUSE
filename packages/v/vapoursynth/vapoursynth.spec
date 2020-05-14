#
# spec file for package vapoursynth
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


Name:           vapoursynth
Version:        50
Release:        0
Summary:        A video processing framework
License:        LGPL-2.1-only AND OFL-1.1
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.vapoursynth.com/
Source0:        https://github.com/vapoursynth/vapoursynth/archive/R%{version}.tar.gz#/%{name}-R%{version}.tar.gz
# PATCH-FIX-OPENSUSE vapoursynth-version.patch -- makes sure that we have
# some sort of version for othervise unversioned .so files
Patch1:         vapoursynth-version.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  pkgconfig(Magick++) >= 7.0
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg) >= 2.9.2

%description
VapourSynth is a library for video manipulation. It has a core
library written in C++ and a Python module to allow video scripts to
be created.

%package -n libvapoursynth-%{version}
Summary:        A video processing framework
Group:          System/Libraries
Obsoletes:      libvapoursynth

%description -n libvapoursynth-%{version}
VapourSynth's core library with a C++ API.

%package -n libvapoursynth-script0
Summary:        Library for interfacing Python with VapourSynth
Group:          System/Libraries
Requires:       python3-%{name}

%description -n libvapoursynth-script0
VSScript (or libvapoursynth-script) is a library for interfacing Python
with VapourSynth.

%package -n python3-%{name}
Summary:        Python interface for VapourSynth
Group:          Development/Languages/Python

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.

%package devel
Summary:        Development files for VapourSynth
Group:          Development/Libraries/C and C++
Requires:       libvapoursynth-%{version} = %{version}
Requires:       libvapoursynth-script0 = %{version}

%description devel
Header files and pkg-config headers for VapourSynth.

%package tools
Summary:        Extra tools for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors

%description tools
This package contains the vspipe tool for interfacing with
VapourSynth.

%package plugin-eedi3
Summary:        EEDI3 plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-eedi3
eedi3 is a very slow edge directed interpolation filter.

eedi3 works by finding the best non-decreasing (non-crossing) warping
between two lines by minimizing a cost functional. The cost is based
on neighborhood similarity (favor connecting regions that look similar),
the vertical difference created by the interpolated values (favor
small differences), the interpolation directions (favor short connections
vs long), and the change in interpolation direction from pixel to pixel
(favor small changes).

%package plugin-morpho
Summary:        Morpho plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-morpho
Morpho plugin for VapourSynth.

%package plugin-removegrain
Summary:        RGVS plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-removegrain
RemoveGrain is a spatial denoising filter.

Modes 0-24 are implemented. Different modes can be specified for
each plane. If there are fewer modes than planes, the last mode
specified will be used for the remaining planes.

%package plugin-vinverse
Summary:        Vinverse plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-vinverse
Vinverse is a simple filter to remove residual combing, based
on an AviSynth script by Didée.

%package plugin-vivtc
Summary:        VIVTC plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-vivtc
VIVTC is a set of filters that can be used for inverse telecine.
It is a rewrite of some of tritical’s TIVTC filters.

%package plugin-miscfilters
Summary:        Miscelaneous plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-miscfilters
Set of miscelaneous filters for VapourSynth.

%package plugin-imwri
Summary:        Image writer plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-imwri
Image writer plugin for VapourSynth.

%package plugin-ocr
Summary:        OCR plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-ocr
Tesseract OCR framwerork support for VapourSynth.

%package plugin-subtext
Summary:        Subtitles plugin for VapourSynth
Group:          Productivity/Multimedia/Video/Editors and Convertors
Requires:       libvapoursynth-%{version}

%description plugin-subtext
Plugin with subtitles support for VapourSynth.

%prep
%setup -q -n %{name}-R%{version}
%patch1 -p1

%build
autoreconf -fiv
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libvapoursynth-%{version} -p /sbin/ldconfig
%postun -n libvapoursynth-%{version} -p /sbin/ldconfig
%post   -n libvapoursynth-script0 -p /sbin/ldconfig
%postun -n libvapoursynth-script0 -p /sbin/ldconfig

%files -n libvapoursynth-%{version}
%license COPYING.LGPLv2.1
%doc ChangeLog
%doc ofl.txt
%dir %{_libdir}/vapoursynth
%{_libdir}/libvapoursynth-%{version}.so

%files -n libvapoursynth-script0
%{_libdir}/libvapoursynth-script.so.0*

%files -n python3-%{name}
%{python3_sitearch}/*.so

%files devel
%doc doc/
%{_includedir}/vapoursynth/
%{_libdir}/libvapoursynth.so
%{_libdir}/libvapoursynth-script.so
%{_libdir}/pkgconfig/*

%files tools
%{_bindir}/vspipe

%files plugin-eedi3
%{_libdir}/vapoursynth/libeedi3.so

%files plugin-morpho
%{_libdir}/vapoursynth/libmorpho.so

%files plugin-removegrain
%{_libdir}/vapoursynth/libremovegrain.so

%files plugin-vinverse
%{_libdir}/vapoursynth/libvinverse.so

%files plugin-vivtc
%{_libdir}/vapoursynth/libvivtc.so

%files plugin-miscfilters
%{_libdir}/vapoursynth/libmiscfilters.so

%files plugin-imwri
%{_libdir}/vapoursynth/libimwri.so

%files plugin-ocr
%{_libdir}/vapoursynth/libocr.so

%files plugin-subtext
%{_libdir}/vapoursynth/libsubtext.so

%changelog
