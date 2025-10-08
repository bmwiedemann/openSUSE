#
# spec file for package waylock
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        1.5.0
Release:        0
Summary:        Small screenlocker for Wayland compositors
License:        ISC
URL:            https://codeberg.org/ifreund/waylock
Source0:        https://codeberg.org/ifreund/waylock/releases/download/v%{version}/waylock-%{version}.tar.gz
Source1:        waylock.pamd
Source2:        https://isaacfreund.com/public_key.txt#/%{name}.keyring
Source3:        https://codeberg.org/ifreund/waylock/releases/download/v%{version}/waylock-%{version}.tar.gz.sig
Source4:        vendor.tar.zst
Patch1:         add-experimental-non-llvm-zig-backend.patch
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  zstd
BuildRequires:  (zig >= 0.15.0 with zig < 0.16)
BuildRequires:  (zig-rpm-macros >= 0.15.0 with zig-rpm-macros < 0.16)
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
%autosetup -a4 -p1

# Replace with configuration that works in openSUSE
cp %{SOURCE1} ./pam.d/waylock

%build
%global zig_opts --global-cache-dir vendor/ -Dpie -Dno-llvm
%zig_build %{zig_opts}

%install
%zig_install %{zig_opts}

# Removes rpmlint error: filelist-forbidden-move-to-usr error
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/%{name} %{buildroot}%{_pam_vendordir}/%{name}
rm -rfv %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%doc README.md PACKAGING.md
%{_bindir}/waylock
%{_mandir}/man1/waylock.1%{?ext_man}
%{_pam_vendordir}/waylock

%changelog
