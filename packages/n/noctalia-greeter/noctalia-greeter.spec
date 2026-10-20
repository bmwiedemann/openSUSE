#
# spec file for package noctalia-greeter
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


Name:           noctalia-greeter
Version:        1.7.0
Release:        0
Summary:        Greeter for Noctalia v5
License:        MIT
URL:            https://github.com/noctalia-dev/noctalia-greeter
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(stb)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)

# Runtime deps
Requires:       greetd
Requires:       dbus-1

Conflicts:      noctalia-greeter-git

%description
Noctalia Greeter is the screen you see before your desktop session starts. It lets you pick a user, enter your password, choose a Wayland session, and pick a color scheme - with the same visual language as Noctalia Shell

It is built for greetd: greetd starts a small Wayland compositor (Cage), and the greeter runs inside that session. It is a login UI only, not a desktop shell or compositor

Pair it with Noctalia Shell v5 if you want wallpaper and palette synced from the shell settings

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

chmod 0644 %{buildroot}%{_datadir}/noctalia-greeter/greetd_setup_lib.sh

sed -i '1c\#!/usr/bin/sh' \
    %{buildroot}%{_bindir}/noctalia-greeter-session \
    %{buildroot}%{_bindir}/noctalia-greeter-print-greetd-config \
		%{buildroot}%{_bindir}/noctalia-greeter-xsession

for script in \
    %{buildroot}%{_datadir}/noctalia-greeter/*.sh
do
    if head -n1 "$script" | grep -q '^#!/usr/bin/env bash'; then
        sed -i '1c\#!/usr/bin/bash' "$script"
    elif head -n1 "$script" | grep -q '^#!/usr/bin/env sh'; then
        sed -i '1c\#!/usr/bin/sh' "$script"
    fi
done

%files
%license LICENSE
%doc README.md
%{_bindir}/noctalia-greeter
%{_bindir}/noctalia-greeter-xsession
%{_bindir}/noctalia-greeter-compositor
%{_bindir}/noctalia-greeter-session
%{_bindir}/noctalia-greeter-apply-appearance
%{_bindir}/noctalia-greeter-print-greetd-config
%{_datadir}/noctalia-greeter
%{_datadir}/polkit-1/actions/org.noctalia.greeter.apply-appearance.policy
/usr/lib/tmpfiles.d

%changelog
