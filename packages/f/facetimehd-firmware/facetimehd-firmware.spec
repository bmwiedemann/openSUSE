#
# spec file for package facetimehd-firmware
#
# Copyright (c) 2021 SUSE LLC
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


Name:           facetimehd-firmware
Version:        1.0
Release:        0
Summary:        FacetimeHD firmware download and extraction tool
License:        GPL-2.0-only
URL:            https://github.com/patjak/facetimehd-firmware
Source0:        https://github.com/patjak/facetimehd-firmware/archive/master.zip
BuildRequires:  unzip
Requires:       coreutils
Requires:       cpio
Requires:       curl
Requires:       unzip
Requires:       xz
BuildArch:      noarch

%description
FacetimeHD firmware download and extraction tool

%prep
%setup -q -n facetimehd-firmware-master

%build

%install
%suse_install_update_script facetimehd-firmware-install.sh
mkdir -p %{buildroot}/lib/firmware/facetimehd

%files
%{_localstatedir}/adm/update-scripts/*
%dir /lib/firmware/facetimehd
%ghost /lib/firmware/facetimehd/firmware.bin

%changelog
