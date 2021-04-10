#
# spec file for package libdrm
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


Name:           libdrm
Version:        2.4.105
Release:        0
Summary:        Userspace Interface for Kernel DRM Services
License:        MIT
Group:          Development/Libraries/X11
URL:            https://dri.freedesktop.org/
# Git-Clone:    https://gitlab.freedesktop.org/mesa/drm.git
# Git-Web:      https://gitlab.freedesktop.org/mesa/drm
# Source URL:   https://dri.freedesktop.org/libdrm/
Source:         https://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  meson >= 0.43
BuildRequires:  pkgconfig
# needed for rst2man to create manual pages
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(pciaccess) >= 0.10
Provides:       libdrm23 = %{version}
Obsoletes:      libdrm23 < %{version}
%if 0%{?with_valgrind_support:1}
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm}
BuildRequires:  pkgconfig(valgrind)
%endif
%endif
# bug437293
%ifarch ppc64
Obsoletes:      libdrm-64bit < %{version}
Provides:       libdrm-64bit = %{version}
%endif

%description
The package contains the userspace interface to the kernel DRM
services.

%package tools
Summary:        Diagnostic utilities for DRI and DRM
Group:          System/Base
Obsoletes:      libdrm < %{version}-%{release}
Provides:       libdrm = %{version}-%{release}

%description tools
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems that support the ioctl
interface, and for chipsets with DRM memory manager, support for
tracking relocations and buffers. libdrm is a low-level library,
typically used by graphics drivers such as the Mesa DRI and X
drivers.

This package contains diagnostic utilities for DRI and DRM.

%package devel
Summary:        Libraries, includes and more to develop libdrm applications
Group:          Development/Libraries/X11
Requires:       libdrm2 = %{version}
Requires:       libdrm_amdgpu1 = %{version}
Requires:       libdrm_nouveau2 = %{version}
Requires:       libdrm_radeon1 = %{version}
%ifarch %{arm} aarch64
Requires:       libdrm_etnaviv1 = %{version}
Requires:       libdrm_exynos1 = %{version}
Requires:       libdrm_freedreno1 = %{version}
Requires:       libdrm_tegra0 = %{version}
%endif
%ifarch %{arm}
Requires:       libdrm_omap1 = %{version}
%endif
%ifarch %{ix86} x86_64
Requires:       libdrm_intel1 = %{version}
%endif
# bug437293
%ifarch ppc64
Obsoletes:      libdrm-devel-64bit < %{version}
Provides:       libdrm-devel-64bit = %{version}
%endif

%description devel
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems that support the ioctl
interface, and for chipsets with DRM memory manager, support for
tracking relocations and buffers. libdrm is a low-level library,
typically used by graphics drivers such as the Mesa DRI and X
drivers.

This package contains the development headers for the library found
in libdrm2.

%package -n libdrm2
Summary:        Userspace Interface for Kernel DRM Services
Group:          System/Libraries

%description -n libdrm2
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems that support the ioctl
interface, and for chipsets with DRM memory manager, support for
tracking relocations and buffers. libdrm is a low-level library,
typically used by graphics drivers such as the Mesa DRI and X
drivers.

%package -n libdrm_intel1
Summary:        Userspace interface for Kernel DRM services for Intel chips
Group:          System/Libraries

%description -n libdrm_intel1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface for Kernel DRM services
for Intel chips.

%package -n libdrm_nouveau2
Summary:        Userspace interface for Kernel DRM services for NVIDIA chips
Group:          System/Libraries

%description -n libdrm_nouveau2
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface for Kernel DRM services
for NVIDIA chips.

%package -n libdrm_radeon1
Summary:        Userspace interface for Kernel DRM services for AMD Radeon chips
Group:          System/Libraries

%description -n libdrm_radeon1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface for Kernel DRM services
for AMD Radeon chips.

%package -n libdrm_amdgpu1
Summary:        Userspace interface for Kernel DRM services for AMD Radeon chips
Group:          System/Libraries

%description -n libdrm_amdgpu1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface for Kernel DRM services
for AMD Radeon chips.

%package -n libkms-devel
Summary:        Development files for the KMS MM abstraction library
Group:          Development/Libraries/C and C++
Requires:       libkms1 = %{version}

%description -n libkms-devel
This package contains the development headers for the library found
in libkms1.

%package -n libkms1
Summary:        Userspace interface to kernel DRM buffer management
Group:          System/Libraries

%description -n libkms1
The KMS Memory Management abstraction library.
This package provides the userspace interface to kernel DRM buffer management

%package -n libdrm_omap1
Summary:        Userspace interface to kernel DRM services for omap chips
Group:          System/Libraries

%description -n libdrm_omap1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface to kernel DRM services
for omap chips.

%package -n libdrm_etnaviv1
Summary:        Userspace interface to kernel DRM services for Vivante chips
Group:          System/Libraries

%description -n libdrm_etnaviv1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface to kernel DRM services
for Vivante chips.

%package -n libdrm_exynos1
Summary:        Userspace interface to kernel DRM services for Samsung Exynos chips
Group:          System/Libraries

%description -n libdrm_exynos1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface to kernel DRM services
for Samsung Exynos chips.

