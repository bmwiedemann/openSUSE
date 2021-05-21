#
# spec file for package kimageformats
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


%if 0%{?suse_version} > 1500
%define with_avif 1
%endif
%if 0%{?suse_version} > 1500 || (0%{?is_opensuse} && 0%{?sle_version} >= 150300)
%define with_heif 1
%endif
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           kimageformats
Version:        5.82.0
Release:        0
Summary:        Image format plugins for Qt
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  openexr
BuildRequires:  openexr-devel
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
%if 0%{?with_avif}
BuildRequires:  cmake(libavif) >= 0.8.2
%endif
%if 0%{?with_heif}
BuildRequires:  cmake(libheif) >= 1.10.0
%endif
%requires_ge    libQt5Gui5
%requires_ge    libQt5PrintSupport5
Recommends:     libqt5-qtimageformats >= 5.12.0
Suggests:       %{name}-eps

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package eps
Summary:        EPS image format plugin for Qt
Group:          System/GUI/KDE
Requires:       ghostscript
Conflicts:      %{name} < %{version}-%{release}

%description eps
This plugin provides support for the EPS document format for QtGui. As
it invokes ghostscript for conversion, it should only be used in trusted
environments.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DKIMAGEFORMATS_HEIF=ON
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/imageformats
%{_kf5_plugindir}/imageformats/kimg_ani.so
%if 0%{?with_avif}
%{_kf5_plugindir}/imageformats/kimg_avif.so
%endif
%if 0%{?with_heif}
%{_kf5_plugindir}/imageformats/kimg_heif.so
%endif
%{_kf5_plugindir}/imageformats/kimg_exr.so
%{_kf5_plugindir}/imageformats/kimg_hdr.so
%{_kf5_plugindir}/imageformats/kimg_kra.so
%{_kf5_plugindir}/imageformats/kimg_ora.so
%{_kf5_plugindir}/imageformats/kimg_pcx.so
%{_kf5_plugindir}/imageformats/kimg_pic.so
%{_kf5_plugindir}/imageformats/kimg_psd.so
%{_kf5_plugindir}/imageformats/kimg_ras.so
%{_kf5_plugindir}/imageformats/kimg_rgb.so
%{_kf5_plugindir}/imageformats/kimg_tga.so
%{_kf5_plugindir}/imageformats/kimg_xcf.so
%dir %{_kf5_servicesdir}/qimageioplugins
%{_kf5_servicesdir}/qimageioplugins/ani.desktop
%if 0%{?with_avif}
%{_kf5_servicesdir}/qimageioplugins/avif.desktop
%endif
%if 0%{?with_heif}
%{_kf5_servicesdir}/qimageioplugins/heif.desktop
%endif
%{_kf5_servicesdir}/qimageioplugins/dds.desktop
%{_kf5_servicesdir}/qimageioplugins/exr.desktop
%{_kf5_servicesdir}/qimageioplugins/hdr.desktop
%{_kf5_servicesdir}/qimageioplugins/jp2.desktop
%{_kf5_servicesdir}/qimageioplugins/kra.desktop
%{_kf5_servicesdir}/qimageioplugins/ora.desktop
%{_kf5_servicesdir}/qimageioplugins/pcx.desktop
%{_kf5_servicesdir}/qimageioplugins/pic.desktop
%{_kf5_servicesdir}/qimageioplugins/psd.desktop
%{_kf5_servicesdir}/qimageioplugins/ras.desktop
%{_kf5_servicesdir}/qimageioplugins/rgb.desktop
%{_kf5_servicesdir}/qimageioplugins/tga.desktop
%{_kf5_servicesdir}/qimageioplugins/xcf.desktop

%files eps
%license LICENSES/*
%dir %{_kf5_plugindir}/imageformats
%dir %{_kf5_servicesdir}/qimageioplugins
%{_kf5_plugindir}/imageformats/kimg_eps.so
%{_kf5_servicesdir}/qimageioplugins/eps.desktop

%changelog
