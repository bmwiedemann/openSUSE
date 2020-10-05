#
# spec file for package rshim
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Mellanox Technologies. All Rights Reserved.
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
Version:        2.0.4.32
Release:        0
Summary:        User-space driver for Mellanox BlueField SoC
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/mellanox/rshim-user-space
Source0:        %{name}-%{version}.tar
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)

%description
This is the user-space driver to access the BlueField SoC via the rshim
interface. It provides ways to push boot stream, debug the target or login
via the virtual console or network interface.

%prep
%setup -q

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install -C src INSTALL_DIR="%{buildroot}%{_sbindir}"
install -d %{buildroot}%{_unitdir}
install -m 0644 rshim.service %{buildroot}%{_unitdir}
install -d %{buildroot}%{_mandir}/man8
install -m 0644 man/rshim.8 %{buildroot}%{_mandir}/man8

%files
%license LICENSE
%doc README.md
%{_unitdir}/rshim.service
%{_sbindir}/rshim
%{_mandir}/man8/rshim.8%{?ext_man}

%changelog
