#
# spec file for package jupiter-dock-updater-bin
#
# Copyright (c) 2025 SUSE LLC
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

Name:           jupiter-dock-updater-bin
Version:        20250220.02
Release:        0%{?dist}
Summary:        Jupiter Dock Updater
# The downloaded content is proprietary / without explicit license.
# This package itself only ships the helper script and placeholders.
License:        GPL-3.0-or-later
URL:            https://gitlab.com/evlaV/jupiter-dock-updater-bin

Source0:        jupiter-dock-updater.sh.in
Source1:        COPYING
Source2:        jupiter-dock-updater.pkg.sha256
Source3:        jupiter-dock-updater-bin.rpmlintrc

Requires:       curl
Requires:       tar
Requires:       zstd
ExclusiveArch:  x86_64

%description
This package installs an update script which downloads the Jupiter
Dock firmware updater files from Valve's SteamOS repositories and
installs them into /usr/lib/jupiter-dock-updater.

The downloaded files are proprietary and are not shipped as part
of this package.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
sed \
    -e 's,__VERSION__,%version,' \
    -e 's,__RELEASE__,%release,' \
    -e 's,__NAME__,%name,' \
    jupiter-dock-updater.sh.in > jupiter-dock-updater.sh

%install
%suse_install_update_script jupiter-dock-updater.sh

mkdir -p %buildroot/var/adm/update-messages
touch %buildroot/var/adm/update-messages/%name-%version-%release-1

mkdir -p %buildroot/usr/lib/jupiter-dock-updater
touch %buildroot/usr/lib/jupiter-dock-updater/hub_update
touch %buildroot/usr/lib/jupiter-dock-updater/jaguar-b0_LUXSHARE_spi_image_V0.013.15.0.128_20250213.bin
touch %buildroot/usr/lib/jupiter-dock-updater/jaguar-b0_mca_i2c_isp_driver_payload.bin
touch %buildroot/usr/lib/jupiter-dock-updater/jupiter-dock-updater-mock.sh
touch %buildroot/usr/lib/jupiter-dock-updater/jupiter-dock-updater.sh
touch %buildroot/usr/lib/jupiter-dock-updater/update.ini

mkdir -p %{buildroot}/usr/share/%{name}
mv jupiter-dock-updater.pkg.sha256 %{buildroot}/usr/share/%{name}

%files
%license COPYING
/var/adm/update-scripts/*
%ghost /var/adm/update-messages/%name-%version-%release-1
%dir /usr/lib/jupiter-dock-updater
%ghost /usr/lib/jupiter-dock-updater/hub_update
%ghost /usr/lib/jupiter-dock-updater/jaguar-b0_LUXSHARE_spi_image_V0.013.15.0.128_20250213.bin
%ghost /usr/lib/jupiter-dock-updater/jaguar-b0_mca_i2c_isp_driver_payload.bin
%ghost /usr/lib/jupiter-dock-updater/jupiter-dock-updater-mock.sh
%ghost /usr/lib/jupiter-dock-updater/jupiter-dock-updater.sh
%ghost /usr/lib/jupiter-dock-updater/update.ini
/usr/share/%{name}

%changelog
