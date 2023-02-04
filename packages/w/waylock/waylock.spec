#
# spec file for package waylock
#
# Copyright (c) 2022 SUSE LLC
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


Name:           waylock
Version:        0.6.1
Release:        0
Summary:        Small screenlocker for Wayland compositors
License:        ISC
URL:            https://github.com/ifreund/waylock
Source0:        https://github.com/ifreund/waylock/releases/download/v%{version}/waylock-%{version}.tar.gz
Source1:        waylock.pamd
Source2:        https://isaacfreund.com/public_key.txt#/%{name}.keyring
Source3:        https://github.com/ifreund/waylock/releases/download/v%{version}/waylock-%{version}.tar.gz.sig
Patch0:         0000-ignore-password-submission-before-locked-event.patch
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(wlroots) >= 0.15.0
BuildRequires:  pkgconfig(xkbcommon)
ExclusiveArch:  x86_64 aarch64 riscv64 %{mips64}

%description
Small screenlocker for Wayland compositors implementing ext-session-lock-v1. 
The ext-session-lock-v1 protocol is significantly more robust than previous client-side Wayland screen locking approaches.
Importantly, the screenlocker crashing does not cause the session to be unlocked.

%prep
%autosetup -n %{name}-%{version} -p1
# Replace with configuration that works in openSUSE
cp %{SOURCE1} ./pam.d/waylock

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
