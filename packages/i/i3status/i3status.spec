#
# spec file for package i3status
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2014 Thomas Pfeiffer <email@pfeiffer.pw>
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


Name:           i3status
Version:        2.15
Release:        0
Summary:        I3 Status Bar
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://i3wm.org/i3status/
Source0:        %{url}/%{name}-%{version}.tar.xz
Source1:        %{url}/%{name}-%{version}.tar.xz.asc
# Michael Stapelberg's GPG key:
# 424E14D703E7C6D43D9D6F364E7160ED4AC8EE1D
Source2:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(yajl)
# man pages
BuildRequires:  asciidoc
BuildRequires:  xmlto

%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system
calls, as one generally wants to update such status lines every
second so that the bar is updated even under load. It saves a bit of
energy by being more efficient than shell commands.

%prep
%autosetup

for f in contrib/*py; do
    sed -i.orig "s:^#\!%{_bindir}/env\s\+python\s\?$:#!/usr/bin/python3:" $f
    touch -r $f.orig $f
    rm $f.orig
done
for f in contrib/*pl; do
    sed -i.orig "s:^#\!%{_bindir}/env\s\+perl\s\?$:#!/usr/bin/perl:" $f
    touch -r $f.orig $f
    rm $f.orig
done

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc CHANGELOG contrib/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
