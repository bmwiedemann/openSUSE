#
# spec file for package libretro-database
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libretro-database
Version:        1.8.7
Release:        0
Summary:        RetroArch Database
License:        MIT
Group:          System/Emulators/Other
URL:            https://github.com/libretro/%{name}

Source:         https://github.com/libretro/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  make
BuildArch:      noarch

Requires:       retroarch

%description
RetroArch incoporates a ROM scanning system to automatically produce playlists.
Each ROM that is scanned by the playlist generator is checked against a database
of ROMs that are known to be good copies.

This package provides data to allow RetroArch identify ROMs and generate playlists.

%prep
%setup -q

%build

%install
%make_install

%fdupes -s %{buildroot}

%files
%license COPYING
%dir %{_datadir}/libretro
%{_datadir}/libretro/database

%changelog
