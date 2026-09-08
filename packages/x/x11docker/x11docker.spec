#
# spec file for package x11docker
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


Name:           x11docker
Version:        7.8.0
Release:        0
Summary:        Tool for running GUI applications in containers
License:        MIT
URL:            https://github.com/mviereck/x11docker
Source0:        https://github.com/mviereck/x11docker/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  hicolor-icon-theme
Requires:       (jq or python3)
Requires:       (podman or docker or nerdctl)
Recommends:     catatonit
Recommends:     libxcvt
Recommends:     weston
Recommends:     xauth
Recommends:     xclip
Recommends:     xdotool
Recommends:     xdpyinfo
Recommends:     xhost
Recommends:     xinit
Recommends:     xorg-x11-server-Xvfb
Recommends:     xorg-x11-server-extra
Recommends:     xpra
Recommends:     xrandr
Recommends:     xwayland

%description
x11docker runs graphical desktop applications and entire desktop
environments in Linux containers. It can use Docker, Podman, or nerdctl
as container backend and starts separate X or Wayland display servers
to reduce common X11 security risks.

%prep
%autosetup
sed -i \
  -e '1s@^#! */usr/bin/env bash@#!/usr/bin/bash@' \
  -e 's/Packagedversion="no"/Packagedversion="yes"/' \
  x11docker

%build

%install
install -Dpm0755 x11docker %{buildroot}%{_bindir}/x11docker
install -Dpm0644 x11docker.man %{buildroot}%{_mandir}/man1/x11docker.1
install -Dpm0644 x11docker.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/x11docker.png

%check
bash -n x11docker
head -n 1 x11docker | grep -qx '#!/usr/bin/bash'
grep -q '^Packagedversion="yes"' x11docker
test "$(./x11docker --version)" = "%{version}"
./x11docker --help > x11docker-help.txt
! grep -q -- '--update' x11docker-help.txt
grep -q 'are not supported in packaged versions of x11docker' x11docker

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md TODO.md paper.md paper.bib
%{_bindir}/x11docker
%{_datadir}/icons/hicolor/64x64/apps/x11docker.png
%{_mandir}/man1/x11docker.1%{?ext_man}

%changelog
