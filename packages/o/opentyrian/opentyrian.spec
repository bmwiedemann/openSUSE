#
# spec file for package opentyrian
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


Name:           opentyrian
Version:        2.1.20130907
Release:        0
Summary:        An arcade-style vertical scrolling shooter
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/opentyrian/opentyrian
Source:         https://github.com/opentyrian/opentyrian/archive/v2.1.20130907.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://github.com/opentyrian/opentyrian/pull/13
Patch0:         appdata.patch
# PATCH-FIX-UPSTREAM https://github.com/opentyrian/opentyrian/commit/962ee8fc46ca51691bde1c8c1022dacbe8a037ed
Patch1:         opl.patch
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  boost-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files

%description
OpenTyrian is a port of the DOS shoot-em-up Tyrian. Thanks to Jason Emery,
the developers were given a copy of the Tyrian source to port but
not redistribute. That code has since been ported from Turbo Pascal to C
using SDL, making it easily cross-platform. The 'Classic' port involves
minimal changes, but the 'Enhanced' port will feature further development.
Tyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed
to fight Microsol and save the galaxy.

%prep
%autosetup -p1
chmod -x CREDITS

%build
make %{?_smp_mflags} STRIP=/bin/true MAKECMDGOALS=release

%install
# install binaries
install -D -m 0755 opentyrian %{buildroot}%{_libexecdir}/%{name}/opentyrian
# install wrapper
mkdir -p %{buildroot}%{_bindir}
cat <<EOT >>%{buildroot}%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/opentyrian
%{_libexecdir}/%{name}/opentyrian
cd -
EOT
chmod +x %{buildroot}%{_bindir}/%{name}
# install man page
install -D -m 0644 linux/man/opentyrian.6 %{buildroot}%{_mandir}/man6/opentyrian.6
# install icon and desktop file
for res in 128 48 32 24 22; do
  install -D -m 0644 linux/icons/tyrian-$res.png "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps/opentyrian.png"
done
install -D -m 0644 linux/opentyrian.desktop %{buildroot}%{_datadir}/applications/opentyrian.desktop
install -D -m 0644 linux/opentyrian.appdata.xml %{buildroot}%{_datadir}/appdata/opentyrian.appdata.xml
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

%files
%license COPYING
%doc CREDITS NEWS README
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_mandir}/man6/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
