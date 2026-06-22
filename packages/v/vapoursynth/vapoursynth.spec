#
# spec file for package vapoursynth
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 4
Name:           vapoursynth
Version:        77
Release:        0
Summary:        A video processing framework
License:        LGPL-2.1-only
URL:            https://www.vapoursynth.com/
Source0:        https://github.com/vapoursynth/vapoursynth/archive/R%{version}.tar.gz#/%{name}-R%{version}.tar.gz
# PATCH-FIX-OPENSUSE vapoursynth-fhs-install.patch -- install libraries, vspipe, headers and pkgconfig to FHS locations instead of the Python wheel dir, give libvsscript a soversion, and emit FHS-correct prefix/includedir/libdir (and a Libs line) in vapoursynth.pc
Patch0:         vapoursynth-fhs-install.patch
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(Magick++) >= 7.0
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg) >= 3.0.5
Obsoletes:      plugin-eedi3
Obsoletes:      plugin-imwri
Obsoletes:      plugin-miscfilters
Obsoletes:      plugin-morpho
Obsoletes:      plugin-ocr
Obsoletes:      plugin-removegrain
Obsoletes:      plugin-subtext
Obsoletes:      plugin-vinverse
Obsoletes:      plugin-vivtc

%description
VapourSynth is a library for video manipulation. It has a core
library written in C++ and a Python module to allow video scripts to
be created.

%package -n libvapoursynth%{sover}
Summary:        A video processing framework

%description -n libvapoursynth%{sover}
VapourSynth's core library with a C++ API.

%package -n libvsscript0
Summary:        Library for interfacing Python with VapourSynth
Requires:       python3-%{name}

%description -n libvsscript0
VSScript (or libvsscript) is a library for interfacing Python
with VapourSynth.

%package -n python3-%{name}
Summary:        Python interface for VapourSynth

%description -n python3-%{name}
Python interface for VapourSynth/VSScript.

%package devel
Summary:        Development files for VapourSynth
Requires:       libvapoursynth%{sover} = %{version}
Requires:       libvsscript0 = %{version}

%description devel
Header files and pkg-config files for VapourSynth.

%package tools
Summary:        Extra tools for VapourSynth

%description tools
This package contains the vspipe tool for interfacing with
VapourSynth.

%prep
%autosetup -p1 -n %{name}-R%{version}

%build
%meson
%meson_build

%install
%meson_install
# drop the useless $ORIGIN RUNPATH (libraries live in the system libdir)
chrpath -d %{buildroot}%{_bindir}/vspipe
chrpath -d %{buildroot}%{python3_sitearch}/vapoursynth/*.so

%ldconfig_scriptlets -n libvapoursynth%{sover}
%ldconfig_scriptlets -n libvsscript0

%files -n libvapoursynth%{sover}
%license COPYING.LESSER
%doc ChangeLog
%{_libdir}/libvapoursynth.so.%{sover}

%files -n libvsscript0
%{_libdir}/libvsscript.so.0

%files -n python3-%{name}
%{python3_sitearch}/vapoursynth/

%files devel
%doc doc/
%{_includedir}/vapoursynth/
%{_libdir}/libvapoursynth.so
%{_libdir}/libvsscript.so
%{_libdir}/pkgconfig/vapoursynth.pc

%files tools
%{_bindir}/vspipe

%changelog
