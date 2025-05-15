#
# spec file for package rshim
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Mellanox Technologies. All Rights Reserved.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rshim
Version:        2.3.8
Release:        0
Summary:        User-space driver for Mellanox BlueField SoC
License:        BSD-3-Clause OR GPL-2.0-only
Group:          System/Management
URL:            https://github.com/mellanox/rshim-user-space
Source0:        https://github.com/Mellanox/rshim-user-space/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libusb-1.0)
ExcludeArch:    %{ix86} armv6l armv6hl armv7l armv7hl

%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
%autosetup -p1 -n rshim-user-space-rshim-%{version}

%build
./bootstrap.sh
%configure \
	--docdir=%{_docdir}/%{name} \
	--with-systemdsystemunitdir=%{_unitdir} \
	--enable-usb \
	--enable-pcie \
	--enable-fuse \
	%{nil}
%make_build

%install
%make_install

%pre
%service_add_pre rshim.service

%post
%service_add_post rshim.service

%preun
%service_del_preun rshim.service

%postun
%service_del_postun rshim.service

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/rshim.conf
%{_sbindir}/bf-reg
%{_sbindir}/bfb-install
%{_sbindir}/bfb-tool
%{_sbindir}/fwpkg_unpack.py
%{_sbindir}/mlx-mkbfb
%{_sbindir}/rshim
%{_unitdir}/rshim.service
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}

%changelog
