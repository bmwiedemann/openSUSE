#
# spec file for package spotify-easyrpm
#
# Copyright (c) 2023 SUSE LLC
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


Name:           spotify-easyrpm
Version:        3.0.4
Release:        0
Summary:        Tool to download, convert and install the Spotify for Linux package
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/megamaced/spotify-easyrpm
Source:         %{name}-%{version}.tar.gz
Requires:       createrepo_c
Requires:       jq
Requires:       rpm-build
Requires:       squashfs
Requires:       update-desktop-files
BuildArch:      noarch

%description
Spotify-easyrpm is a script which downloads the latest snap package
from the snapcraft.io repository and converts it into an RPM for
installation.

Automated updates are also supported and installed through the system
update manager.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/spotify-easyrpm

%changelog
