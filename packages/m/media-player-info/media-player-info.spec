#
# spec file for package media-player-info
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d

Name:           media-player-info
Version:        23
Release:        0
Summary:        Media Player Information
# Note on license: some files in the tools subdirectories are GPL-2.0+ (or
# MIT); those files are not shipped at all in the resulting binary package.
# Hence, the binary package is indeed still BSD-3-Clause.
License:        BSD-3-Clause
Group:          System/GUI/Other
Url:            http://hal.freedesktop.org/releases/
Source:         http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM reproducible.patch bwiedemann@suse.com -- Make build reproducible.
Patch0:         reproducible.patch
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  pkgconfig(udev)
%if 0%{?suse_version} > 1230
BuildRequires:  pkgconfig(systemd)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains a repository of data files describing media player
(mostly USB Mass Storage ones) capabilities. These files contain information
about the directory layout to use to add music to these devices, about the
supported file formats, ... These capabilities used to be provided by HAL
in the 10-usb-music-players.fdi file but had to be moved elsewhere as part
of the big HALectomy.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?jobs:-j%jobs}

%install
%makeinstall

%if 0%{?suse_version} > 1230
%post
%udev_hwdb_update
%udev_rules_update

%postun
if [ $1 -eq 0 ]; then
        %udev_hwdb_update
        %udev_rules_update
fi
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
## WARNING: if adding other files to the package, check their license (see note above License tag)
%dir %{_datadir}/media-player-info
%{_datadir}/media-player-info/*.mpi
%if 0%{?suse_version} > 1230
%{_udevhwdbdir}/20-usb-media-players.hwdb
%endif
%{_udevrulesdir}/40-usb-media-players.rules
## WARNING: if adding other files to the package, check their license (see note above License tag)

%changelog
