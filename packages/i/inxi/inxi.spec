#
# spec file for package inxi
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011-2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define _version 3.3.35-1
Name:           inxi
Version:        3.3.35
Release:        0
Summary:        A system information script
License:        GPL-3.0-or-later
URL:            https://codeberg.org/smxi/inxi
Source:         %{name}-%{_version}.tar.xz
Requires:       pciutils
Requires:       procps
Requires:       util-linux
Recommends:     Mesa-demo-x
Recommends:     bind-utils
Recommends:     dmidecode
Recommends:     iproute2
Recommends:     kmod-compat
Recommends:     sensors
Recommends:     tree
Recommends:     usbutils
Recommends:     perl(Cpanel::JSON::XS)
Recommends:     perl(Time::HiRes)
Recommends:     perl(XML::Dumper)
Suggests:       curl
Suggests:       freeipmi
Suggests:       hddtemp
Suggests:       sudo
Supplements:    (wmctrl and xorg-x11-server)
Supplements:    (xdpyinfo and xorg-x11-server)
Supplements:    (xprop and xorg-x11-server)
Supplements:    (xrandr and xorg-x11-server)
BuildArch:      noarch

%description
inxi is a command line system information tool. It was forked from
infobash. The primary purpose of inxi is for support, and sys admin
use. inxi is used widely for forum and IRC support.

%prep
%autosetup -n %{name}-%{_version}
sed -i '/^#!/s/env \(.*\)$/\1/' %{name}

%build
## Nothing to build.

%install
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
## Empty section added as per rpmlint report

%files
%license LICENSE.txt
%doc inxi.changelog README.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
