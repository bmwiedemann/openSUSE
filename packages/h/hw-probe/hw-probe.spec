#
# spec file for package hw-probe
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           hw-probe
Version:        1.6.6
Release:        0
Summary:        Tool for checking operability of hardware and finding drivers
License:        BSD-4-Clause AND LGPL-2.1-or-later
URL:            https://github.com/linuxhw/hw-probe
Source0:        https://github.com/linuxhw/hw-probe/archive/%{version}/%{name}-%{version}.tar.gz
# spec-cleaner deviation: keep plain perl, perl-libwww-perl and usbutils
# names; provider-form expansion is noise on this non-Perl package.
BuildRequires:  perl
BuildRequires:  perl(Getopt::Long)
Requires:       acpica
Requires:       curl
Requires:       dmidecode
Requires:       hdparm
Requires:       hwinfo
Requires:       lsb-release
Requires:       pciutils
Requires:       perl-libwww-perl
Requires:       sensors
Requires:       smartmontools
Requires:       sysstat
Requires:       usbutils
Requires:       util-linux
Recommends:     Mesa-demo-x
Recommends:     mcelog
BuildArch:      noarch

%description
Hardware Probe Tool (hw-probe) is a tool to probe for hardware, check
operability and find drivers with the help of the Linux hardware
database.

Each probe is a snapshot of the computer hardware state and system
logs. The tool checks operability of devices by analysis of logs,
uploads them and returns a permanent URL to view the probe of the
computer.

%prep
%autosetup -p1
sed -i "s|\#\!\/usr\/bin\/env perl|\#\!\/usr\/bin\/perl|g" hw-probe.pl

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
make install prefix=%{_prefix} DESTDIR=%{buildroot}
install -Dm 644 -t "%{buildroot}%{_unitdir}/" periodic/hw-probe.*

%pre
%service_add_pre %{name}.service %{name}.timer

%post
%service_add_post %{name}.service %{name}.timer

%preun
%service_del_preun %{name}.service %{name}.timer

%postun
%service_del_postun %{name}.service %{name}.timer

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.*

%changelog
