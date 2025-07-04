#
# spec file for package kf6-kimageformats
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


%define qt6_version 6.8.0

%define rname kimageformats

%if 0%{?suse_version} > 1500
# Fails on Leap 15 with '/usr/include/OpenEXR/ImathVec.h:228:34: error: ISO C++17 does not allow dynamic exception specification'
%define with_exr 1
# Leap 15 doesn't have libjxl >= 0.9.4
%define with_jxl 1
# Not available
%define with_jp2 1
%endif
# Full KF6 version (e.g. 6.15.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kimageformats
Version:        6.15.0
Release:        0
Summary:        Image format plugins for Qt
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
%if 0%{?with_exr}
BuildRequires:  openexr-devel
%endif
BuildRequires:  cmake(KF6Archive) >= %{_kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(libavif) >= 0.8.2
BuildRequires:  cmake(libheif) >= 1.10.0
%if 0%{?with_jp2}
BuildRequires:  cmake(OpenJPEG)
%endif
%if 0%{?with_jxl}
BuildRequires:  pkgconfig(libjxl) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_cms) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_threads) >= 0.9.4
%endif
BuildRequires:  pkgconfig(libraw) >= 0.20.2
BuildRequires:  pkgconfig(libraw_r) >= 0.20.2
# Also install the Qt image plugins
Requires:       qt6-imageformats >= %{qt6_version}

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package eps
Summary:        EPS image format plugin for Qt
Requires:       ghostscript

%description eps
This plugin provides support for the EPS document format for QtGui. As
it invokes ghostscript for conversion, it should only be used in trusted
environments.

%package devel
Summary:        Development files for kimageformats
Requires:       %{name} = %{version}

%description devel
This package contains development files for kimageformats, a framework
to provide additional image format plugins for QtGui.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DKIMAGEFORMATS_HEIF:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%files
%license LICENSES/*
%dir %{_kf6_plugindir}/imageformats
%{_kf6_plugindir}/imageformats/kimg_ani.so
%{_kf6_plugindir}/imageformats/kimg_avif.so
%{_kf6_plugindir}/imageformats/kimg_dds.so
%if 0%{?with_exr}
%{_kf6_plugindir}/imageformats/kimg_exr.so
%endif
%{_kf6_plugindir}/imageformats/kimg_hdr.so
%{_kf6_plugindir}/imageformats/kimg_heif.so
%if 0%{?with_jxl}
%{_kf6_plugindir}/imageformats/kimg_jxl.so
%endif
%if 0%{?with_jp2}
%{_kf6_plugindir}/imageformats/kimg_jp2.so
%endif
%{_kf6_plugindir}/imageformats/kimg_kra.so
%{_kf6_plugindir}/imageformats/kimg_ora.so
%{_kf6_plugindir}/imageformats/kimg_pcx.so
%{_kf6_plugindir}/imageformats/kimg_pfm.so
%{_kf6_plugindir}/imageformats/kimg_pic.so
%{_kf6_plugindir}/imageformats/kimg_psd.so
%{_kf6_plugindir}/imageformats/kimg_pxr.so
%{_kf6_plugindir}/imageformats/kimg_qoi.so
%{_kf6_plugindir}/imageformats/kimg_ras.so
%{_kf6_plugindir}/imageformats/kimg_raw.so
%{_kf6_plugindir}/imageformats/kimg_rgb.so
%{_kf6_plugindir}/imageformats/kimg_sct.so
%{_kf6_plugindir}/imageformats/kimg_tga.so
%{_kf6_plugindir}/imageformats/kimg_xcf.so

%files eps
%license LICENSES/*
%dir %{_kf6_plugindir}/imageformats
%{_kf6_plugindir}/imageformats/kimg_eps.so

%files devel
%{_kf6_cmakedir}/KF6ImageFormats/

%changelog
