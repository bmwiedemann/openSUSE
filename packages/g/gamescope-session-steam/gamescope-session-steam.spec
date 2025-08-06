#
# spec file for package gamescope-session-steam
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

Name:           gamescope-session-steam
Version:        1+git20250418.7104815
Release:        0
Summary:        Steam Big Picture Mode session based on gamescope
License:        MIT
URL:            https://github.com/TobiPeterG/gamescope-session-steam
Source0:        %{name}-%{version}.tar.xz
Source1:        jupiter-biosupdate
Source2:        steamos-select-branch
Source3:        steamos-update
Source99:       %{name}.rpmlintrc
BuildRequires:  dejavu-fonts
BuildRequires:  gamescope-session
BuildRequires:  pkgconfig(systemd)
Requires:       gamescope
Requires:       gamescope-session
#!BuildIgnore:  gamescope
Requires:       python3
Requires:       dejavu-fonts
Recommends:     steam
BuildArch:      noarch

%description
Steam Big Picture Mode session based on gamescope.
This opens Steam in the "SteamOS" mode.

%package generic
Summary:        Missing bits for non Yuga Linux systems
URL:            https://github.com/TobiPeterG/gamescope-session-steam
Requires:       gamescope-session-steam
Conflicts:      deckifier
BuildArch:      noarch

%description generic
Missing bits for non Yuga Linux systems with basic binaries called by Steam.

%prep
%autosetup -p1

%build

%install
cp -rv usr %{buildroot}/usr

# font workaround for initial big picture mode startup
mkdir -p %{buildroot}%{_datadir}/fonts/truetype/ttf-dejavu
ln -s %{_datadir}/fonts/truetype/DejaVuSans.ttf %{buildroot}%{_datadir}/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
sed -i '1s|^#!/bin/env python3|#!/usr/bin/python3|' %{buildroot}%{_bindir}/steam-http-loader
chmod +x %{buildroot}%{_datadir}/gamescope-session-plus/sessions.d/steam

# remove ChimeraOS specific files
rm -r %{buildroot}%{_datadir}/polkit-1/actions
rm %{buildroot}%{_bindir}/jupiter-biosupdate
rm %{buildroot}%{_bindir}/steamos-select-branch
rm %{buildroot}%{_bindir}/steamos-update

# override ChimeraOS specific files
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/steamos-polkit-helpers/jupiter-biosupdate
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/steamos-polkit-helpers/steamos-select-branch
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/steamos-polkit-helpers/steamos-update

%files
%{_datadir}/fonts/*
%{_datadir}/applications
%{_datadir}/gamescope-session-plus/sessions.d
%{_datadir}/wayland-sessions

%{_bindir}/steam-http-loader

%files generic
%{_bindir}/steamos-session-select
%dir %{_bindir}/steamos-polkit-helpers
%{_bindir}/steamos-polkit-helpers/jupiter-biosupdate
%{_bindir}/steamos-polkit-helpers/steamos-select-branch
%{_bindir}/steamos-polkit-helpers/steamos-update

%changelog
