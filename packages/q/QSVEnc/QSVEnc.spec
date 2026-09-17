#
# spec file for package QSVEnc
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024-2025 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           QSVEnc
Version:        8.30+0
Release:        0
Summary:        HW encoder (QSV) testing
License:        MIT
URL:            https://github.com/rigaya/QSVEnc
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE QSVEnc-system-libs.patch -- System libvpl; skip bundled hdr10plus; VapourSynth V4-only
Patch0:         QSVEnc-system-libs.patch
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dovi)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libplacebo)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvmaf)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(vpl)
BuildRequires:  pkgconfig(vulkan)
ExclusiveArch:  %{ix86} x86_64

%description
Investigate performance and image quality of HW encoder (QSV) of Intel.

%prep
%autosetup -p1
# Fix end of line encoding warning
sed -i 's/\r//' QSVEncC_Options.en.md;
sed -i 's/\r//' ReleaseNotes.md;

%build
%meson \
  -Dc_link_args=-Wl,-z,noexecstack \
  -Dcpp_link_args=-Wl,-z,noexecstack \
  -Denable_avisynth=false \
  -Denable_vapoursynth=true \
  -Denable_libass=true \
  -Dlibass_static=false \
  -Denable_libplacebo=true \
  -Dlibplacebo_static_link=false \
  -Denable_vulkan=true \
  -Denable_vmaf=enabled \
  -Dlibvmaf_static=false \
  -Denable_openvino=false \
  -Denable_libvship=disabled
%meson_build

%install
%meson_install

%files
%license license.txt
%doc QSVEncC_Options.en.md ReleaseNotes.md
%{_bindir}/qsvencc

%changelog
