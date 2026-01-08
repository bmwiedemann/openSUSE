#
# spec file for package libnvidia-egl-wayland
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
%define meson_build /usr/bin/meson compile -C %{_vpath_builddir} %{_smp_mflags} --verbose
%define meson_install /usr/bin/meson install -C %{_vpath_builddir} --no-rebuild --destdir=%{buildroot}
%endif

%global commit0 ada1c37041002f4f009a33d6d285eae39bf9ad02
%global date 20251213
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %%{version}

%define so_ver 1
%define lname libnvidia-egl-wayland2%{so_ver}
%define rname egl-wayland2

Name:           libnvidia-egl-wayland2
Version:        1.0.1%{!?tag:~%{date}git%{shortcommit0}}
Release:        1
Summary:        Dma-buf-based Wayland external platform library
# src/wayland/dma-buf.h is GPL 2, rest is Apache 2.0
License:        Apache-2.0 and GPL-2.0
URL:            https://github.com/NVIDIA/egl-wayland2
Group:          Development/Libraries/C and C++
Source0:        egl-wayland2-1.0.0-rc.tar.gz
Source1:        baselibs.conf
Source2:        CONTRIBUTING.md
Source3:        LICENSE
Source4:        rpmlintrc
Patch1:         0001-egl-wayland2-close-dmabuf-format-table-fd.patch
Patch2:         0002-Update-the-wl_egl_window-attached-size.patch
Patch3:         0003-egl-wayland2-Fix-libdrm-loading-when-wl_drm-is-not-a.patch
Patch4:         0004-Remove-a-stray-abort-in-eplWlCreateWindowSurface.patch
Patch5:         0005-Increment-version-number-to-1.0.1.patch
Patch6:         0006-base-Add-basic-support-for-EGL_KHR_partial_update.patch
Patch7:         0007-base-Add-an-EplImplFuncs-function-for-EGL_BUFFER_AGE.patch
Patch8:         0008-base-Add-an-EplImplFuncs-function-for-eglSetDamageRe.patch
Patch9:         0009-wayland-Implement-EplImplFuncs-QueryBufferAge.patch
Patch10:        0010-Fix-the-version-check-for-wl_surface.patch
Patch11:        0011-wayland-Flip-the-damage-rectangles-in-wl_surface_dam.patch
Patch12:        0012-egl-wayland2-add-FP16-DRM-format.patch
Patch14:        0014-Fix-multisampled-windows.patch
Patch15:        0015-Disable-multisampled-windows-on-older-drivers.patch
Patch16:        0016-Don-t-pass-EGL_RENDER_BUFFER-to-the-driver.patch
Patch17:        0017-Fix-an-incorrect-return-statement-in-eplWlSwapBuffer.patch
Patch18:        0018-Replace-SurfaceFeedbackState-modifiers_changed-with-.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.50
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(gbm) >= 21.2.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

%description
This is a new implementation of the EGL External Platform Library for Wayland
(EGL_KHR_platform_wayland), using the NVIDIA driver's new platform surface
interface, which simplifies a lot of the library and improves window resizing.

%package -n %{lname}
Summary:        Dma-buf-based Wayland external platform library
Group:          System/Libraries

%description -n %{lname}
This is a new implementation of the EGL External Platform Library for Wayland
(EGL_KHR_platform_wayland), using the NVIDIA driver's new platform surface
interface, which simplifies a lot of the library and improves window resizing.

%prep
%autosetup -p1 -n egl-wayland2-1.0.0-rc

%build
export LDFLAGS="-Wl,-z,noexecstack -Wl,-z,now -Wl,-z,relro %{?_lto_cflags}"
%meson
%meson_build

%install
%meson_install
rm -f %{buildroot}%{_libdir}/libnvidia-egl-wayland2.so

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-wayland2.so.%{so_ver}*
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/09_nvidia_wayland2.json

%changelog
