#
# spec file for package waylock
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


%global _zig_wayland_ver   65475badb37fdfa06ac091554fdc81689a37a72a
%global _zig_xkbcommon_ver 7b188de0ba794b52eb70340abf2469b858630816
Name:           waylock
Version:        0.6.4
Release:        0
Summary:        Small screenlocker for Wayland compositors
License:        ISC
URL:            https://codeberg.org/ifreund/waylock
Source0:        https://codeberg.org/ifreund/waylock/archive/v%{version}.tar.gz
Source1:        waylock.pamd
Source2:        https://isaacfreund.com/public_key.txt#/%{name}.keyring
Source3:        https://codeberg.org/ifreund/waylock/releases/download/v%{version}/waylock-%{version}.tar.gz.sig
Source4:        https://codeberg.org/ifreund/zig-wayland/archive/%{_zig_wayland_ver}.tar.gz#/zig-wayland.tar.gz
Source5:        https://codeberg.org/ifreund/zig-xkbcommon/archive/%{_zig_xkbcommon_ver}.tar.gz#/zig-xkbcommon.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(xkbcommon)

%description
Screenlocker for Wayland compositors implementing ext-session-lock-v1.
(The v1 protocol is robust in that a crashing locker does not
cause the session to be unlocked.)

%prep
%setup -n %{name}

# Replace with configuration that works in openSUSE
cp %{SOURCE1} ./pam.d/waylock

tar xvf %{SOURCE4} -C deps/
tar xvf %{SOURCE5} -C deps/

%build
%zig_build -Dpie

%install
%zig_install -Dpie

# Removes rpmlint error: filelist-forbidden-move-to-usr error
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/%{name} %{buildroot}%{_pam_vendordir}/%{name}
rm -rfv %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%doc README.md
%{_bindir}/waylock
%{_mandir}/man1/waylock.1%{?ext_man}
%{_pam_vendordir}/waylock

%changelog
