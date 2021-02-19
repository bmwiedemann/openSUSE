#
# spec file for package hw-probe
#
# Copyright (c) 2020 Andrey Ponomarenko <andrewponomarenko@yandex.ru>
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


Name:       hw-probe
Version:    1.5
Release:    1
Summary:    Check operability of computer hardware and find drivers
License:    LGPL-2.0+
Group:      Hardware/Other
BuildArch:  noarch
URL:        https://github.com/linuxhw/hw-probe
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:   perl-libwww-perl
Requires:   curl
Requires:   hwinfo
Requires:   dmidecode
Requires:   pciutils
Requires:   usbutils
Requires:   smartmontools
Requires:   hdparm
Requires:   sysstat
Requires:   util-linux
Requires:   sensors
Requires:   lsb-release
Requires:   acpica
Recommends: Mesa-demo-x
Recommends: mcelog
BuildRequires: perl
BuildRequires: perl(Getopt::Long)

%description
A tool to check operability of computer hardware and upload result
to the Linux hardware database.

Probe — is a snapshot of your computer hardware state and system
logs. The tool checks operability of devices by analysis of logs
and returns a permanent url to view the probe of the computer.

The tool is intended to simplify collecting of logs necessary for
investigating hardware related problems. Just run one simple
command in the console to check your hardware and collect all the
system logs at once:

    sudo -E hw-probe -all -upload

By creating probes you contribute to the HDD/SSD Real-Life
Reliability Test study: https://github.com/linuxhw/SMART

%prep
%setup -q

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
make install prefix=%{_prefix} DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
