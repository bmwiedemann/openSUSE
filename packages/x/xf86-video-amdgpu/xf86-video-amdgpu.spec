#
# spec file for package xf86-video-amdgpu
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%if 0%{?suse_version} < 1330
%define pci_ids_dir %{_sysconfdir}/X11/xorg_pci_ids
%endif
Name:           xf86-video-amdgpu
Version:        19.1.0
Release:        0
Summary:        AMDGPU video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source:         http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source3:        amdgpu.ids
Patch0:         u_fno-common.patch
Patch1:         N_amdgpu-present-Check-tiling-for-newer-versions-too.patch
BuildRequires:  autoconf >= 2.6.0
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4.58
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.16
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v00001002d*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%{x11_abi_videodrv_req}

%description
amdgpu is an Xorg driver for AMD video cards.

Its autodetects whether your hardware has a CI or newer AMD Graphics Card

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?pci_ids_dir:1}
rm -f %{buildroot}%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
mkdir -p %{buildroot}%{pci_ids_dir}
cp %{SOURCE3} %{buildroot}%{pci_ids_dir}/
%endif

%files
%defattr(-,root,root)
%doc COPYING README.md
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/amdgpu_drv.so
%{_mandir}/man4/amdgpu.4%{?ext_man}
%if 0%{?pci_ids_dir:1}
%dir %{pci_ids_dir}
%{pci_ids_dir}/amdgpu.ids
%else
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%endif

%changelog
