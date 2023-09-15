#
# spec file for package mbpoll
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           mbpoll
Version:        1.5.2
Release:        0
Summary:        Command line utility to communicate with ModBus slave (RTU or TCP)
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/epsilonrt/mbpoll
Source:         https://github.com/epsilonrt/mbpoll/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmodbus) >= 3.1.4

%description
mbpoll uses libmodbus (http://libmodbus.org/).
Although the syntax of these options is very close modpoll proconX program,
it is a completely independent project.

mbpoll can:
 - read discrete inputs
 - read and write binary outputs (coil)
 - read input registers
 - read and write output registers (holding register)

The reading and writing registers may be in decimal, hexadecimal or
floating single precision.

%prep
%setup -q
sed -i 's/\r$//' AUTHORS README.md

%build
%cmake
%make_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/mbpoll

%changelog
