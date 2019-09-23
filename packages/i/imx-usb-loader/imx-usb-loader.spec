#
# spec file for package imx-usb-loader
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guillaume GARDET <guillaume@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define git_version 1525394112.2913fd0

Name:           imx-usb-loader
Version:        0.2~git20180504
Release:        0
Summary:        Vybrid/i.MX recovery utility
License:        LGPL-2.1-or-later
Group:          Hardware/Other
Url:            https://github.com/boundarydevices/imx_usb_loader
Source0:        imx_usb_loader-%{git_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkg-config
# exclude PowerPC as no <sys/io.h>
ExcludeArch:    ppc ppc64 ppc64le

%description
This utility allows to download and execute code on Freescale i.MX5/i.MX6 and Vybrid SoCs through the Serial Download Protocol (SDP). Depending on the board, there is usually some kind of recovery button to bring the SoC into serial download boot mode, check documentation of your hardware.

The utility support USB and UART as serial link.

%prep
%setup -q -n imx_usb_loader-%{git_version}

%build
CFLAGS="$RPM_OPT_FLAGS"  \
make

%install
make install DESTDIR=%{buildroot} sysconfdir=%{_sysconfdir}

%check
make tests

%files
%defattr(-,root,root)
%{_bindir}/imx_uart
%{_bindir}/imx_usb
%dir %{_sysconfdir}/imx-loader.d
%config %{_sysconfdir}/imx-loader.d/imx_usb.conf
%config %{_sysconfdir}/imx-loader.d/mx50_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx51_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx53_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx6_usb_sdp_spl.conf
%config %{_sysconfdir}/imx-loader.d/mx6_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx7_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx7ulp_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/mx8mq_usb_work.conf
%config %{_sysconfdir}/imx-loader.d/vybrid_usb_work.conf
%doc COPYING
%doc README.md

%changelog
