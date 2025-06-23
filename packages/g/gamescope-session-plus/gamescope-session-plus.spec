#
# spec file for package gamescope-session-plus
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

Name:           gamescope-session-plus
Version:        1+git20250407.5030491
Release:        0
Summary:        A gamescope-based user session
License:        MIT
URL:            https://github.com/ChimeraOS/gamescope-session
Source0:        %{name}-%{version}.tar.xz
Provides:       gamescope-session
Conflicts:      gamescope-session

BuildRequires:  pkgconfig(systemd)

Requires:       gamescope
#!BuildIgnore:  gamescope
Requires:       python3

BuildArch:      noarch

%description
A gamescope-based user session. This sub-package only installs the
common assets used by real sessions such as gamescope-session-steam
or OpenGamepadUI.

%prep
%autosetup -n %{name}-%{version}

%build

%install

# user-visible helper scripts
install -D -m0755 usr/bin/export-gpu            %{buildroot}%{_bindir}/export-gpu
install -D -m0755 usr/bin/gamescope-session-plus %{buildroot}%{_bindir}/gamescope-session-plus

# shared data tree under /usr/share
for f in $(find usr/share/gamescope-session-plus -type f); do
  install -D -m0644 "$f" \
      "%{buildroot}%{_datadir}/gamescope-session-plus/${f#usr/share/gamescope-session-plus/}"
done

# systemd user units
for u in usr/lib/systemd/user/*; do
  install -D -m0644 "$u" \
      "%{buildroot}%{_userunitdir}/$(basename "$u")"
done

chmod 755 %{buildroot}%{_datadir}/gamescope-session-plus/gamescope-session-plus

%files
%license LICENSE
%doc    README.md

%dir %{_datadir}/gamescope-session-plus

%{_datadir}/gamescope-session-plus/device-quirks
%{_datadir}/gamescope-session-plus/gamescope-session-plus

%{_bindir}/export-gpu
%{_bindir}/gamescope-session-plus

%{_userunitdir}/*

%changelog