%package -n libdrm_freedreno1
Summary:        Userspace interface to kernel DRM services for Qualcomm Adreno chips
Group:          System/Libraries

%description -n libdrm_freedreno1
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface to kernel DRM services
for Qualcomm Adreno chips.

%package -n libdrm_tegra0
Summary:        Userspace interface to kernel DRM services for Nvidia Tegra chips
Group:          System/Libraries

%description -n libdrm_tegra0
libdrm is a library for accessing the Direct Rendering Manager on
Linux, BSD and other operating systems.

This package provides userspace interface to kernel DRM services
for Nvidia Tegra chips.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%meson \
	--default-library=shared \
	-Dinstall-test-programs=true \
	-Dudev=true \
%ifarch %{arm}
	-Domap=true \
%endif
%ifarch %{arm} aarch64
	-Detnaviv=true \
	-Dexynos=true \
	-Dfreedreno=true \
	-Dtegra=true \
%endif
%ifnarch %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm}
	-Dvalgrind=false \
%else
%if 0%{!?with_valgrind_support:1}
	-Dvalgrind=false \
%endif
%endif
	%{nil}
%meson_build

%check
### FIXME ### Tests fail on arm, so lets not run them there for now.
%ifnarch %{arm}
%meson_test
%endif

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}

%post   -n libdrm2 -p /sbin/ldconfig
%postun -n libdrm2 -p /sbin/ldconfig
%post   -n libdrm_intel1 -p /sbin/ldconfig
%postun -n libdrm_intel1 -p /sbin/ldconfig
%post   -n libdrm_nouveau2 -p /sbin/ldconfig
%postun -n libdrm_nouveau2 -p /sbin/ldconfig
%post   -n libdrm_radeon1 -p /sbin/ldconfig
%postun -n libdrm_radeon1 -p /sbin/ldconfig
%post   -n libdrm_amdgpu1 -p /sbin/ldconfig
%postun -n libdrm_amdgpu1 -p /sbin/ldconfig
%post   -n libkms1 -p /sbin/ldconfig
%postun -n libkms1 -p /sbin/ldconfig

%ifarch %{arm}
%post   -n libdrm_omap1 -p /sbin/ldconfig
%postun -n libdrm_omap1 -p /sbin/ldconfig
%endif

%ifarch %{arm} aarch64
%post   -n libdrm_etnaviv1 -p /sbin/ldconfig
%postun -n libdrm_etnaviv1 -p /sbin/ldconfig
%post   -n libdrm_exynos1 -p /sbin/ldconfig
%postun -n libdrm_exynos1 -p /sbin/ldconfig
%post   -n libdrm_freedreno1 -p /sbin/ldconfig
%postun -n libdrm_freedreno1 -p /sbin/ldconfig
%post   -n libdrm_tegra0 -p /sbin/ldconfig
%postun -n libdrm_tegra0 -p /sbin/ldconfig
%endif

%files tools
%{_bindir}/drmdevice
%ifarch %{arm} aarch64
%{_bindir}/etnaviv_2d_test
%{_bindir}/etnaviv_bo_cache_test
%{_bindir}/etnaviv_cmd_stream_test
%{_bindir}/exynos_fimg2d_test
%{_bindir}/exynos_fimg2d_event
%{_bindir}/exynos_fimg2d_perf
%endif
%{_bindir}/kms-steal-crtc
%{_bindir}/kms-universal-planes
%{_bindir}/kmstest
%{_bindir}/modeprint
%{_bindir}/modetest
%{_bindir}/proptest
%{_bindir}/vbltest

%files devel
%{_mandir}/man?/drm*?%{ext_man}
%{_includedir}/libdrm
%ifarch %{arm}
%{_includedir}/omap
%endif
%ifarch %{arm} aarch64
%{_includedir}/exynos
%{_includedir}/freedreno
%endif
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_includedir}/libsync.h
%{_libdir}/libdrm*.so
%{_libdir}/pkgconfig/libdrm*.pc

%files -n libdrm2
%{_libdir}/libdrm.so.2*
%dir %{_datarootdir}/libdrm

%ifarch %{ix86} x86_64
%files -n libdrm_intel1
%{_libdir}/libdrm_intel.so.1*
%endif

%files -n libdrm_nouveau2
%{_libdir}/libdrm_nouveau.so.2*

%files -n libdrm_radeon1
%{_libdir}/libdrm_radeon.so.1*

%files -n libdrm_amdgpu1
%{_libdir}/libdrm_amdgpu.so.1*
%{_datarootdir}/libdrm/amdgpu.ids

%files -n libkms1
%{_libdir}/libkms.so.1*

%files -n libkms-devel
%{_includedir}/libkms
%{_libdir}/libkms.so
%{_libdir}/pkgconfig/libkms.pc

%ifarch %{arm}
%files -n libdrm_omap1
%{_libdir}/libdrm_omap.so.1*
%endif

%ifarch %{arm} aarch64
%files -n libdrm_etnaviv1
%{_libdir}/libdrm_etnaviv.so.1*

%files -n libdrm_exynos1
%{_libdir}/libdrm_exynos.so.1*

%files -n libdrm_freedreno1
%{_libdir}/libdrm_freedreno.so.1*

%files -n libdrm_tegra0
%{_libdir}/libdrm_tegra.so.0*
%endif

%changelog
