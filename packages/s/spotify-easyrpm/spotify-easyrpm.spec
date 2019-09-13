#
# spec file for package spotify-easyrpm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spotify-easyrpm
Version:        2.0.3
Release:        0
Summary:        Download, convert and install the Spotify for Linux package
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/megamaced/spotify-easyrpm
Source:         %{name}-%{version}.tar.gz
Requires:	rpm-build
Requires:	createrepo
Requires:	update-desktop-files
BuildArch:      noarch

%description
Spotify-easyrpm is a script which downloads the latest debian package from the Spotify
repository and converts it into an RPM for installation

Automated updates are also supported and installed through the system update manager

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
