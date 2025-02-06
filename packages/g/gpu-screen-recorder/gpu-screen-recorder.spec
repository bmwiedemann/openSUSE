#
# spec file for package gpu-screen-recorder
#
# Copyright (c) 2025 mantarimay
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


%bcond_with test
Name:           gpu-screen-recorder
Version:        20250125
Release:        0
Summary:        An extremely fast hardware-accelerated screen recorder
License:        GPL-3.0-only
URL:            https://git.dec05eba.com/gpu-screen-recorder/about
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vulkan-headers
BuildRequires:  zstd
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)

%description
This is a screen recorder that has minimal impact on system performance
by recording your monitor using the GPU only, similar to ShadowPlay on
windows. This is the fastest screen recording tool for Linux.

This screen recorder can be used for recording your desktop offline, for
live streaming and for nvidia ShadowPlay-like instant replay, where only
the last few minutes are saved.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%if 0%{?suse_version} < 1600
rm %{buildroot}/usr/lib/modprobe.d/gsr-nvidia.conf
%endif

%if %{with test}
%check
%meson_test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/gsr-kms-server
%{_userunitdir}/%{name}.service
%if 0%{?suse_version} > 1600
%{_modprobedir}/gsr-nvidia.conf
%endif

%changelog
