#
# spec file for package ckb-next
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


Name:           ckb-next
Version:        0.4.2
Release:        0
Summary:        RGB driver for Corsair keyboard and mice
License:        GPL-2.0-only AND BSD-3-Clause
Group:          Hardware/Other
URL:            https://github.com/ckb-next/ckb-next
Source:         https://github.com/ckb-next/ckb-next/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE ckb-next-use-run.patch
Patch1:         ckb-next-use-run.patch
# PATCH-FIX-OPENSUSE ckb-next-systemd.patch
Patch2:         ckb-next-systemd.patch
# PATCH-FIX-OPENSUSE ckb-next-no-cmake-modules.patch
Patch3:         ckb-next-no-cmake-modules.patch
# PATCH-FIX-UPSTREAM ckb-next-udev.patch
Patch4:         ckb-next-udev.patch
# PATCH-FIX-UPSTREAM 422.patch boo#1135528
Patch5:         422.patch
# PATCH-FIX-UPSTREAM ckb-next-gcc10.patch
Patch6:         ckb-next-gcc10.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} >= 1500
BuildRequires:  quazip-qt5-devel
%endif
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      ckb < %{version}
Provides:       ckb = %{version}
Requires:       bash
%{systemd_requires}

%description
ckb is a driver for Corsair keyboards and mice. It brings the
features of their proprietary CUE software to the Linux operating
system. This project supports much of the same functionality,
including full RGB animations.

%prep
%autosetup -p1

%build
%cmake \
       -DDISABLE_UPDATER=1 \
       -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
       -DUDEV_RULE_DIRECTORY=%{_udevrulesdir}
%cmake_build

%install
%cmake_install
for s in 16 22 32 48 64 96 128 192 256; do
   mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
   convert -strip -resize ${s}x${s} %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/ckb-next.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
mkdir %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}-daemon
%suse_update_desktop_file -r %{name} Settings HardwareSettings

%pre
%service_add_pre %{name}-daemon.service

%post
%service_add_post %{name}-daemon.service

%preun
%service_del_preun %{name}-daemon.service

%postun
%service_del_postun %{name}-daemon.service

%files
%license LICENSE
%doc CHANGELOG.md FIRMWARE README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-dev-detect
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_sbindir}/rc%{name}-daemon
%{_libexecdir}/%{name}-daemon
%{_libexecdir}/%{name}-animations
%{_udevrulesdir}/99-%{name}-daemon.rules
%{_unitdir}/%{name}-daemon.service

%changelog
