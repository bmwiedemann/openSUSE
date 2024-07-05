#
# spec file for package vapoursynth
#
# Copyright (c) 2024 SUSE LLC
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
Version:        69
Release:        0
Summary:        A video processing framework
License:        LGPL-2.1-only
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.vapoursynth.com/
Source0:        https://github.com/vapoursynth/vapoursynth/archive/R%{version}.tar.gz#/%{name}-R%{version}.tar.gz
# PATCH-FIX-OPENSUSE vapoursynth-version.patch -- makes sure that we have
# some sort of version for othervise unversioned .so files
Patch0:         vapoursynth-version.patch
# Patch to revert for Leap 15.x builds
Patch1:         ac62a4d2a54bacccd09b97453bffe759c01f18ef.patch
BuildRequires:  autoconf
BuildRequires:  automake
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
Obsoletes:      plugin-eedi3
Obsoletes:      plugin-imwri
Obsoletes:      plugin-miscfilters
Obsoletes:      plugin-morpho
Obsoletes:      plugin-ocr
Obsoletes:      plugin-removegrain
Obsoletes:      plugin-subtext
Obsoletes:      plugin-vinverse
Obsoletes:      plugin-vivtc
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc12
BuildRequires:  gcc12-PIE
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif

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

%prep
%setup -q -n %{name}-R%{version}
%patch -P 0 -p1
%if 0%{?suse_version} <= 1500
%patch -P 1 -p1 -R
%endif

%build
%if 0%{?suse_version} <= 1500
export CC="gcc-12"
export CXX="g++-12"
%endif

autoreconf -fiv
%if 0%{?suse_version} <= 1500
# Woraround for old autoconf
sed -z -i "s|PACKAGE_URL='http://www.vapoursynth.com/\n'|PACKAGE_URL='http://www.vapoursynth.com/'|" configure
%endif
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
%license COPYING.LESSER
%doc ChangeLog
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

%changelog
