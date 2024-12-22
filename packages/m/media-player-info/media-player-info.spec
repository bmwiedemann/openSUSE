#
# spec file for package media-player-info
#
# Copyright (c) 2024 SUSE LLC
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
Version:        26
Release:        0
Summary:        Media Player Information
# Note on license: some files in the tools subdirectories are GPL-2.0+ (or
# MIT); those files are not shipped at all in the resulting binary package.
# Hence, the binary package is indeed still BSD-3-Clause.
License:        BSD-3-Clause
Group:          System/GUI/Other
URL:            https://www.freedesktop.org/wiki/Software/media-player-info/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildArch:      noarch

%description
This package contains a repository of data files describing media player
(mostly USB Mass Storage ones) capabilities. These files contain information
about the directory layout to use to add music to these devices, about the
supported file formats, ... These capabilities used to be provided by HAL
in the 10-usb-music-players.fdi file but had to be moved elsewhere as part
of the big HALectomy.

%prep
%autosetup

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

%post
%{udev_hwdb_update}
%udev_rules_update

%postun
if [ $1 -eq 0 ]; then
        %{udev_hwdb_update}
        %udev_rules_update
fi

%files
%license COPYING
%doc AUTHORS NEWS
%dir %{_datadir}/media-player-info
%{_datadir}/media-player-info/*.mpi
%{_udevhwdbdir}/20-usb-media-players.hwdb
%{_udevrulesdir}/40-usb-media-players.rules
%{_datadir}/metainfo/org.freedesktop.media_player_info.metainfo.xml

%changelog
