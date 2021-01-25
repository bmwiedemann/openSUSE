#
# spec file for package Hawck
#
# Copyright (c) 2021 SUSE LLC
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


Name:           Hawck
Version:        0.7.1
Release:        0
Summary:        Key-rebinding daemon for Linux
License:        BSD-2-Clause
URL:            https://github.com/snyball/Hawck
Source0:        https://github.com/snyball/Hawck/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM Hawck-kernel_version.patch
Patch0:         Hawck-kernel_version.patch
BuildRequires:  fdupes
%if 0%{?suse_version} > 1500
BuildRequires:  gcc
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(lua) >= 5.3
BuildRequires:  pkgconfig(systemd)
Requires:       libnotify-tools

%description
A key-rebinding system that works on Wayland, X11 and on console ttys.
Hawck intercepts key presses and runs corresponding Lua scripts.

%prep
%autosetup -p1
# Use SUSE paths, also consider using %%_distconfdir where supported
sed -e '/install.*LICENSE/s/^/#/' \
    -e '/install.*LLib/s/755/644/' \
    -e 's|/etc/udev/rules.d|%{_udevrulesdir}|' \
    -e 's|/etc/modules-load.d|%{_modulesloaddir}|' \
    -e 's|/etc/hawck|%{_datadir}/hawck|' \
    -i bin/hawck-install.sh bin/hawck-user-setup.sh

%build
export CC=gcc
export CXX=g++
test -x "$(type -p gcc-10)" && export CC=gcc-10
test -x "$(type -p g++-10)" && export CXX=g++-10
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sbindir}
pushd %{buildroot}%{_sbindir}
ln -s service rchawck-inputd
popd
%fdupes %{buildroot}%{_datadir}

%pre
%service_add_pre hawck-inputd.service

%post
%service_add_post hawck-inputd.service

%preun
%service_del_preun hawck-inputd.service

%postun
%service_del_postun hawck-inputd.service

%files
%license LICENSE
%doc README.md

%{_bindir}/hawck-add
%{_bindir}/hawck-inputd
%{_bindir}/hawck-macrod
%{_bindir}/hwk2lua
%{_sbindir}/rchawck-inputd
%dir %{_datadir}/hawck
%dir %{_datadir}/hawck/bin
%dir %{_datadir}/hawck/icons
%dir %{_datadir}/hawck/keymaps
%dir %{_datadir}/hawck/keymaps/qwerty
%dir %{_datadir}/hawck/keys
%dir %{_datadir}/hawck/LLib
%dir %{_datadir}/hawck/scripts
%{_datadir}/hawck/bin/get-lua-errors.sh
%{_datadir}/hawck/bin/hawck-add.sh
%{_datadir}/hawck/bin/hawck-macrod.desktop
%{_datadir}/hawck/bin/hawck-user-setup
%{_datadir}/hawck/bin/kill-9-hawck.sh
%{_datadir}/hawck/bin/lskbd
%{_datadir}/hawck/icons/alt_hawck_logo_128x128.png
%{_datadir}/hawck/icons/alt_hawck_logo_v2_red_*.png
%{_datadir}/hawck/icons/alt_hawck_logo_v2_red_with_text.png
%{_datadir}/hawck/keymaps/aliases.lua
%{_datadir}/hawck/keymaps/default_linux.lua
%{_datadir}/hawck/keymaps/qwerty/no.map
%{_datadir}/hawck/keys/__UNSAFE_MODE.csv
%{_datadir}/hawck/LLib/app.lua
%{_datadir}/hawck/LLib/builtins.lua
%{_datadir}/hawck/LLib/cfg.lua
%{_datadir}/hawck/LLib/config.lua
%{_datadir}/hawck/LLib/Hawck.lua
%{_datadir}/hawck/LLib/init.lua
%{_datadir}/hawck/LLib/json.lua
%{_datadir}/hawck/LLib/kbd.lua
%{_datadir}/hawck/LLib/Keymap.lua
%{_datadir}/hawck/LLib/match.lua
%{_datadir}/hawck/LLib/Notify.lua
%{_datadir}/hawck/LLib/strict.lua
%{_datadir}/hawck/LLib/utils.lua
%{_datadir}/hawck/cfg.lua
%{_datadir}/hawck/scripts/example.hwk
%{_datadir}/icons/hicolor/*/apps/hawck.png
%{_mandir}/man1/hawck-inputd.1%{?ext_man}
%{_mandir}/man1/hawck-macrod.1%{?ext_man}
%{_modulesloaddir}/hawck-uinput.conf
%{_udevrulesdir}/99-hawck-input.rules
%{_unitdir}/hawck-inputd.service
%{_userunitdir}/hawck-macrod.service

%changelog
