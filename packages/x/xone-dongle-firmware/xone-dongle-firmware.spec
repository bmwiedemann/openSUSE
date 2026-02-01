#
# spec file for package xone-dongle-firmware
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           xone-dongle-firmware
# Version of the install/firmware.sh script
Version:        0+git20251208.d8be599
Release:        0
Summary:        Xbox Wireless Controller Adapter firmware downloader
# The firmware itself is proprietary and downloaded from Microsoft;
# this package only contains helper scripts and placeholders.
License:        GPL-3.0-or-later
URL:            https://github.com/dlundqvist/xone

Source0:        xone-dl-firmware.sh.in
Source1:        COPYING
Source2:        firmware.sha256

Requires:       bash
Requires:       bsdtar
Requires:       curl
Requires:       w3m
Conflicts:      xone < 0.5.0
BuildArch:      noarch

%description
This package installs an update script which downloads the firmware
for the Xbox Wireless Controller Adapter (wireless dongle) from
Microsoft. The firmware itself is proprietary and is not shipped
in this package.

During installation or update, the user is shown Microsoft's Terms
of Use. By downloading and using the firmware, you agree to
Microsoft's terms of use:
https://www.microsoft.com/en-us/legal/terms-of-use

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
sed \
    -e 's,__VERSION__,%version,' \
    -e 's,__RELEASE__,%release,' \
    -e 's,__NAME__,%name,' \
    xone-dl-firmware.sh.in > xone-dl-firmware.sh

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
install -m 0755 xone-dl-firmware.sh %{buildroot}%{_libexecdir}/%{name}/xone-dl-firmware.sh

mkdir -p %buildroot/usr/share/doc/%{name}
touch %buildroot/usr/share/doc/%{name}/MICROSOFT-TOS.html

mkdir -p %buildroot/usr/lib/firmware
touch %buildroot/usr/lib/firmware/xone_dongle_02e6.bin
touch %buildroot/usr/lib/firmware/xone_dongle_02fe.bin
touch %buildroot/usr/lib/firmware/xone_dongle_02f9.bin
touch %buildroot/usr/lib/firmware/xone_dongle_091e.bin

mkdir -p %{buildroot}/usr/share/%{name}
mv firmware.sha256 %{buildroot}/usr/share/%{name}

# Store update messages under /usr/share to work with transactional-update snapshots
mkdir -p %{buildroot}/usr/share/%{name}/update-messages
touch %{buildroot}/usr/share/%{name}/update-messages/%name-%version-%release-1

%posttrans
%{_libexecdir}/%{name}/xone-dl-firmware.sh --no-fail || :

%files
%license COPYING
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/xone-dl-firmware.sh
%dir /usr/share/doc/%{name}
%ghost /usr/share/doc/%{name}/MICROSOFT-TOS.html
%ghost /usr/lib/firmware/xone_dongle_02e6.bin
%ghost /usr/lib/firmware/xone_dongle_02fe.bin
%ghost /usr/lib/firmware/xone_dongle_02f9.bin
%ghost /usr/lib/firmware/xone_dongle_091e.bin
%dir /usr/share/%{name}
%dir /usr/share/%{name}/update-messages
%ghost /usr/share/%{name}/update-messages/%name-%version-%release-1
/usr/share/%{name}/firmware.sha256

%changelog
